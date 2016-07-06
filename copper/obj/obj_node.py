from copper.op_manager import OP_Manager

class OBJ_Node(OP_Manager):
	__base__ = True
	
	def __init__(self, engine, parent):
		super(OBJ_Node, self).__init__(engine, parent, mask=None)

	@classmethod
	def renderNode(cls):
		raise NotImplementedError
