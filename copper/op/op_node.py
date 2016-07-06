import six

from copper.op.base import RegistryMeta
from copper.op.op_parameters import OP_Parameters

@six.add_metaclass(RegistryMeta)
class OpRegistry(type):
    _registry = {}

    def __new__(meta, name, bases, clsdict):
        cls = super(OpRegistry, meta).__new__(meta, name, bases, clsdict)
        if not clsdict.pop('__base__', False):
            meta._registry[name] = cls
            if cls.type():
                meta._registry[cls.type().name()] = cls
        return cls


class NodeType(object):
	__name__ = None
	__category__ = None
	__icon_name__ = None

	def __init__(self):
		pass

	@classmethod
	def name(cls):
		return cls.__name__

	@classmethod
	def category(cls):
		return cls.__category__

	@classmethod
	def icon(clas):
		return cls.__icon_name__


@six.add_metaclass(OpRegistry)
class OP_Node(OP_Parameters):
	""" Node base class """

	__base__ = True

	def __init__(self):
		OP_Parameters.__init__(self)

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

	'''
	isNetwork returns if the node can have children.  This is true
	if the node has an operator table or has any children.
	This does NOT tell you if it is derived from OP_Network.
	'''
	@classmethod
	def isNetwork(cls):
		raise NotImplementedError


	@classmethod
	def iconName(cls):
		return 'icons/nodes/%s.svg' % cls.type().icon()

	@classmethod
	def type(cls):
		return cls.NodeType

