from copper.op.op_network import OP_Network
from copper.op.node_type_category import SopNodeTypeCategory

from copper.parm_template import *
from copper.vmath import Matrix4

class OBJ_Node(OP_Network):
	__base__ = True
	
	def __init__(self, engine, parent):
		super(OBJ_Node, self).__init__(engine, parent)
		self._render_node = None
		self._display_node = None

	def parmTemplates(self):
		templates = super(OBJ_Node, self).parmTemplates()
		templates += [
			MenuParmTemplate(name='xOrd', label='Transform Order', 
				menu_items=('srt', 'str', 'rst', 'rts', 'tsr', 'trs'), 
				menu_labels=('Scale Rot Trans', 'Scale Trans Rot', 'Rot Scale Trans', 'Rot Trans Scale', 'Trans Scale Rot', 'Trans Rot Scale'), default_value=0),
			MenuParmTemplate(name='rOrd', label='Rotate Order', 
				menu_items=('xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'), 
				menu_labels=('Rx Ry Rz', 'Rx Rz Ry', 'Ry Rx Rz', 'Ry Rz Rx', 'Rz Rx Ry', 'Rz Ry Rx'), default_value=0),
			FloatParmTemplate(name="t", label="Translate", length=3, default_value=(0.0, 0.0, 0.0), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="r", label="Rotate", length=3, default_value=(0.0, 0.0, 0.0), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="s", label="Scale", length=3, default_value=(1.0, 1.0, 1.0), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="p", label="Pivot", length=3, default_value=(0.0, 0.0, 0.0), min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.XYZW),
			FloatParmTemplate(name="scale", label="Uniform Scale", length=1, default_value=(1.0,), min=0.0, max=1.0, min_is_strict=False, max_is_strict=False, naming_scheme=ParmNamingScheme.Base1),
		]
		return templates


	def renderNode(self):
		if self.children():
			return self.children()[0]
		else:
			return self._render_node


	def displayNode(self):
		if self.children():
			return self.children()[0]
		else:
			return self._display_node

	@classmethod
	def childTypeCategory(cls):
		return SopNodeTypeCategory


	def worldTransform(self):
		M = Matrix4(1)
		return M