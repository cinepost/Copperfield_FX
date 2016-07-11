from copper.op.op_network import OP_Network
import copper.parameter as parameter

from copper.parm_template import *

class ROP_Node(OP_Network):
	'''
		Base output operator class
	'''
	__base__ = True 
	
	def __init__(self, engine, parent):
		super(ROP_Node, self).__init__(engine, parent)

	def parmTemplates(self):
		templates = super(ROP_Node, self).parmTemplates()
		templates += [
			ButtonParmTemplate(name="execute", label="Render", callback=self.render),
			MenuParmTemplate(name="trange", label="Valid Frame Range", menu_items=('off', 'normal', 'on'), menu_labels=('Render Current Frame', 'Render Frame Range', 'Render Frame Range Only (Strict)')),
			IntParmTemplate(name="f", label="Start/End/Inc", length=3, default_value=(1,240,1), naming_scheme=ParmNamingScheme.Base1)
		]
		return templates

	def render(self, frame_range=None):
		if frame_range:
			f1 = frame_range[0]
			f2 = frame_range[1]
			f3 = frame_range[2]
		else:
			f1 = self.parm("f1").evalAsInt()
			f2 = self.parm("f2").evalAsInt()
			f3 = self.parm("f3").evalAsInt()
		
		for frame in range(f1, f2, f3):
			self.renderFrame(frame)
