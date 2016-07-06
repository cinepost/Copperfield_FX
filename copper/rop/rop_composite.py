from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import DriverNodeTypeCategory
from copper.rop.rop_node import ROP_Node
from copper import parameter

class ROP_Composite(ROP_Node):
	
	class NodeType(NodeTypeBase):
		icon_name = 'ROP_comp'
		type_name = 'comp'
		category = DriverNodeTypeCategory

	def __init__(self, engine, parent):
		super(ROP_Composite, self).__init__(engine, parent)
		self.addParameter("coppath", parameter.CopperParmOpPath, "", label="COP Name")
		self.addParameter("copoutput", parameter.CopperParmFile, "", label="Output Picture")

	@classmethod
	def label(cls):
		return "Composite"

	def execute(self):
		self.render()	

	def renderToFile(self, node_path, filename, frame = None):
		node = self.node(node_path)
		if frame:
			render_frame = frame
		else:
			render_frame = self.frame()

		self.setFrame(render_frame)	

		self.setFrame(frame)	
		render_file_name = CopperString(self.engine, filename).expandedString()	
		
		self.log("OpenCL. Rendering frame %s for node %s to file: %s" % (render_frame, node.path(), render_file_name))
		buff = node.getOutHostBuffer()
		image = Image.frombuffer('RGBA', node.size, buff.astype(numpy.uint8), 'raw', 'RGBA', 0, 1)			

		if "lin" in sys.platform :
			# Flip image vertically
			image = image.transpose(Image.FLIP_TOP_BOTTOM)

		image.save(render_file_name, 'JPEG', quality=100)

	def render(self, frame_range=(), res=(), output_file=None, output_format=None, to_flipbook=False):
		f1 = self.parm("f1").evalAsInt()
		f2 = self.parm("f2").evalAsInt()
		f3 = self.parm("f3").evalAsInt()
		if frame_range:
			f1 = frame_range[0]
			f2 = frame_range[1]
			if len(frame_range) > 2: f3 = frame_range[2]

		output_node = self.engine.node(self.parm("coppath").eval())

		for frame in range(f1, f2, f3):
			self.renderToFile(output_node.path(), self.parm("copoutput").eval(), frame)
            