import matplotlib.image
from PIL import Image 
import pyopencl as cl
import numpy as np
import os
import logging 

from copper.core.op.node_type import NodeTypeBase
from copper.core.op.node_type_category import Cop2NodeTypeCategory
from copper.core.op.op_data_socket import OP_DataSocket
from copper.core.data.image_data import ImageData
from copper.cop.cop_node import CopNode

from copper.core.parameter.parm_template import *

logger = logging.getLogger(__name__)

class COP2_Render(CopNode):
	
	class NodeType(NodeTypeBase):
		icon_name = 'COP2_render'
		type_name = 'render'
		category = Cop2NodeTypeCategory

	def __init__(self, engine, parent):
		super(COP2_Render, self).__init__(engine, parent)
		self._output_sockets = (
			OP_DataSocket(self, "output1", ImageData),
		)

		from copper.renderers import Workbench
		self.renderer = Workbench()

	def parmTemplates(self):
		templates = super(COP2_Render, self).parmTemplates()
		templates += [
			MenuParmTemplate(name='overridesize', label='File Size', menu_items=('natural', 'project', 'size'), menu_labels=('Natural Resolution',
 				'Project Resolution', 'Specific Resolution'), default_value=0),
			IntParmTemplate(name="size", label="Size", length=2, default_value=(1280,720), naming_scheme=ParmNamingScheme.Base1),
			
		]
		
		return templates

	@classmethod
	def label(cls):
		return "Render"

	def xRes(self):
		if self.overridesize:
			return self.parm("size1").eval()

		self.cook()
		return self.image_width

	def yRes(self):
		if self.overridesize:
			return self.parm("size2").eval()

		self.cook()
		return self.image_height

	def imageBounds(self):
		return (0, 0, self.xRes(), self.yRes())

	@property
	def overridesize(self):
		if self.parm("overridesize").evalAsString() != "natural":
			return True

		return False

	def compute(self, lock, cl_context, cl_queue):
		super(COP2_Render, self).compute()
		
		self.image_width = self.parm("size1").eval()
		self.image_height = self.parm("size2").eval()

		print("render init")
		self.renderer.init(self.image_width, self.image_height, 16)

		print("rendering")
		image_array = np.flip(self.renderer.renderFrame(), (0, 1))
		print("rendering done")
		try:
			print("dev buffer")
			self.devOutBuffer = cl.Image(cl_context, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, self.image_format, 
				shape=(self.image_width, self.image_height), hostbuf=image_array.astype("float32"))

		except:
			raise