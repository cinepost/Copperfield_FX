import six
import logging 

from .base import OpRegistry
from .op_parameters import OP_Parameters
from .op_input import OP_Input 

@six.add_metaclass(OpRegistry)
class OP_Node(OP_Parameters):
	""" Node base class """

	__base__ = True

	def __init__(self):
		OP_Parameters.__init__(self)
		self._needs_to_cook = True
		self._bypass = False

		self._inputs = []

		self.pos_x = None
		self.pos_y = None
		self.width = 120
		self.height = 32
		self.color = (0.4, 0.4, 0.4, 1.0,)

	def cook(self, force=False, frame_range=()):
		# first cook all input nodes if needed
		if any(node.needsToCook() for node in self.inputs()):
			logging.debug("Cooking inputs: %s" % [inp.path() for inp in self.inputs()])
			for node in self.inputs():
				node.cook()

		# cook node itself if needed
		if self.needsToCook() and not self.isBypassed():
			self.cookData()

	def cookData(self):
		raise NotImplementedError

	def setPos(self, x, y):
		self.pos_x = x
		self.pos_y = y

	def getPos(self):
		return (self.pos_x, self.pos_y,)

	def moveToGoodPosition(self):
		'''Moves node in a good place among it's siblings. Used to arrange nodes in a network for the first time. Or just auto place node.'''
		raise NotImplementedError

	@classmethod
	def isNetwork(cls):
		'''
		isNetwork returns if the node can have children.  This is true
		if the node has an operator table or has any children.
		This does NOT tell you if it is derived from OP_Network.
		'''
		raise NotImplementedError

	@classmethod
	def isManager(cls):
		raise NotImplementedError

	@classmethod
	def iconName(cls):
		return 'icons/nodes/%s.svg' % cls.type().icon()

	def hasInputs(self):
		if len(self._inputs) > 0:
			return True
		else:
			return False

	def inputs(self):
		return tuple(inp.getNode() for inp in self._inputs)

	def input(self, input_index):
		try:
			inp = self._inputs[input_index]
		except:
			raise BaseException("Wrong input index %s specified for node %s !!!") % (input_index, self)

		return inp.getNode()			

	def inputNames(self):
		""" Returns dict of input names eg: ["Input 1", "Input 2"] """
		return tuple([inp.name() for inp in self._inputs])

	def inputConnections(self):
		return []

	def inputConnectors(self):
		return []

	def outputNames(self):
		return []

	def outputConnections(self):
		return []

	def outputConnectors(self):
		return []

	def setInput(self, input_index, node):
		try:
			inp = self._inputs[input_index]					
		except:
			raise

		inp.setNode(node)

	@classmethod
	def type(cls):
		return cls.NodeType

	def isBypassed(self):
		return self._bypass

	def bypass(self, on_off):
		self._bypass = on_off

	def setModified(self, on_off):
		''' 
		Call this method to instruct node it needs to recook itself next time needed. For example when parameter was changes
		'''
		self._needs_to_cook = on_off 

	def needsToCook(self):
		return self._needs_to_cook

