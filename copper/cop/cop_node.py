import sys, string
import Imath
from PIL import Image
import pyopencl as cl
import numpy
import logging
import threading
import logging
import copy

from copper.copper_string import CopperString
from copper.parameter import CopperParameter
from copper.op.op_network import OP_Network
from copper.cop.cop_plane import COP_Plane

from copper.parm_template import *

logger = logging.getLogger(__name__)

class CopNode(OP_Network):
	__base__ = True
	type_name = None # This is a TYPE name for the particular compositing OP ...
	
	def __init__(self, engine, parent):
		super(CopNode, self).__init__(engine, parent)

		self._display_flag = False
		self._render_flag = False

		self.devOutBuffer = None # Device output buffer. This buffer holds thre result image array

		self.image_format = cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.FLOAT)
		self.common_program = engine.load_program("common.cl")
		
		self._planes = {
			"C": COP_Plane(self, channel_names=['r','g','b'], dtype=float),
			"A": COP_Plane(self, dtype=float)
		}

	def parmTemplates(self):
		templates = super(CopNode, self).parmTemplates()
		templates += [
			FloatParmTemplate(name="effectamount", label="Effect Amount", length=1, default_value=(1.0,), min=0.0, max=1.0, min_is_strict=True, max_is_strict=True, naming_scheme=ParmNamingScheme.Base1)
		]
		return templates

	def xRes(self):
		'''
		Returns the x-resolution of the node's image for the current frame. Raises hou.OperationFailed if the node could not be cooked or opened for processing.
		'''
		raise NotImplementedError

	def yRes(self):
		'''
		Returns the y-resolution of the node's image for the current frame. Raises hou.OperationFailed if the node could not be cooked or opened for processing.
		'''
		raise NotImplementedError

	def imageBounds(self, plane="C"):
		'''
		Returns the x and y boundaries of the given plane in the form of (xmin, ymin, xmax, ymax). The value of the plane argument is the plane name.
		By default, the image bounds of the color plane is returned.
		Note that the image bounds is not the same as the image resolution. For example, the image bounds for a Font COP is the bounding rectangle around the displayed letters 
		while the resolution is the size of the node's image.
		Note that the returned image bounds is for the current frame.
		Raises ValueError if plane is None or empty. Raises hou.OperationFailed if the node could not be cooked or opened for processing. 
		Raises hou.OperationFailed if the given plane does not exist.
		'''
		return (0, 0, self.xRes(), self.yRes())

	def depth(self,plane):
		'''
		Return the data format used to represent one component of one pixel in the given image plane.
		For example, if the depth of the "C" (color) plane is hou.imageDepth.Int8, each of the red, green, and blue components is stored as an (unsigned) 8-bit integer, 
		occupying one byte. If, for example, it is instead hou.imageDepth.Float32, each of the red, green, and blue components is a 32-bit float and occupies 4 bytes 
		(12 bytes total for all 3 components combined).
		'''
		return NotImplementedError

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

	def isDisplayFlagSet(self):
		'''
		Returns True if the node's display flag is turned on. Returns False otherwise.
		'''
		return self._display_flag

	def isRenderFlagSet(self):
		'''
		Turns the node's render flag on or off. The render flag controls which node in a compositing network will be rendered to /hom/hou/mplay or to disk. 
		The value of the on argument must be True or False.
		Raises hou.PermissionError if the node is unwritable.
		'''
		return self._render_flag

	def isTimeDependent(self):
		return False		

	def planes(self):
		'''
		Returns a tuple of plane names in the node's image sequence. Raises hou.OperationFailed if the node could not be cooked or opened for processing.
		'''
		return tuple(self.__planes__.keys())

	def setDisplayFlag(self, on):
		self._display_flag = on

	def setRenderFlag(self, on):
		self._render_flag = on

	def saveImage(self, file_name, frame_range=(), img_format='JPEG'):
		if type(frame_range) != tuple:
			logger.error("Expecting frame_range as tuple. Got %s" % type(frame_range))
			return 

		for frame in range(frame_range[0], frame_range[1]+1):
			file_name_expanded = CopperString(file_name).expandedString(context={'frame':frame})	
			logger.info("Rendering frame %s of node %s to file: %s" % (frame, self.path(), file_name_expanded))
			
			if self.needsToCook():
				self.cook()

			buff = self.getOutHostBuffer()
			image = Image.frombuffer('RGBA', self.shape(), buff.astype(numpy.uint8), 'raw', 'RGBA', 0, 1)			

			if img_format == 'JPEG':
				image.convert("RGB").save(file_name_expanded, 'JPEG', quality=100)
			else:
				image.save(file_name_expanded, 'PNG')

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

	def cookData(self, lock, context={}):
		try:
			self.compute(lock, self.engine.openclContext(), self.engine.openclQueue())
		except Exception as e:
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
		
		quantized_buffer = cl.Image(self.engine.openclContext(), cl.mem_flags.READ_WRITE, cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.HALF_FLOAT), shape=self.shape())	
		
		with self.engine.openclQueue() as queue:
			evt = self.common_program.quantize_show(queue, self.shape(), None, device_buffer, quantized_buffer )
			evt.wait()

		with self.engine.openclQueue() as queue:	
			evt = cl.enqueue_copy(queue, host_buffer, quantized_buffer, origin=(0,0), region=self.shape())
			evt.wait()

		return host_buffer

