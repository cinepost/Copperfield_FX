class OP_Connection(object):
	def __init__(self, name, node=None):
		self._name = name
		self._node = node

	def setNode(self, node):
		self._node = node

	def node(self):
		return self._node

	def name(self):
		return self._name

	def connected(self):
		if self._node: return True
		return False