from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import ManagerNodeTypeCategory
from copper.op.op_network import OP_Network

class MGR_Node(OP_Network):
	__base__ = True

	def __init__(self, engine, parent):
		super(MGR_Node, self).__init__(engine, parent)

	@classmethod
	def isManager(cls):
		return True

	@classmethod
	def label(cls):
		return "Composite"

	def cook(self, force=False, frame_range=()):
		pass