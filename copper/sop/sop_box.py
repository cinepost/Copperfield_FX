from copper.sop import SOP_Node
from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import SopNodeTypeCategory
from copper.op.op_connection import OP_Connection
from copper import parameter

from copper.parm_template import *
from copper.geometry import Geometry, Polygon
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
			FloatParmTemplate(name="divrate", label="Axis Divisions", length=3, default_value=(4, 4, 4), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.Base1),
			ToggleParmTemplate(name="dodivs", label="Use Divisions", default_value=False),
			FloatParmTemplate(name="divs", label="Divisions", length=3, default_value=(3, 3, 3), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
		]
		
		return templates

	@classmethod
	def label(cls):
		return "Box"


	@timeit
	def cookMySop(self, lock, context):
		with lock:
			scale = self.parm("scale").evalAsFloat()

			sizex = scale * self.parm("sizex").eval()
			sizey = scale * self.parm("sizey").eval()
			sizez = scale * self.parm("sizez").eval()

			tx = self.parm("tx").evalAsInt() - sizex / 2.0
			ty = self.parm("ty").evalAsInt() - sizey / 2.0
			tz = self.parm("tz").evalAsInt() - sizez / 2.0

			dodivs = self.parm("dodivs").eval()

			self._geometry._points = []
			self._geometry._prims = []

			if dodivs:
				# Create divided box
				divsx = self.parm("divsx").evalAsInt()
				divsy = self.parm("divsy").evalAsInt()
				divsz = self.parm("divsz").evalAsInt()

				step_x = sizex / (divsx - 1)
				step_y = sizey / (divsy - 1)
				step_z = sizez / (divsz - 1)

				for x in range(divsx):
					for y in range(divsy):
						for z in range(divsz):
							self._geometry._points.append([tx + x*step_x, ty + y*step_y, tz + z*step_z])

			else:
				# create generic hollow box
				divsx = self.parm("divrate1").evalAsInt()
				divsy = self.parm("divrate2").evalAsInt()
				divsz = self.parm("divrate3").evalAsInt()

				step_x = sizex / (divsx - 1)
				step_y = sizey / (divsy - 1)
				step_z = sizez / (divsz - 1)

				tx1 = tx; ty1 = ty; tz1 = tz;
				tx2 = tx + sizex; ty2 = ty + sizey; tz2 = tz + sizez;

				# z axis points
				for x in range(divsx):
					for y in range(divsy):
						self._geometry._points.append([tx1 + x*step_x, ty1 + y*step_y, tz1])

				for x in range(divsx):
					for y in range(divsy):
						self._geometry._points.append([tx2 - x*step_x, ty2 - y*step_y, tz2])


				# create z axis polygons
				for x in range(divsx - 1):
					for y in range(divsy - 1):
						poly = Polygon(self)
						poly._vertices = [x + y*divsx, x + y*divsx+1, x + (y+1)*divsx+1, x + (y+1)*divsx]
						poly.setIsClosed()
						self._geometry._prims.append(poly)

				offset = divsx * divsy # this is the points offset between thow XY planes of box
				for x in range(divsx - 1):
					for y in range(divsy - 1):
						poly = Polygon(self)
						poly._vertices = [x + (y+1)*divsx + offset, x + (y+1)*divsx+1 + offset, x + y*divsx+1 + offset, x + y*divsx + offset]
						poly.setIsClosed()
						self._geometry._prims.append(poly)

				# y axis points 
				for z in range(1, divsz -1):
					for x in range(divsx):
						self._geometry._points.append([tx1 + x*step_x, ty1, tz1 + z*step_z])

				for z in range(1, divsz -1):
					for x in range(divsx):
						self._geometry._points.append([tx2 - x*step_x, ty2, tz2 - z*step_z])

				# x axis points 
				for z in range(1, divsz-1):
					for y in range(1, divsy-1):
						self._geometry._points.append([tx1, ty1 + y*step_y, tz1 + z*step_z])

				for z in range(1, divsz-1):
					for y in range(1, divsy-1):
						self._geometry._points.append([tx2, ty2 - y*step_y, tz2 - z*step_z])







