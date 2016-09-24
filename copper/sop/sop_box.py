from copper.sop import SOP_Node
from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import SopNodeTypeCategory
from copper.op.op_connection import OP_Connection
from copper import parameter

from copper.parm_template import *

class SOP_Box(SOP_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'SOP_Box'
		type_name = 'box'
		category = SopNodeTypeCategory

	def __init__(self, engine, parent):
		super(SOP_Box, self).__init__(engine, parent)
		self._inputs = (
			OP_Connection("input1"),
		)
		self._outputs = (
			OP_Connection("output1"),
		)
		
	def parmTemplates(self):
		templates = super(SOP_Node, self).parmTemplates()
		templates += [
			FloatParmTemplate(name="size", label="Size", length=1, default_value=(1,), min=0.0, max=100.0),
		]
		
		return templates

	@classmethod
	def label(cls):
		return "Box"