from copper.op_manager import OP_Manager

class COP2_Network(OP_Manager):
	icon_name = 'icons/nodes/cop2-network.svg'
	
	def __init__(self, engine, parent):
		super(COP2_Network, self).__init__(engine, parent)

	@classmethod
	def isNetwork(cls):
		return True

	@classmethod
	def isOp(cls):
		return True

	@classmethod
	def type(cls):
		return "img"

	@classmethod
	def label(cls):
		return "Image Network"
