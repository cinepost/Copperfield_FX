from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import ManagerNodeTypeCategory, CopNetNodeTypeCategory
from .mgr_node import MGR_Node

class COP_Network(MGR_Node):
	
	class NodeType(NodeTypeBase):
		icon_name = 'cop2-network'
		type_name = 'img'
		category = ManagerNodeTypeCategory

	def __init__(self, engine, parent):
		super(COP_Network, self).__init__(engine, parent)

	@classmethod
	def childTypeCategory(cls):
		return CopNetNodeTypeCategory

	@classmethod
	def label(cls):
		return "Composite"