import sys
import Imath
from PIL import Image
import pyopencl as cl
import numpy

import threading
from compy.parameter import CompyParameter
import compy.network_manager as network_manager


class CLC_Node(object):
    """ Base class for nodes graph representation """

    def __init__(self, parent=None):
        self.parent = parent
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.color = (0.5, 1.0, 0.25,)
        self.parms = {}
        self.icon = None
        self.parms = {}

    def setPos(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def getPos(self):
        return (self.x_pos, self.y_pos,)

    def getIcon(self):
    	return self.icon    

    def addParameter(self, name, parm_type, value=None):
    	parm = CompyParameter(self, name, parm_type)
    	if value != None: parm.set(value)
    	self.parms[name] = parm

    def setParms(self, parameters):
		for parm in parameters:
			self.parms[parm].set(parameters[parm])		

    def __str__(self):
        return self.__class__.__name__

class CLC_Base(CLC_Node, network_manager.CLC_NetworkManager):
	# Base class for FX filters
	__fx__			= True # Indicated that this is FX node
	type_name		= None # This is a TYPE name for the particular FX node...
	
	def __init__(self, engine, parent):
		network_manager.CLC_NetworkManager.__init__(self)
		super(CLC_Base, self).__init__(parent)
		if engine:
			self.engine = engine
		else:
			raise BaseException("No engine specified !!!")
		
		self.width	= None	
		self.height	= None
		self.cooked	= False	

		self.devOutBuffer = None # Device output buffer. This buffer holds thre result image array

		self.image_format = cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.FLOAT)
		self.common_program = engine.load_program("common.cl")
		
		self.addParameter("bypass", bool, False)
		
	@property
	def size(self):
		return (self.width, self.height)
		
	@property	
	def area(self):	
		return self.width * self.height
		
	@property	
	def volume(self):	
		return self.area * 4

	@property
	def nbytes(self):
		return self.volume * 4
		
	@property
	def pitch(self):
		return self.width * 16		

	def cook(self):
		if self.cooked != True:
			for node in self.inputs():
				node.cook()
				
			try:
				self.compute()
			except:
				raise
			else:	 
				self.cooked = True
				return True
		else:
			print "%s node already cooked !" % self		

	def get_out_buffer(self):
		if self.cooked == False:
			self.cook()
		
		return self.devOutBuffer
		
	def show(self):
		if self.cooked == True:
			temp_buff = numpy.empty((self.width, self.height, 4), dtype = numpy.float16)
			self.engine.queue.finish()
			imgToShowBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.HALF_FLOAT), shape=self.size)
			
			evt = self.common_program.quantize_show(self.engine.queue, self.size, None, 
				self.devOutBuffer,
				imgToShowBuffer
			)
			evt.wait()
			
			print "Copying dev buffer %s to host buffer %s" % (self.get_out_buffer().size, temp_buff.nbytes)
			evt = cl.enqueue_copy(self.engine.queue, temp_buff, imgToShowBuffer, origin=(0,0), region=self.size)
			evt.wait()
			
			Image.frombuffer('RGBA', (self.width, self.height), temp_buff.astype(numpy.uint8), 'raw', 'RGBA', 0, 1).show()		
		else:
			raise BaseException("Unable to show uncooked source %s !!!" % self)					
