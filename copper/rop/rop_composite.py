import sys
import numpy
from PIL import Image

from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import DriverNodeTypeCategory
from copper.rop.rop_node import ROP_Node
from copper import parameter

from copper.parm_template import *

class ROP_Composite(ROP_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'ROP_comp'
		type_name = 'comp'
		category = DriverNodeTypeCategory


	def __init__(self, engine, parent):
		super(ROP_Composite, self).__init__(engine, parent)

	def parmTemplates(self):
		templates = super(ROP_Composite, self).parmTemplates()
		templates += [
			StringParmTemplate(name="coppath", label="COP Name", string_type = StringParmType.NodeReference),
			StringParmTemplate(name="copoutput", label="Output Picture", string_type = StringParmType.FileReference)
		]
		return templates

	@classmethod
	def label(cls):
		return "Composite"

	def renderFrame(self, frame=None):
		if frame:
			output_node = self.engine.node(self.parm("coppath").evalAsString())
			self._renderToFile(output_node, self.parm("copoutput").evalAsStringAtFrame(frame), frame=frame)

	def _renderToFile(self, node, filename, frame = None):
		if frame:
			render_frame = frame
		else:
			render_frame = self.frame()

		
		print "Rendering frame %s for node %s to file: %s" % (render_frame, node.path(), filename)
		buff = node.getOutHostBuffer()

		image = Image.frombuffer('RGBA', node.shape(), buff.astype(numpy.uint8), 'raw', 'RGBA', 0, 1)			

		if "lin" in sys.platform :
			# Flip image vertically
			image = image.transpose(Image.FLIP_TOP_BOTTOM)

		image.save(filename, 'JPEG', quality=100)
            