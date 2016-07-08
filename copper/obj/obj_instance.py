from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import ObjectNodeTypeCategory
from obj_node import OBJ_Node

class OBJ_Instance(OBJ_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'OBJ_instance'
		type_name = 'instance'
		category = ObjectNodeTypeCategory

	def __init__(self, engine, parent):
		super(OBJ_Instance, self).__init__(engine, parent)

	@classmethod
	def label(cls):
		return "Instance"
