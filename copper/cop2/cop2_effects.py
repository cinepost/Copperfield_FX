import pyopencl as cl
import numpy

from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import Cop2NodeTypeCategory
from copper.cop2.cop2_node import COP2_Node
from copper import parameter

from copper.parm_template import *

class COP2_Blur(COP2_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'COP2_blur'
		type_name = 'blur'
		category = Cop2NodeTypeCategory

	def __init__(self, engine, parent):
		super(COP2_Blur, self).__init__(engine, parent)
		self.program = engine.load_program("effects_blur.cl")
		self.__inputs__ = [None]
		self.__input_names__ = ["Input 1"]

	@classmethod
	def label(cls):
		return "Blur"

	def parmTemplates(self):
		templates = super(COP2_Blur, self).parmTemplates()
		templates += [
			FloatParmTemplate(name="blursize", label="Size", length=1, default_value=(0,05)),
			FloatParmTemplate(name="blursizey", label="Y Size", length=1, default_value=(0,05)),
			ToggleParmTemplate(name="useindepy", label="Independent Y control", default_value=False)
		]
		
		return templates

	def compute(self):	
		if self.hasInputs():
			self.devTmpBuffer = cl.Image(self.engine.openclContext(), self.engine.mf.READ_WRITE, self.image_format, shape=self.input(0).shape())
			self.devOutBuffer = cl.Image(self.engine.openclContext(), self.engine.mf.READ_WRITE, self.image_format, shape=self.input(0).shape())	
			self.width = self.input(0).xRes()
			self.height = self.input(0).yRes()
			print "Blurring area: %s x %s" % (self.width, self.height)
			exec_evt = self.program.fast_blur_h(self.engine.openclQueue(), (self.width, self.height), None, 
				self.input(0).getOutDevBuffer(),     
				self.devTmpBuffer, 
				numpy.float32(self.parm("blursize").evalAsFloat()),
				numpy.int32(self.width),
				numpy.int32(self.height ),
				numpy.int32(self.parm("useindepy").evalAsInt()),
			)
			exec_evt.wait()
			
			exec_evt = self.program.fast_blur_v(self.engine.openclQueue(), (self.width, self.height), None, 
				self.devTmpBuffer,     
				self.devOutBuffer, 
				numpy.float32(self.parm("blursizey").evalAsFloat()),
				numpy.int32(self.width),
				numpy.int32(self.height ),
				numpy.int32(self.parm("useindepy").evalAsInt()),
			)
			exec_evt.wait()
			del self.devTmpBuffer
		else:
			raise BaseException("No input specified !!!")	


class COP2_PressRaster(COP2_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'COP2_press'
		type_name = 'press'
		category = Cop2NodeTypeCategory

	def __init__(self, engine, parent):
		super(COP2_PressRaster, self).__init__(engine, parent)
		self.program = engine.load_program("effects_press_raster.cl")
		self.__inputs__ = [None]
		self.__input_names__ = ["Input 1"]	

		self.addParameter("density", float, 100)
		self.addParameter("quality", int, 2)
			
	def compute(self):	
		if self.has_inputs():
			self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=self.inputs.get(0).size)	
			self.width = self.input(0).width
			self.height = self.input(0).height
			print "Raterizing area: %s x %s" %(self.input(0).width, self.input(0).height)
			exec_evt = self.program.raster(self.engine.queue, self.size, None, 
				self.input(0).getOutDevBuffer(),     
				self.devOutBuffer,
				numpy.int32(self.input(0).width),
				numpy.int32(self.input(0).height),
				numpy.float32(self.parm("density").eval()),
				numpy.int32(self.parm("quality").eval()),
			)
			exec_evt.wait()
		else:
			raise BaseException("No input specified !!!")
