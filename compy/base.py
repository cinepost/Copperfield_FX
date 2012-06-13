import sys
import Imath
from PIL import Image
import pyopencl as cl
import numpy

import threading              

class CLC_Node(object):
	# Base class for nodes graph representation
	def __init__(self):
		self.title 	= self.name 	# Do incrementation here (Blur1, Blur2, Blur3, etc...)
		self.x_pos	= 0.0
		self.y_pos	= 0.0
		self.color	= (0.5, 1.0, 0.25,)
		
	def setPos(self, x, y):
		self.x_pos = x
		self.y_pos = y
		
	def getPos(self):
		return (self.x_pos, self.y_pos,)		

class CLC_Base(CLC_Node):
	# Base class for FX filters
	__cfx__			= True
	name			= None
	devOutBuffer 	= None
	parms			= {}
	
	def __init__(self, engine):
		if engine:
			self.engine = engine
		else:
			raise BaseException("No OpenCL engine specified !!!")
		
		self.width	= None	
		self.height	= None
		self.cooked	= False	
		self.inputs	= {}
		self.image_format = cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.FLOAT)
		self.parms = {
			"effectamount"	: 	1,
		}
		
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
			temp_buff = numpy.empty((self.width, self.height, 4)).astype(numpy.float32)
			print "Copying dev buffer %s to host buffer %s" % (self.get_out_buffer().size, temp_buff.nbytes)
			self.engine.queue.finish()
			evt = cl.enqueue_copy(self.engine.queue, temp_buff, self.devOutBuffer, origin=(0,0), region=self.size)
			evt.wait()
			Image.frombuffer('RGBA', (self.width, self.height), temp_buff.astype(numpy.uint8), 'raw', 'RGBA', 0, 1).show()		
		else:
			raise BaseException("Unable to show uncooked source %s !!!" % self)					

