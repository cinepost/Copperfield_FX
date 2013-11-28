from compy.op_parameters import OP_Parameters

class OP_NetworkBoxItem(object):
	""" Base class for nodes graph rendering """

	def __init__(self):
		self.x_pos = 0.0
		self.y_pos = 0.0
		self.color = (0.5, 1.0, 0.25,)
		self.icon = None

	def setPos(self, x, y):
		self.x_pos = x
		self.y_pos = y

	def getPos(self):
		return (self.x_pos, self.y_pos,)

	def getIcon(self):
		return self.icon



class OP_Node(OP_Parameters, OP_NetworkBoxItem):
	""" Base class for nodes graph rendering """

	def __init__(self):
		OP_Parameters.__init__(self)
		OP_NetworkBoxItem.__init__(self)

	def log(self, text):
		print "%s: %s" % (self.path(), text)	
