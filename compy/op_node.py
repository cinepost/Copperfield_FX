from compy.op_parameters import OP_Parameters

class OP_NetworkBoxItem(object):
	""" Base class for nodes graph rendering """

	def __init__(self):
		self.x_pos = 40.0
		self.y_pos = 40.0
		self.width = 120
		self.height = 40
		self.color = (0.4, 0.4, 0.4, 1.0,)
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
		print "%s at frame %s: %s" % (self.path(), self.engine.frame(), text)	
