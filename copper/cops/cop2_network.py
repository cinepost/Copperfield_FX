from copper.op_manager import OP_Manager

class COP2_Network(OP_Manager):
	__mgr__ 	= True # Indicates that this is a network manager node
	__network_label__ = 'Composite'
	type_name = 'img'

	def __init__(self, engine, parent):
		super(COP2_Network, self).__init__(engine, parent)
