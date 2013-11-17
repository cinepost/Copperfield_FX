import base

class CLC_Composite(base.CLC_Out):
	type_name = "composite"
	category = "image"

	def __init__(self, engine, parent):
		super(CLC_Composite, self).__init__(engine, parent)
		self.addParameter("coppath", str, "")