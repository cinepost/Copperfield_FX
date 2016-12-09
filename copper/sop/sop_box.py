from copper.sop import SOP_Node
from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import SopNodeTypeCategory
from copper.op.op_connection import OP_Connection
from copper import parameter

from copper.parm_template import *
from .geometry import Geometry

class SOP_Box(SOP_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'SOP_Box'
		type_name = 'box'
		category = SopNodeTypeCategory

	def __init__(self, engine, parent):
		super(SOP_Box, self).__init__(engine, parent)
		self._inputs = (
			OP_Connection("input1"),
		)
		self._outputs = (
			OP_Connection("output1"),
		)
		
	def parmTemplates(self):
		templates = super(SOP_Node, self).parmTemplates()
		templates += [
			FloatParmTemplate(name="size", label="Size", length=3, default_value=(1, 1, 1), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="t", label="Center", length=3, default_value=(0, 0, 0), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="scale", label="Uniform Scale", length=1, default_value=(1.0,), min=0.0, max=10.0),
			FloatParmTemplate(name="divrate", label="Divrate", length=3, default_value=(3, 3, 3), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.Base1),
		]
		
		return templates

	@classmethod
	def label(cls):
		return "Box"


	def compute(self, lock):
		with lock:
			scale = self.parm("scale").evalAsFloat()

			sizex = scale * self.parm("size1").eval()
			sizey = scale * self.parm("size2").eval()
			sizez = scale * self.parm("size3").eval()

			tx = self.parm("t1").evalAsInt() - sizex / 2.0
			ty = self.parm("t2").evalAsInt() - sizey / 2.0
			tz = self.parm("t3").evalAsInt() - sizez / 2.0

			divratex = self.parm("divrate1").evalAsInt()
			divratey = self.parm("divrate2").evalAsInt()
			divratez = self.parm("divrate3").evalAsInt()

			step_x = sizex / (divratex - 1)
			step_y = sizey / (divratey - 1)
			step_z = sizez / (divratez - 1)

			self._geometry._points = []
			for x in range(divratex):
				for y in range(divratey):
					for z in range(divratez):
						#self._geometry._points.append(Point(tx + x*step_x, ty + y*step_y , tz + z*step_z))
						self._geometry.createPoint().setPosition([tx + x*step_x, ty + y*step_y, tz + z*step_z])







