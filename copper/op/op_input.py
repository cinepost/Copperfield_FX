class OP_Input(object):
	def __init__(self, input_name, input_node=None):
		self.input_name = input_name
		self.input_node = input_node

	def setNode(self, node):
		self.input_node = node

	def getNode(self):
		return self.input_node

	def name(self):
		return self.input_name