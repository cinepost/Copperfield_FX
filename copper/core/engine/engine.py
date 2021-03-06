import sys, os
import pyopencl as cl
import pickle
import numpy
import uuid
import logging
from lazy import lazy
from pyopencl.tools import get_gl_sharing_context_properties
from PIL import Image

from PyQt5 import QtCore

from copper import settings
from copper.core.op.op_node import OP_Node
from copper.core.op.node_type import NodeTypeBase
from copper.core.op.node_type_category import DirectorNodeTypeCategory, ManagerNodeTypeCategory
from copper.core.op.base import OpRegistry
from copper.core.utils import CopperString
from copper.translators import CopperNullTranslator, boomShotTranslator
from copper.root_types import ROOT_Types

from .engine_signals import signals as engine_signals

try:
    from copper.ui.signals import ui_signals
except:
    ui_signals = None

logger = logging.getLogger(__name__)

class Engine(QtCore.QObject):
    programs    = {}
    app         = None
    filters     = {}
    network_cb  = None

    def __init__(self, device_type = settings.CL_DEVICE_TYPE, device_index=settings.CL_DEVICE_INDEX, cl_path=settings.CL_PROGRAMS_PATH): # "cpu" or "gpu" here or "ALL"
        QtCore.QObject.__init__(self)
        self._time = 0.0
        self._frame = 0
        self.__fps__ = 25.0
        self._cl_ctx = None
        self._cl_queue = None

        self._current_node = None

        self.signals = engine_signals
        self.ui_signals = ui_signals

        from copper.copper_cache import OpDataCache
        self._data_cache = OpDataCache(maxsize=1024) # One gig memory cache for op data

        logger.debug("Initializing engine of type %s" % device_type)
        self._devices = []
        platforms = cl.get_platforms()
        for platform in platforms:
            if device_type is "CPU":
                self._devices += platform.get_devices(cl.device_type.CPU)
            
            elif device_type is "GPU":
                self._devices += platform.get_devices(cl.device_type.GPU)
            
            elif device_type is "ALL":   
                self._devices += platform.get_devices(cl.device_type.ALL)   
            
            else:
                self._devices = None    
            
        if self._devices:       
            self.cl_path = cl_path
            self.cl_mode = True
            logger.info("Using Open_CL.")
        else:
            logger.error("NO OPEN_CL CAPABLE DEVICE FOUND !!!")
            exit(1)     

        logger.debug("Bundled with ops: %s \n Done." % OpRegistry._registry)

        # register translators
        self.translators = {}
        translators = [CopperNullTranslator(), boomShotTranslator() ]
        for translator in translators:
            self.translators[translator.registerExtension()] = translator
    
        # connect signals
        self.signals.cookNodeData[OP_Node].connect(self.cookNodeData)
        self.signals.getNodeByPath[str].connect(self.getNodeByPath)

        if self.ui_signals:
            self.ui_signals.cooperNodeSelected[OP_Node].connect(self.nodeSelected)

    @lazy
    def root(self):
        from copper.managers import ROOT_Network
        self._root = ROOT_Network(self)
        return self._root

    def node(self, path):
        return self.root.node(path)

    def pwd(self):
        return self._current_node or self.root

    def setPwd(self, node_or_path):
        ispath = isinstance(node_or_path, str)
        isnode = isinstance(node_or_path, OP_Node)
        assert isnode or ispath, "node_or_path should be either str ot OP_Node"
        if ispath:
            self._current_node = self.root.node(node_or_path)
        else:
            self._current_node = node_or_path

        self.signals.nodeSelected.emit(self._current_node)


    def set_network_change_callback(self, callback):
        self.network_cb = callback

    def call_network_changed_callback(self):
        if self.network_cb:
            logging.debug("Calling network change callback...")
            self.network_cb()       

    def load_program(self, filename):
        program_file = open("%s/%s" % (os.path.expandvars(self.cl_path), filename), 'r')
        program_code = program_file.read()
        program_file.close()
        return cl.Program(self.openclContext(), program_code).build()

    def have_gl(self):
        return cl.have_gl() 

    def openclContext(self, device_index=0):
        if not self._cl_ctx:
            cl_context_properties = []
            if self.have_gl():
                cl_context_properties += get_gl_sharing_context_properties()
            if device_index:
                self._cl_ctx = cl.Context(  properties=cl_context_properties,
                                        devices = [self._devices[device_index]])
            else:
                self._cl_ctx = cl.Context(  properties=cl_context_properties,
                                        devices = self._devices)

            logger.debug("OpenCL context created: %s" % self._cl_ctx)
        return self._cl_ctx
        
    def openclQueue(self):
        if not self._cl_queue:
            self._cl_queue = cl.CommandQueue(self.openclContext(), properties=cl.command_queue_properties.PROFILING_ENABLE)
        
        return self._cl_queue

    def fps(self):
        return self._fps

    def time(self):
        return self._time

    def frame(self):
        return self._frame      

    def setFps(self, fps):
        self.__fps__ = fps  

    def setTime(self, time):
        self.__time__ = time
        self.__frame__ = float(time) * float(self.__fps__)

    def setFrame(self, frame):
        self.__frame__ = frame
        self.__time__ = float(frame) / float(self.__fps__)          

    def flush(self):
        for net_name in self.__node_dict__:
            self.__node_dict__[net_name].flush()

    @QtCore.pyqtSlot(OP_Node)
    def cookNodeData(self, node):
        node.cook()

    @QtCore.pyqtSlot(OP_Node)
    def nodeSelected(self, node):
        self.setPwd(node)
        self.signals.nodeSelected[OP_Node].emit(node)

    @QtCore.pyqtSlot(str)
    def getNodeByPath(self, node_path):
        return self.root.node(node_path)

    def renderToFile(self, node_path, filename, frame = None):
        node = self.node(node_path)
        if frame:
            render_frame = frame
        else:
            render_frame = self.frame()

        self.setFrame(render_frame) 

        self.setFrame(frame)    
        render_file_name = CopperString(self.engine, filename).expandedString() 
        
        logger.info("OpenCL. Rendering frame %s for node %s to file: %s" % (render_frame, node.path(), render_file_name))
        buff = node.getOutHostBuffer()
        image = Image.frombuffer('RGBA', node.size, buff.astype(numpy.uint8), 'raw', 'RGBA', 0, 1)          

        if "lin" in sys.platform :
            # Flip image vertically
            image = image.transpose(Image.FLIP_TOP_BOTTOM)

        image.save(render_file_name, 'JPEG', quality=100)

    def save_project(self, filename):
        project_file = open(filename, "wb")

        # write out nodes
        node_list = []
        node_links = []
        for node in self.node("/img").children() + self.node("/out").children():
            node_list += node.dump(recursive=True, dump_parms=True)
            node_links += node.dumpLinks(recursive=True)

        project_file.write("nodes = %s\n" % node_list)
        project_file.write("links = %s\n" % node_links)
        project_file.close()

    def readFile(self, file_path):
        return open(file_path, "rb").read()

    def interpreter(self):
        import code, sys
        console = code.InteractiveConsole(locals={'hou': self})
        
        banner = "%s\n" % sys.version
        banner+= 'on %s\n' % sys.platform 
        banner+= 'CopperFX python interpreter\n'

        console.interact(banner)

    def open_project(self, filename):
        file_extension = filename.rsplit(".",1)[-1]
        translator = self.translators.get(file_extension, None)
        if not translator: raise BaseException("No translator found for file type \"%s\"" % file_extension)
        project_string = translator.translateToString(filename)
        project_code = compile(project_string, '<string>', 'exec')

        self.flush() # erase all node networks this engine holds
        ns = {}
        exec(project_code, ns)
        links = ns['links']
        
        # create nodes and fill parameters
        for node_desc in ns['nodes']:
            node = self.node(node_desc["path"]).createNode(node_desc["type"], node_desc["name"]) 
            if node_desc.get("parms"):
                node.setParms(node_desc["parms"])

        # set up links between nodes
        for link in ns['links']:
            from_node = self.node(link[0])
            to_node = self.node(link[1])
            input_index = link[3]
            to_node.setInput(input_index, from_node)        

        self.call_network_changed_callback()

    def build_test_project(self):
        #### ---- create simple scene for debug purposes
        
        ## Create out composite node
        out = self.node("out")

        ## Create composite output driver
        out_comp = out.createNode("comp")
        out_comp.setParms({"coppath": "/img/img1/file1", "copoutput": "~/Desktop/copper_test/img_test_$F4.jpg", "f1": 0, "f2": 25, "f3":1})

        ## First get image network
        img = self.node("img")
        
        ## Create composition
        comp = img.createNode("comp")

        obj = self.node("obj")

        #geo1 = obj.createNode("geo")
        #font1 = geo1.createNode("font")

        #ins = obj.createNode("instance")
        
        #geo2 = obj.createNode("geo", "geo1")
        #box = geo2.createNode("box")

        geo3 = obj.createNode("geo")
        file = geo3.createNode("file")
        file.setParms({"filename": "/home/max/dev/Copperfield_FX/test/geometry/cube.obj"})

        ## Create COP2_Render node
        render1 = comp.createNode("render")

        ## Create COP2_File node 
        file1 = comp.createNode("file")
        file1.setPosition((10, 10))
        #file1.setParms({"size1": 1280, "size2": 720, "filename": "~/Desktop/mythbuster.jpg"})

        ## Create COP2_blur node
        blur1 = comp.createNode("blur")
        blur1.setInput(0, render1)
        blur1.setParms({"blursize":0.01, "blursizey": 0.05, "useindepy" : True})

        ## Create COP2_Press node
        halftone1 = comp.createNode("halftone")
        halftone1.setParms({"quality":4, "density": 100})
        halftone1.setInput(0, blur1)

        self.setPwd(obj) 
