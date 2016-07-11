import sys, string
import Imath
from PIL import Image
import pyopencl as cl
import numpy
import logging
import threading

from copper.parameter import CopperParameter
from copper.op.op_network import OP_Network
from copper.cop2.cop_plane import COP_Plane

from copper.parm_template import *

class COP2_Node(OP_Network):
	__base__ = True
	type_name = None # This is a TYPE name for the particular compositing OP ...
	
	def __init__(self, engine, parent):
		super(COP2_Node, self).__init__(engine, parent)

		self.image_width	= None	
		self.image_height	= None
		self.cooked	= False	

		self.devOutBuffer = None # Device output buffer. This buffer holds thre result image array

		self.image_format = cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.FLOAT)
		self.common_program = engine.load_program("common.cl")
		
		self.__planes__ = {
			"C": COP_Plane(self, channel_names=['r','g','b'], dtype=float),
			"A": COP_Plane(self, dtype=float)
		}

	def parmTemplates(self):
		templates = super(COP2_Node, self).parmTemplates()
		templates += [
			FloatParmTemplate(name="effectamount", label="Effect Amount", length=1, default_value=(1.0,), min=0.0, max=1.0, min_is_strict=True, max_is_strict=True, naming_scheme=ParmNamingScheme.Base1)
		]
		return templates

	def xRes(self):
		raise NotImplementedError

	def yRes(self):
		raise NotImplementedError

	def imageBounds(self):
		return (self.xRes()/2, self.yRes()/2, self.xRes()/2, self.yRes()/2)
		
	@property	
	def area(self):	
		return self.xRes() * self.yRes()
		
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

	def invalidate(self):
		print "Node %s invalidated!" % self.name
		self.cooked = False

	def cook(self, force=False, frame_range=(), software=False):
		if any(node.cooked is False for node in self.inputs()):
			self.log("Cooking inputs: %s" % [inp.name() for inp in self.inputs()])
			for node in self.inputs():
				node.cook()

		if self.cooked != True:
			try:
				self.compute()
			except:
				raise
			else:	 
				self.cooked = True
				logging.debug("Cooked.")
				return True
		else:
			self.log("Already cooked." )
			return True	

	def getCookedPlanes(self):
		bypass_node = self.bypass_node()
		if bypass_node:

			self.log("Getting bypass planes from node %s" % bypass_node.path())
			self.width = bypass_node.getImageWidth()
			self.height = bypass_node.getImageHeight()
			return bypass_node.getCookedPlanes()

		self.cooked = False
		if self.cooked == False:
			self.cook(software=True)

		return self.__planes__	

	def getOutDevBuffer(self):
		bypass_node = self.bypass_node()
		if bypass_node:

			self.log("Getting bypass cl buffer from node %s" % bypass_node.path())

			self.width = bypass_node.xRes()
			self.height = bypass_node.yRes()
			return bypass_node.getOutDevBuffer()

		if self.cooked == False:
			print "Cooking node %s" % self.name()
			self.cook()
			print "Cooking node %s done." % self.name()
		
		return self.devOutBuffer

	def getOutHostBuffer(self):
		device_buffer = self.getOutDevBuffer()
		#print "Device buffer is %s of size %s" % (device_buffer, device_buffer.size)
		host_buffer = numpy.empty((self.width, self.height, 4), dtype = numpy.float16)
		self.engine.queue.finish()
		#print "Building quantized buffer for node %s with size %s" % (self, self.size)
		quantized_buffer = cl.Image(self.engine.openclContext(), self.engine.mf.READ_WRITE, cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.HALF_FLOAT), shape=self.size)	
		#print "Quantized buffer is %s of size %s" % (quantized_buffer, quantized_buffer.size)
		#print "Executing quantize program for node %s" % self.name()
		
		with cl.CommandQueue(self.engine.openclContext()) as queue:
			evt = self.common_program.quantize_show(queue, self.size, None, device_buffer, quantized_buffer )
			evt.wait()

		with cl.CommandQueue(self.engine.openclContext()) as queue:	
			evt = cl.enqueue_copy(queue, host_buffer, quantized_buffer, origin=(0,0), region=self.size)
			evt.wait()
		
		return host_buffer

