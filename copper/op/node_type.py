import six
import inspect 

from copper.op.base import RegistryMeta

@six.add_metaclass(RegistryMeta)
class NodeTypeRegistry(type):
    _registry = {}

    def __new__(meta, name, bases, clsdict):
        cls = super(NodeTypeRegistry, meta).__new__(meta, name, bases, clsdict)
        if not clsdict.pop('__base__', False):
            meta._registry[name] = cls
            if 'cat_name' in clsdict:
                meta._registry[cls.cat_name] = cls
        return cls

    def __repr__(cls):
		return "<%s for %s>" % (inspect.getmro(cls)[1].__name__, cls.type_name)

@six.add_metaclass(NodeTypeRegistry)
class NodeTypeBase(object):
	__base__ = True

	type_name = None
	category = None
	icon_name = None

	def __init__(self):
		pass

	@classmethod
	def name(cls):
		return cls.type_name

	@classmethod
	def nameWithCategory(cls):
		return "%s/%s" % (cls.category.name(), cls.name())

	@classmethod
	def category(cls):
		return cls.category

	@classmethod
	def icon(cls):
		return cls.icon_name
