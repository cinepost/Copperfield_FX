from copper.op_manager import OP_Manager

class ROP_Network(OP_Manager):
	__mgr__ = True # Indicates that this is a network manager node
	__network_label__ = 'Geometry'
	type_name = 'rop'
	#icon_name = 'icons/nodes/obj-node.svg'

	def __init__(self, engine, parent):
		super(ROP_Network, self).__init__(engine, parent, mask=None)
