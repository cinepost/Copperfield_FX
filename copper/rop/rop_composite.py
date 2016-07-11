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

	def renderToFile(self, node_path, filename, frame = None):
		node = self.node(node_path)
		if frame:
			render_frame = frame
		else:
			render_frame = self.frame()

		
		print "Rendering frame %s for node %s to file: %s" % (render_frame, node.path(), render_file_name)
		buff = node.getOutHostBuffer()
		image = Image.frombuffer('RGBA', node.size, buff.astype(numpy.uint8), 'raw', 'RGBA', 0, 1)			

		if "lin" in sys.platform :
			# Flip image vertically
			image = image.transpose(Image.FLIP_TOP_BOTTOM)

		image.save(render_file_name, 'JPEG', quality=100)

	def renderFrame(self, frame=None):
		if frame:
			output_node_path = self.engine.node(self.parm("coppath").evalAsString()).path()
			self.renderToFile(output_node_path, self.parm("copoutput").evalAsStringAtFrame(frame), frame=frame)
            