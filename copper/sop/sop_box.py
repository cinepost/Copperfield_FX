from copper.sop import SOP_Node
from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import SopNodeTypeCategory
from copper.op.op_connection import OP_Connection
from copper import parameter

from copper.parm_template import *
from copper.geometry import Geometry
from copper.utils.decorators import timeit

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
			ToggleParmTemplate(name="dodivs", label="Use Divisions", default_value=False),
			FloatParmTemplate(name="divs", label="Divisions", length=3, default_value=(3, 3, 3), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.Base1),
		]
		
		return templates

	@classmethod
	def label(cls):
		return "Box"

	@timeit
	def cookMySop(self, lock):
		with lock:
			scale = self.parm("scale").evalAsFloat()

			sizex = scale * self.parm("size1").eval()
			sizey = scale * self.parm("size2").eval()
			sizez = scale * self.parm("size3").eval()

			tx = self.parm("t1").evalAsInt() - sizex / 2.0
			ty = self.parm("t2").evalAsInt() - sizey / 2.0
			tz = self.parm("t3").evalAsInt() - sizez / 2.0

			dodivs = self.parm("dodivs").eval()

			divsx = self.parm("divs1").evalAsInt()
			divsy = self.parm("divs2").evalAsInt()
			divsz = self.parm("divs3").evalAsInt()

			step_x = sizex / (divsx - 1)
			step_y = sizey / (divsy - 1)
			step_z = sizez / (divsz - 1)

			self._geometry._points = []

			if dodivs:
				# Create divided box

				for x in range(divsx):
					for y in range(divsy):
						for z in range(divsz):
							#self._geometry.createPoint()#.setPosition([tx + x*step_x, ty + y*step_y, tz + z*step_z])
							self._geometry._points.append([tx + x*step_x, ty + y*step_y, tz + z*step_z])

			else:
				# create generic hollow box
				tx1 = tx; ty1 = ty; tz1 = tz;
				tx2 = tx + sizex; ty2 = ty + sizey; tz2 = tz + sizez;

				# x axis points
				for y in range(divsy):
					for z in range(divsz):
						self._geometry._points.append([tx1, ty1 + y*step_y, tz1 + z*step_z])
						self._geometry._points.append([tx2, ty2 - y*step_y, tz2 - z*step_z])

				# y axis points 
				for z in range(divsz):
					for x in range(1, divsx-1):
						self._geometry._points.append([tx1 + x*step_x, ty1, tz1 + z*step_z])
						self._geometry._points.append([tx2 - x*step_x, ty2, tz2 - z*step_z])

				# z axis points 
				for x in range(1, divsx-1):
					for y in range(1, divsy-1):
						self._geometry._points.append([tx1 + x*step_x, ty1 + y*step_y, tz1])
						self._geometry._points.append([tx2 - x*step_x, ty2 - y*step_y, tz2])





