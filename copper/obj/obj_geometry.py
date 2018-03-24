from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import ObjectNodeTypeCategory
from .obj_node import OBJ_Node

class OBJ_Geometry(OBJ_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'OBJ_geo'
		type_name = 'geo'
		category = ObjectNodeTypeCategory

	def __init__(self, engine, parent):
		super(OBJ_Geometry, self).__init__(engine, parent)

	@classmethod
	def label(cls):
		return "Geometry"
