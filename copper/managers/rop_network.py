from copper.core.op.node_type import NodeTypeBase
from copper.core.op.node_type_category import ManagerNodeTypeCategory, DriverNodeTypeCategory
from .mgr_node import MGR_Node

class ROP_Network(MGR_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'rop-network'
		type_name = 'out'
		category = ManagerNodeTypeCategory

	def __init__(self, engine, parent):
		super(ROP_Network, self).__init__(engine, parent)

	@classmethod
	def childTypeCategory(cls):
		return DriverNodeTypeCategory

	@classmethod
	def label(cls):
		return "Output"