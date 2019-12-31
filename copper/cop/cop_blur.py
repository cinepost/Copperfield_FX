import pyopencl as cl
import numpy

from copper.core.op.node_type import NodeTypeBase
from copper.core.op.node_type_category import Cop2NodeTypeCategory
from copper.core.op.op_data_socket import OP_DataSocket
from copper.core.data import ImageData
from copper.cop.cop_node import CopNode

from copper.core.parameter.parm_template import *

class COP2_Blur(CopNode):

	class NodeType(NodeTypeBase):
		icon_name = 'COP2_blur'
		type_name = 'blur'
		category = Cop2NodeTypeCategory

	def __init__(self, engine, parent):
		super(COP2_Blur, self).__init__(engine, parent)
		self.program = engine.load_program("effects_blur.cl")
		self._input_sockets = (
			OP_DataSocket(self, "input1", ImageData),
			OP_DataSocket(self, "input2", ImageData),
		)
		self._output_sockets = (
			OP_DataSocket(self, "output1", ImageData),
		)
		
	@classmethod
	def label(cls):
		return "Blur"

	def parmTemplates(self):
		templates = super(COP2_Blur, self).parmTemplates()
		templates += [
			FloatParmTemplate(name="blursize", label="Size", length=1, default_value=(0.05,), min=0.0, max=1.0),
			FloatParmTemplate(name="blursizey", label="Y Size", length=1, default_value=(0.05,), min=0.0, max=1.0),
			ToggleParmTemplate(name="useindepy", label="Independent Y control", default_value=False)
		]
		
		return templates

	def xRes(self):
		return self.input(0).xRes()

	def yRes(self):
		return self.input(0).yRes()

	def imageBounds(self):
		h_half_extents = int(0.5 * (self.xRes() * self.parm("blursize").evalAsFloat()))
		v_half_extents = int(0.5 * (self.yRes() * self.parm("blursizey").evalAsFloat()))
		return (0 - h_half_extents, 0 - v_half_extents, self.xRes() + h_half_extents, self.yRes() + v_half_extents) 

	def compute(self, lock, cl_context, cl_queue):
		super(COP2_Blur, self).compute()	
		if self.hasInputs():
			self.devTmpBuffer = cl.Image(cl_context, cl.mem_flags.READ_WRITE, self.image_format, shape=self.input(0).shape())
			self.devOutBuffer = cl.Image(cl_context, cl.mem_flags.READ_WRITE, self.image_format, shape=self.input(0).shape())	
			self.width = self.input(0).xRes()
			self.height = self.input(0).yRes()
			#print "Blurring area: %s x %s" % (self.width, self.height)
			exec_evt = self.program.fast_blur_h(cl_queue, (self.width, self.height), None, 
				self.input(0).getCookedData(),     
				self.devTmpBuffer, 
				numpy.float32(self.parm("blursize").evalAsFloat()),
				numpy.int32(self.width),
				numpy.int32(self.height ),
			)
			#exec_evt.wait()
			
			exec_evt = self.program.fast_blur_v(cl_queue, (self.width, self.height), None, 
				self.devTmpBuffer,     
				self.devOutBuffer, 
				numpy.float32(self.parm("blursizey").evalAsFloat()),
				numpy.int32(self.width),
				numpy.int32(self.height ),
			)
			exec_evt.wait()
			del self.devTmpBuffer
		else:
			raise BaseException("No input specified !!!")	

