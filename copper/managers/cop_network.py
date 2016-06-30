from copper.op_manager import OP_Manager

class COP_Network(OP_Manager):
	icon_name = 'icons/nodes/cop2-network.svg'
	
	def __init__(self, engine, parent):
		super(COP_Network, self).__init__(engine, parent, mask=None)

	@classmethod
	def isNetwork(cls):
		return True

	@classmethod
	def type(cls):
		return "copnet"

	@classmethod
	def isOp(cls):
		return True

	@classmethod
	def label(cls):
		return "Composite"