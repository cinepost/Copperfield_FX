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
		#self.addParameter("execute", parameter.CopperParmButton, None, label="Render", callback=self.execute)
		#self.addParameter("f1", int, 0)
		#self.addParameter("f2", int, 100)
		#self.addParameter("f3", int, 1)

	@classmethod
	def parmTemplates(cls):
		templates = super(ROP_Node, cls).parmTemplates()
		templates += [
			ButtonParmTemplate(name="execute", label="Render"),
			IntParmTemplate(name="f", label="Start/End/Inc", length=3, default_value=(1,240,1), naming_scheme=ParmNamingScheme.Base1)
		]
		return templates

	def execute(self):
		raise NotImplementedError	
