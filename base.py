import numpy
from PIL import Image
import pyopencl as cl

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import threading              

class CLC_Base(object):
	devOutBuffer = None
	width		 = 0	
	height		 = 0
	cooked		 = False
	
	def __init__(self, engine, width, height):
		if engine:
			self.engine = engine
		else:
			raise BaseException("No OpenCL engine specified !!!")
			
		if width !=0 and height !=0:
			self.width = width
			self.height = height	
		
	def load_program(self, filename):
		of = open("cl/%s" % filename, 'r')
		return cl.Program(self.engine.ctx, of.read()).build() #TODO cache program here
		
	@property
	def size(self):
		return (self.width, self.height)
		
	@property	
	def area(self):	
		return self.width * self.height
		
	@property	
	def volume(self):	
		return self.area * 3

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
				return True

	def get_out_buffer(self):
		return self.devOutBuffer

	def show(self):
		if self.cooked:
			temp_buff = numpy.zeros((self.width, self.height, 3)).astype(numpy.float32)
			cl.enqueue_copy(self.engine.queue, temp_buff, self.devOutBuffer).wait()
			self.engine.queue.finish()
			Image.frombuffer('RGB', (self.width, self.height), temp_buff.astype(numpy.uint8), 'raw', 'RGB', 0, 1).show()			
		else:
			raise BaseException("Unable to show uncooked source %s !!!" % self)					

