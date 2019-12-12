import logging

from copper.op.op_network import OP_Network
from copper.parm_template import *

from copper.geometry import Geometry

class SOPCookException(Exception):
    pass

class SOP_Node(OP_Network):
	__base__ = True
	
	def __init__(self, engine, parent):
		super(SOP_Node, self).__init__(engine, parent)
		self._geometry = Geometry()


	def cookMySop(self, lock, context):
		raise NotImplementedError


	def cookData(self, lock, context={}):
		try:
			self.cookMySop(lock. context)
		except Exception as e:
			logging.exception("Error cooking SOP data !!!")
			return False

		self._needs_to_cook = False
		return True


	def geometry(self):
		self.cook()
		return self._geometry
