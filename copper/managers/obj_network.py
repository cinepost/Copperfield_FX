from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import ManagerNodeTypeCategory
from copper.op.op_network import OP_Network

class OBJ_Network(OP_Network):

	class NodeType(NodeTypeBase):
		icon_name = 'obj-network'
		type_name = 'obj'
		category = ManagerNodeTypeCategory

	def __init__(self, engine, parent):
		super(OBJ_Network, self).__init__(engine, parent, mask=None)

	@classmethod
	def label(cls):
		return "Obj"