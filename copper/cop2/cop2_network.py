from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import CopNetNodeTypeCategory
from copper.op.op_network import OP_Network

class COP2_Network(OP_Network):

	class NodeType(NodeTypeBase):
		icon_name = 'cop2-network'
		type_name = 'img'
		category = CopNetNodeTypeCategory
	
	def __init__(self, engine, parent):
		super(COP2_Network, self).__init__(engine, parent)

	@classmethod
	def label(cls):
		return "Image Network"
