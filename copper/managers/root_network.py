import logging

from copper.core.op.node_type import NodeTypeBase
from copper.core.op.node_type_category import ManagerNodeTypeCategory, DirectorNodeTypeCategory
from .mgr_node import MGR_Node

logger = logging.getLogger(__name__)


class ROOT_Network(MGR_Node):
	
	class NodeType(NodeTypeBase):
		icon_name = 'NETWORKS_root'
		type_name = 'root'
		category = DirectorNodeTypeCategory

	def __init__(self, engine):
		super(ROOT_Network, self).__init__(engine, None)

		self._name = "/"

		# create base network managers
		self.createNode("out", "out")
		self.createNode("img", "img")
		self.createNode("obj", "obj")	

	@classmethod
	def childTypeCategory(cls):
		return ManagerNodeTypeCategory

	@classmethod
	def label(cls):
		return "Root"