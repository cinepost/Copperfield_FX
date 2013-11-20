import sys, string
import Imath
from PIL import Image
import pyopencl as cl
import numpy

import threading
from compy.parameter import CompyParameter
from compy.compy_string import CompyString
import compy.network_manager as network_manager


class CLC_Node(object):
	""" Base class for nodes graph rendering """

	def __init__(self):
		self.x_pos = 0.0
		self.y_pos = 0.0
		self.color = (0.5, 1.0, 0.25,)
		self.icon = None

	def setPos(self, x, y):
		self.x_pos = x
		self.y_pos = y

	def getPos(self):
		return (self.x_pos, self.y_pos,)

	def getIcon(self):
		return self.icon    				

class CLC_Base(CLC_Node, network_manager.CLC_NetworkManager):
	# Base class for OPs
	__op__			= True # Indicated that this is OP node
	type_name		= None # This is a TYPE name for the particular compositing OP ...
	
	def __init__(self, engine, parent):
		network_manager.CLC_NetworkManager.__init__(self, engine, parent, mask=None)
		super(CLC_Base, self).__init__()

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

	def isTimeDependent(self):
		return False			

	def cook(self, force=False, frame_range=()):

		if any(node.cooked is False for node in self.inputs()):
			print "Cooking inputs: %s" % [inp.name() for inp in self.inputs()]
			for node in self.inputs():
				node.cook()
				print "Node %s cooked!" % node.name()

		if self.cooked != True:
			try:
				print "Computing node %s" % self.name()
				self.compute()
			except:
				raise
			else:	 
				self.cooked = True
				return True
		else:
			print "%s node already cooked !" % self
			return True	

	def getOutDevBuffer(self):
		if self.cooked == False:
			self.cook()
		
		return self.devOutBuffer

	def getOutHostBuffer(self):
		print "Queue is %s" % self.engine.queue
		device_buffer = self.getOutDevBuffer()
		print "Device buffer is %s of size %s" % (device_buffer, device_buffer.size)
		host_buffer = numpy.empty((self.width, self.height, 4), dtype = numpy.float16)
		self.engine.queue.finish()
		print "Building quantized buffer for node %s with size %s" % (self, self.size)
		quantized_buffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.HALF_FLOAT), shape=self.size)	
		print "Quantized buffer is %s of size %s" % (quantized_buffer, quantized_buffer.size)
		print "Executing quantize program for node %s" % self.name()
		print "Queue is %s" % self.engine.queue

		with cl.CommandQueue(self.engine.ctx) as queue:
			evt = self.common_program.quantize_show(queue, self.size, None, device_buffer, quantized_buffer )
			print "Waiting for quantize program for node %s" % self.name()
			evt.wait()

		with cl.CommandQueue(self.engine.ctx) as queue:	
			evt = cl.enqueue_copy(queue, host_buffer, quantized_buffer, origin=(0,0), region=self.size)
			evt.wait()
		
		return host_buffer

	def show(self):
		try:
			host_buff = self.getOutHostBuffer()
			Image.frombuffer('RGBA', (self.width, self.height), host_buff.astype(numpy.uint8), 'raw', 'RGBA', 0, 1).show()		
		except:
			raise BaseException("Unable to show uncooked source %s !!!" % self)					
