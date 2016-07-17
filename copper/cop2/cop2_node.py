import sys, string
import Imath
from PIL import Image
import pyopencl as cl
import numpy
import logging
import threading
import logging
import copy

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

		self.devOutBuffer = None # Device output buffer. This buffer holds thre result image array

		self.image_format = cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.FLOAT)
		self.common_program = engine.load_program("common.cl")
		
		self._planes = {
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
		return (0, 0, self.xRes(), self.yRes())
		
	def shape(self):
		return (self.xRes(), self.yRes())

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

	def compute(self):
		logging.debug("Computing %s" % self.path())

	def cookData(self, lock):
		try:
			self.compute(lock, self.engine.openclContext(), self.engine.openclQueue())
		except Exception, e:
			logging.error(str(e))
			return False

		self._needs_to_cook = False
		return True

	def getCookedData(self):
		return self.getOutDevBuffer()

	def getOutDevBuffer(self):		
		return self.devOutBuffer

	def getOutHostBuffer(self):
		device_buffer = self.getOutDevBuffer()
		host_buffer = numpy.empty((self.xRes(), self.yRes(), 4), dtype = numpy.float16)
		self.engine.openclQueue().finish()
		
		quantized_buffer = cl.Image(self.engine.openclContext(), self.engine.mf.READ_WRITE, cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.HALF_FLOAT), shape=self.shape())	
		
		with self.engine.openclQueue() as queue:
			evt = self.common_program.quantize_show(queue, self.shape(), None, device_buffer, quantized_buffer )
			evt.wait()

		with self.engine.openclQueue() as queue:	
			evt = cl.enqueue_copy(queue, host_buffer, quantized_buffer, origin=(0,0), region=self.shape())
			evt.wait()

		return host_buffer

