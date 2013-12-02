import sys, string
import Imath
from PIL import Image
import pyopencl as cl
import numpy

import threading
from compy.parameter import CompyParameter
from compy.compy_string import CompyString
from compy.op_manager import OP_Manager
from compy.cops.cop_plane import COP_Plane    				

class COP_Node(OP_Manager):
	# Base class for OPs
	__op__			= True # Indicated that this is OP node
	type_name		= None # This is a TYPE name for the particular compositing OP ...
	
	def __init__(self, engine, parent, mask=None):
		super(COP_Node, self).__init__(engine, parent, mask=mask)

		self.width	= None	
		self.height	= None
		self.cooked	= False	

		self.devOutBuffer = None # Device output buffer. This buffer holds thre result image array

		self.image_format = cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.FLOAT)
		self.common_program = engine.load_program("common.cl")
		
		self.addParameter("effectamount", float, 1.0, label="Effect Amount")
		self.__planes__ = {
			"C": COP_Plane(self, channel_names=['r','g','b'], dtype=float),
			"A": COP_Plane(self, dtype=float)
		}

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

	def planes(self):
		return self.__planes__.keys()

	def getPlane(self, plane_name):
		return self.__planes__.get(plane_name)	

	def components(self, plane):
		try:
			return self.__planes__.get(plane).components()			
		except:
			raise BaseException("Unable to get components from plane %s" % plane)

	def bypass_node(self):
		return None			

	def cook(self, force=False, frame_range=(), software=False):
		if any(node.cooked is False for node in self.inputs()):
			self.log("Cooking inputs: %s" % [inp.name() for inp in self.inputs()])
			for node in self.inputs():
				node.cook(software=software)

		if self.cooked != True:
			try:
				if software:
					self.log("SW computing started.")
					self.compute_sw()
					self.log("SW computing done.")
				else:
					self.log("CL computing started.")
					self.compute()
					self.log("CL computing done.")
			except:
				raise
			else:	 
				self.cooked = True
				self.log("Cooked.")
				return True
		else:
			self.log("Already cooked." )
			return True	

	def getCookedPlanes(self):
		bypass_node = self.bypass_node()
		if bypass_node:

			self.log("Getting bypass planes from node %s" % bypass_node.path())
			self.width = bypass_node.width
			self.height = bypass_node.height
			return bypass_node.getCookedPlanes()

		self.cooked = False
		if self.cooked == False:
			self.cook(software=True)

		return self.__planes__	

	def getOutDevBuffer(self):
		bypass_node = self.bypass_node()
		if bypass_node:

			self.log("Getting bypass cl buffer from node %s" % bypass_node.path())

			out_buffer = bypass_node.getOutDevBuffer()
			self.width = bypass_node.width
			self.height = bypass_node.height
			return out_buffer

		self.cooked = False
		if self.cooked == False:
			self.cook()
		
		return self.devOutBuffer

	def getOutHostBuffer(self):
		device_buffer = self.getOutDevBuffer()
		#print "Device buffer is %s of size %s" % (device_buffer, device_buffer.size)
		host_buffer = numpy.empty((self.width, self.height, 4), dtype = numpy.float16)
		self.engine.queue.finish()
		#print "Building quantized buffer for node %s with size %s" % (self, self.size)
		quantized_buffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.HALF_FLOAT), shape=self.size)	
		#print "Quantized buffer is %s of size %s" % (quantized_buffer, quantized_buffer.size)
		#print "Executing quantize program for node %s" % self.name()
		
		with cl.CommandQueue(self.engine.ctx) as queue:
			evt = self.common_program.quantize_show(queue, self.size, None, device_buffer, quantized_buffer )
			evt.wait()

		with cl.CommandQueue(self.engine.ctx) as queue:	
			evt = cl.enqueue_copy(queue, host_buffer, quantized_buffer, origin=(0,0), region=self.size)
			evt.wait()
		
		return host_buffer

