class OP_DataSocket(object):
	def __init__(self, name, node=None, data_cls=None):
		self._name = name
		self._node = node
		self._data_cls = data_cls

	def setNode(self, node):
		self._node = node

	def node(self):
		return self._node

	def name(self):
		return self._name

	def connected(self):
		if self._node: return True
		return False