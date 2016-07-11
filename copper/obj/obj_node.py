from copper.op.op_network import OP_Network

from copper.parm_template import *

class OBJ_Node(OP_Network):
	__base__ = True
	
	def __init__(self, engine, parent):
		super(OBJ_Node, self).__init__(engine, parent)

	def parmTemplates(self):
		templates = super(OBJ_Node, self).parmTemplates()
		templates += [
			FloatParmTemplate(name="t", label="Translate", length=3, default_value=(0.0,0.0,0.0), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="r", label="Rotate", length=3, default_value=(0.0,0.0,0.0), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="s", label="Scale", length=3, default_value=(1.0,1.0,1.0), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="p", label="Pivot", length=3, default_value=(0.0,0.0,0.0), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="scale", label="Uniform Scale", length=1, default_value=(1.0,), min=0.0, max=1.0, min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.Base1),
		]
		return templates

	@classmethod
	def renderNode(cls):
		raise NotImplementedError
