from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import ManagerNodeTypeCategory, ObjectNodeTypeCategory
from .mgr_node import MGR_Node

class OBJ_Network(MGR_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'obj-network'
		type_name = 'obj'
		category = ManagerNodeTypeCategory

	def __init__(self, engine, parent):
		super(OBJ_Network, self).__init__(engine, parent)

	@classmethod
	def childTypeCategory(cls):
		return ObjectNodeTypeCategory

	@classmethod
	def label(cls):
		return "Obj"