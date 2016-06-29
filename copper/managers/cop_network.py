from copper.op_manager import OP_Manager

class COP_Network(OP_Manager):
	__mgr__ = True # Indicates that this is a network manager node
	__network_label__ = 'Images'
	type_name = 'copnet'
	#icon_name = 'icons/nodes/obj-node.svg'

	def __init__(self, engine, parent):
		super(COP_Network, self).__init__(engine, parent, mask=None)
