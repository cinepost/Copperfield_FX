from copper.op.op_network import OP_Network
from copper.op.node_type_category import SopNodeTypeCategory

from copper.parm_template import *
from copper.vmath import Matrix4

class ObjNode(OP_Network):
	__base__ = True
	
	def __init__(self, engine, parent):
		super(ObjNode, self).__init__(engine, parent)
		self._render_node = None
		self._display_node = None

	def parmTemplates(self):
		templates = super(ObjNode, self).parmTemplates()
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
		x_ord = self.parm('xOrd').evalAsString()
		r_ord = self.parm('rOrd').evalAsString()

		tx = self.parm('tx').evalAsFloat()
		ty = self.parm('ty').evalAsFloat()
		tz = self.parm('tz').evalAsFloat()

		Mt = Matrix4.translation(tx, ty, tz)

		rx = self.parm('rx').evalAsFloat()
		ry = self.parm('ry').evalAsFloat()
		rz = self.parm('rz').evalAsFloat()

		if r_ord == 'xzy':
			rx, ry, rz = rx, rz, ry
		elif r_ord == 'yxz':
			rx, ry, rz = ry, rx, rz
		elif r_ord == 'yzx':
			rx, ry, rz = ry, rz, rx
		elif r_ord == 'zxy':
			rx, ry, rz = rz, rx, ry
		elif r_ord == 'zyx':
			rx, ry, rz = rz, ry, rx

		Mr = Matrix4.eulerToMatrixDegrees(rx, ry, rz)

		u_scale = self.parm('scale').evalAsFloat()
		sx = self.parm('sx').evalAsFloat()
		sy = self.parm('sy').evalAsFloat()
		sz = self.parm('sz').evalAsFloat()

		Ms = Matrix4.scale(sx, sy, sz)

		t_mat = Ms * Mr * Mt

		if x_ord == 'str':
			t_mat = Ms * Mt * Mr
		elif x_ord == 'rst':
			t_mat = Mr * Ms * Mt
		elif x_ord == 'rts':
			t_mat = Mr * Mt * Ms
		elif x_ord == 'tsr':
			t_mat = Mt * Ms * Mr
		elif x_ord == 'trs':
			t_mat = Mt * Mr * Ms

		return t_mat