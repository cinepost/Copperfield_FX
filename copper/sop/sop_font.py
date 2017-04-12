from copper.sop import SOP_Node
from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import SopNodeTypeCategory
from copper.op.op_connection import OP_Connection
from copper import parameter

from copper.parm_template import *
from copper.geometry import Geometry, Polygon
from copper.utils.decorators import timeit

import freetype

class SOP_Font(SOP_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'SOP_Font'
		type_name = 'font'
		category = SopNodeTypeCategory

	def __init__(self, engine, parent):
		super(SOP_Font, self).__init__(engine, parent)
		self._inputs = (
			OP_Connection("input1"),
		)
		self._outputs = (
			OP_Connection("output1"),
		)
		
	def parmTemplates(self):
		templates = super(SOP_Node, self).parmTemplates()
		templates += [
			StringParmTemplate(name="file", label="Font", default_value=("media/fonts/Vera.ttf",), string_type=StringParmType.FileReference),
			StringParmTemplate(name="text", label="Text", default_value=("test",))
		]
		
		return templates

	@classmethod
	def label(cls):
		return "Font"


	@timeit
	def cookMySop(self, lock):
		with lock:
			font_file = self.parm("file").evalAsString()
			text = self.parm("text").evalAsString()

			face = freetype.Face(font_file)

			self._geometry._points = []
			self._geometry._prims = []

			self._geometry._points.append([0, 0, 0])

			for char in text:
				face.load_char(char)
				outline = face.glyph.outline





