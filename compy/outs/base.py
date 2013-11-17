import compy.network_manager as network_manager
import compy.parameter as parameter

class CLC_Out(network_manager.CLC_NetworkManager):
	'''
		Base output operator class
	'''
	__op__			= True # Indicated that this is OP node
	type_name		= None # This is a TYPE name for the particular output OP...

	def __init__(self, engine, parent):
		super(CLC_Out, self).__init__(engine, parent)
		self.addParameter("execute", parameter.CompyButton, None, label="Render")
		self.addParameter("f1", int, 0)
		self.addParameter("f2", int, 100)
		self.addParameter("f3", int, 1)

