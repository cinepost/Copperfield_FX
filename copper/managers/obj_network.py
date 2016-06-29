from copper.op_manager import OP_Manager

class OBJ_Network(OP_Manager):
	icon_name = 'icons/nodes/obj-network.svg'

	def __init__(self, engine, parent):
		super(OBJ_Network, self).__init__(engine, parent, mask=None)

	@classmethod
	def isNetwork(cls):
		return True

	@classmethod
	def type(cls):
		return "obj"

	@classmethod
	def isOp(cls):
		return True

	@classmethod
	def label(cls):
		return "Obj"