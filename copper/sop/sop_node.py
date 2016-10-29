from copper.op.op_network import OP_Network
from copper.parm_template import *

from .geometry import Copper_Geometry

class SOP_Node(OP_Network):
	__base__ = True
	
	def __init__(self, engine, parent):
		super(SOP_Node, self).__init__(engine, parent)
		self._geometry = Copper_Geometry()

	def cookData(self, lock):
		return self._geometry
