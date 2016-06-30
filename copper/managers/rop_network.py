from copper.op_manager import OP_Manager

class ROP_Network(OP_Manager):
	icon_name = 'icons/nodes/rop-network.svg'

	def __init__(self, engine, parent):
		super(ROP_Network, self).__init__(engine, parent, mask=None)

	@classmethod
	def isNetwork(cls):
		return True

	@classmethod
	def type(cls):
		return "out"

	@classmethod
	def isOp(cls):
		return True

	@classmethod
	def label(cls):
		return "Output"