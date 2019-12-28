import os
import logging
import freetype

from copper.sop import SOP_Node
from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import SopNodeTypeCategory
from copper.op.op_connection import OP_Connection
from copper import parameter

from copper.parm_template import *
from copper.geometry import Geometry, Polygon
from copper.utils.decorators import timeit

logger = logging.getLogger(__name__)


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
			StringParmTemplate(name="file", label="Font", default_value=("$COPPER_HOME/media/fonts/Vera.ttf",), string_type=StringParmType.FileReference),
			StringParmTemplate(name="text", label="Text", default_value=("test",))
		]
		
		return templates

	@classmethod
	def label(cls):
		return "Font"


	@timeit
	def cookMySop(self, lock, context):
		with lock:
			self._geometry.clear()

			font_file = self.parm("file").evalAsString()
			text = self.parm("text").evalAsString()

			logger.debug("Generating font geometry for text %s" % text)

			if not os.path.isfile(font_file):
				logger.error("Font file %s does not exist !" % font_file)
				return

			face = freetype.Face(font_file)
			face.set_char_size(width=0, height=0, hres=72, vres=72)

			glyphs = {}

			#g = face.load_glyph(1)
			for char in text:
				#glyph = freetype.Glyph(char)
				c = face.load_char(char)
				logger.debug("char: %s" % c)
				#g = face.load_glyph(0)
				#outline = face.glyph.outline
				#logger.debug("char %s tags: %s" %(char, outline.tags))





