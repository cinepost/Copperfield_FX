from copper.core.op.node_type import NodeTypeBase
from copper.core.op.node_type_category import CopNetNodeTypeCategory, Cop2NodeTypeCategory
from copper.core.op.op_network import OP_Network

class COPNET_Network(OP_Network):

	class NodeType(NodeTypeBase):
		icon_name = 'cop2-network'
		type_name = 'comp'
		category = CopNetNodeTypeCategory
	
	def __init__(self, engine, parent):
		super(COPNET_Network, self).__init__(engine, parent)

	@classmethod
	def childTypeCategory(cls):
		return Cop2NodeTypeCategory

	@classmethod
	def label(cls):
		return "Image Network"
