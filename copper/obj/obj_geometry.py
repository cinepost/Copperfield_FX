from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import ObjectNodeTypeCategory
from copper.op.op_network import OP_Network

class OBJ_Geometry(OP_Network):

	class NodeType(NodeTypeBase):
		icon_name = 'OBJ_geo'
		type_name = 'geo'
		category = ObjectNodeTypeCategory

	def __init__(self, engine, parent):
		super(OBJ_Geometry, self).__init__(engine, parent, mask=None)


	@classmethod
	def label(cls):
		return "Geometry"
