from compy.op_manager import OP_Manager
import compy.parameter as parameter

class COP_Out(OP_Manager):
	'''
		Base output operator class
	'''
	__op__			= True # Indicated that this is OP node
	type_name		= None # This is a TYPE name for the particular output OP...

	def __init__(self, engine, parent):
		super(CLC_Out, self).__init__(engine, parent)
		self.addParameter("execute", parameter.CompyParmButton, None, label="Render", callback=self.execute)
		self.addParameter("f1", int, 0)
		self.addParameter("f2", int, 100)
		self.addParameter("f3", int, 1)

	def execute(self):
		raise BaseException("Unimplemented execute() for %s" % self)	
