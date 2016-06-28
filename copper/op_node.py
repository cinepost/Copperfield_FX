from copper.op_parameters import OP_Parameters

class OP_NetworkBoxItem(object):
	""" Base class for nodes graph rendering """
	icon_name = None

	def __init__(self):
		self.pos_x = None
		self.pos_y = None
		self.width = 120
		self.height = 32
		self.color = (0.4, 0.4, 0.4, 1.0,)

	def setPos(self, x, y):
		self.pos_x = x
		self.pos_y = y

	def getPos(self):
		return (self.pos_x, self.pos_y,)

	@classmethod
	def getIcon(cls):
		return cls.icon



class OP_Node(OP_Parameters, OP_NetworkBoxItem):
	""" Base class for nodes graph rendering """

	def __init__(self):
		OP_Parameters.__init__(self)
		OP_NetworkBoxItem.__init__(self)

	def log(self, text):
		print "%s at frame %s: %s" % (self.path(), self.engine.frame(), text)	
