from compy.rops.rop_base import ROP_Base
from compy import parameter

class ROP_Composite(ROP_Base):
	type_name = "composite"
	category = "image"

	def __init__(self, engine, parent):
		super(ROP_Composite, self).__init__(engine, parent)
		self.addParameter("coppath", parameter.CompyParmOpPath, "", label="COP Name")
		self.addParameter("copoutput", parameter.CompyParmFile, "", label="Output Picture")

	def execute(self):
		self.render()	

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
			self.engine.renderToFile(output_node.path(), self.parm("copoutput").eval(), frame)
            