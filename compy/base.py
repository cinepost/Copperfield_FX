import sys
import Imath
from PIL import Image
import pyopencl as cl
import numpy

import threading
from compy import parameter


class CLC_Node(object):
    # Base class for nodes graph representation
    name = None

    def __init__(self, parent=None):
        self.parent = parent
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.color = (0.5, 1.0, 0.25,)

    def setPos(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def getPos(self):
        return (self.x_pos, self.y_pos,)

    def __str__(self):
        return self.__class__.__name__

class CLC_Base(CLC_Node):
    # Base class for FX filters
    __fx__			= True # Indicated that this is FX node
    name			= None # This is a TYPE name for the particular FX node... don't be confused here

    def __init__(self, engine, parent):
        super(CLC_Base, self).__init__(parent)
        if engine:
            self.engine = engine
        else:
            raise BaseException("No engine specified !!!")

        self.width	= None
        self.height	= None
        self.cooked	= False
        self.inputs	= {}

        self.devOutBuffer = None # Device output buffer. This buffer holds thre result image array

        self.image_format = cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.FLOAT)
        self.common_program = engine.load_program("common.cl")
        self.parms = {
            "effectamount"	: 	parameter.CompyParameter(1),
        }

    @property
    def children(self):
        return None

    def setParms(self, parameters):
        self.parms.update(parameters)

    def setInput(self, layer_number, layer):
        self.inputs[layer_number] = layer

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
            for key in self.inputs.keys():
                self.inputs[key].cook()

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

