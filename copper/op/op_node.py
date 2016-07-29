import six
import multiprocessing
import logging 
import datetime
from collections import OrderedDict

from .base import OpRegistry
from .op_parameters import OP_Parameters
from .op_connection import OP_Connection
from .op_cooking_queue import OpCookingQueue

@six.add_metaclass(OpRegistry)
class OP_Node(OP_Parameters):
	""" Node base class """

	__base__ = True

	def __init__(self):
		OP_Parameters.__init__(self)
		self._creation_time = datetime.datetime.now()
		self._hidden = False
		self._needs_to_cook = True
		self._selected = False
		self._bypass = False

		self._inputs = ()
		self._outputs = ()

		self._pos_x = None
		self._pos_y = None
		self._width = 120
		self._height = 32
		self._color = (0.4, 0.4, 0.4, 1.0,)

	def color(self):
		'''
		Return the color of this node's tile in the network editor.
		'''
		return self._color

	def cook(self, force=False, frame_range=()):
		if self.needsToCook():
			queue = OpCookingQueue(self)
			queue.execute(frame_range=frame_range)

	def cookData(self):
		raise NotImplementedError

	def creationTime(self):
		'''
		Return the date and time when the node was created.
		'''
		return self._creation_time

	def destroy(self):
		'''
		Delete this node.
		'''
		raise NotImplementedError

	def errors(self):
		'''
		Return the text of any errors from the last cook of this node, or the empty string ("" ) if there were no errors.
		'''
		return self._errors

	def setPosition(self, pos):
		'''
		Sets the position of this node's tile in the network editor graph. Raises hou.InvalidInput if the node cannot have the given position.
		'''
		self._pos_x = pos[0]
		self._pos_y = pos[1]

	def position(self):
		'''
		Return the position of this node's tile in the network editor graph as a Vector2 . See also move() and setPosition() .
		'''
		return (self._pos_x, self._pos_y)

	def moveToGoodPosition(self):
		'''Moves node in a good place among it's siblings. Used to arrange nodes in a network for the first time. Or just auto place node.'''
		raise NotImplementedError

	def hide(self, on):
		'''
		Hide or show a node in the network editor. See hou.Node.isHidden for more information about hidden nodes.
		'''
		self._hidden = on

	def isHidden(self):
		'''
		Return whether the node is hidden in the network editor. Note that Houdini also uses the term "exposed" to refer to nodes that are not hidden.
		'''
		return self._hidden

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

	def isSelected(self):
		'''
		Return whether this node is selected.
		'''
		return self._selected

	@classmethod
	def iconName(cls):
		return 'icons/nodes/%s.svg' % cls.type().icon()

	def hasInputs(self):
		if len(self._inputs) > 0:
			return True

		return False

	def input(self, input_index):
		try:
			inp = self._inputs[input_index]
		except:
			raise BaseException("Wrong input index %s specified for node %s !!!") % (input_index, self)

		return inp.node()	

	def inputs(self):
		'''
		Return a tuple of the nodes connected to this node's inputs.
		'''
		return tuple([op_connection.node() for op_connection in self._inputs])

	def inputAncestors(self, include_ref_inputs=True, follow_subnets=False):
		'''
		Return a tuple of all input ancestors of this node. If include_ref_inputs is False, then reference inputs are not traversed.
		If follow_subnets is True, then instead of treating subnetwork nodes as a single node, we also traverse its children starting with its display node.
		'''
		ancestors = self.inputs()
		if ancestors:
			for ancestor in ancestors:
				ancestors += ancestor.inputAncestors(include_ref_inputs, follow_subnets)

		return ancestors

	def inputNames(self):
		""" Returns dict of input names eg: ["Input 1", "Input 2"] """
		return tuple([op_connection.name() for op_connection in self._inputs])

	def inputConnections(self):
		return []

	def inputConnectors(self):
		return []

	def isCurrent(self):
		raise NotImplementedError

	def outputs(self):
		return tuple([op_connection.node() for op_connection in self._outputs])

	def outputNames(self):
		""" Returns dict of output names eg: ["Input 1", "Input 2"] """
		return tuple([op_connection.name() for op_connection in self._outputs])

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

	def setSelected(on, clear_all_selected=False, show_asset_if_selected=False):
		'''
		Select or deselect this node, optionally deselecting all other selected nodes in this network. If show_asset_if_selected is True, 
		then the panes will show the top-level asset of the selected node instead.
		'''
		self._selected = on

	def size(self):
		'''
		Return the size of this node's tile in the network editor graph as a Vector2 .
		'''
		return (self._width, self._height)

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
		if on_off == True:
			from gui.signals import signals
			signals.copperNodeModified[str].emit(self.path())

	def needsToCook(self, time=None):
		if not time:
			cook_time = self.root().time()

		return self._needs_to_cook

	def warnings(self):
		'''
		Return the text of any warnings from the last cook of this node, or the empty string ("" ) if there were no warnings.			
		'''
		return self._warnings
