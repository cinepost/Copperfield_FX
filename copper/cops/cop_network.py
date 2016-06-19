from copper.op_manager import OP_Manager

class COP_Network(OP_Manager):
	__mgr__ 	= True # Indicates that this is a network manager node
	__network_label__ = 'Composite'
	type_name 	= 'comp'

	def __init__(self, engine, parent):
		super(COP_Network, self).__init__(engine, parent)
