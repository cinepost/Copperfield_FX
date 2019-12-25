import pyopencl as cl
import numpy

from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import Cop2NodeTypeCategory
from copper.op.op_connection import OP_Connection
from copper.cop.cop_node import CopNode
from copper import parameter

from copper.parm_template import *

class COP2_PressRaster(CopNode):

	class NodeType(NodeTypeBase):
		icon_name = 'COP2_press'
		type_name = 'press_raster'
		category = Cop2NodeTypeCategory

	def __init__(self, engine, parent):
		super(COP2_PressRaster, self).__init__(engine, parent)
		self.program = engine.load_program("effects_press_raster.cl")
		self._inputs = (
			OP_Connection("input1"),
			OP_Connection("input2"),
			OP_Connection("input3"),
		)
		self._outputs = (
			OP_Connection("output1"),
		)
		

	def parmTemplates(self):
		templates = super(COP2_PressRaster, self).parmTemplates()
		templates += [
			FloatParmTemplate(name="density", label="Density", length=1, default_value=(200,), min=10.0, max=1000.0),
			IntParmTemplate(name="quality", label="Super sampling", length=1, default_value=(2,), min=1, max=10),
		]
		
		return templates

	@classmethod
	def label(cls):
		return "Press Raster"

	def xRes(self):
		return self.input(0).xRes()

	def yRes(self):
		return self.input(0).yRes()
			
	def compute(self, lock, cl_context, cl_queue):
		super(COP2_PressRaster, self).compute()	
		if self.hasInputs():
			self.devOutBuffer = cl.Image(cl_context, cl.mem_flags.READ_WRITE, self.image_format, shape=self.input(0).shape())	
			self.width = self.xRes()
			self.height = self.yRes()
			exec_evt = self.program.raster(cl_queue, (self.width, self.height), None, 
				self.input(0).getCookedData(),     
				self.devOutBuffer,
				numpy.int32(self.input(0).xRes()),
				numpy.int32(self.input(0).yRes()),
				numpy.float32(self.parm("density").eval()),
				numpy.int32(self.parm("quality").eval()),
			)
			exec_evt.wait()
		else:
			raise BaseException("No input specified !!!")
