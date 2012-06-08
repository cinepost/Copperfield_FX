import numpy
import Imath
from PIL import Image
import pyopencl as cl

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import threading              

class CLC_Base(object):
	devOutBuffer 	= None
	width		 	= None	
	height		 	= None
	cooked		 	= False
	parms		 	= {
		"effectamount"	: 	1,
	}
	inputs			= {}
	
	def __init__(self, engine):
		if engine:
			self.engine = engine
		else:
			raise BaseException("No OpenCL engine specified !!!")
			
		self.image_format = cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.FLOAT)
	
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

	@property
	def is_cooked(self):
		return self.cooked		

	def cook(self):
		if not self.cooked:
			try:
				self.compute()
			except:
				self.cooked = False
				raise
			else:	 
				self.cooked = True
				print "Node %s cooked!" % self
				return True

	def get_out_buffer(self):
		if not self.is_cooked:
			self.cook()
		
		return self.devOutBuffer
		
	def show(self):
		if self.cooked:
			temp_buff = numpy.empty((self.width, self.height, 4)).astype(numpy.float32)
			print "Copying dev buffer %s to host buffer %s" % (self.get_out_buffer().size, temp_buff.nbytes)
			self.engine.queue.finish()
			evt = cl.enqueue_copy(self.engine.queue, temp_buff, self.devOutBuffer, origin=(0,0), region=self.size)
			evt.wait()
			Image.frombuffer('RGBA', (self.width, self.height), temp_buff.astype(numpy.uint8), 'raw', 'RGBA', 0, 1).show()		
			#Imath.PreviewImage(self.width, self.height, temp_buff.tostring())
		else:
			raise BaseException("Unable to show uncooked source %s !!!" % self)					

