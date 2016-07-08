from copper.op.op_network import OP_Network

class OBJ_Node(OP_Network):
	__base__ = True
	
	def __init__(self, engine, parent):
		super(OBJ_Node, self).__init__(engine, parent)

	@classmethod
	def renderNode(cls):
		raise NotImplementedError
