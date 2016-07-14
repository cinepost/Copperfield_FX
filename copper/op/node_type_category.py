import six
import inspect 

from copper.op.base import RegistryMeta

@six.add_metaclass(RegistryMeta)
class NodeTypeCategoryRegistry(type):
    _registry = {}
    _registry_aliases = {}

    def __new__(meta, name, bases, clsdict):
        cls = super(NodeTypeCategoryRegistry, meta).__new__(meta, name, bases, clsdict)
        if not clsdict.pop('__base__', False):
            meta._registry[name] = cls
            if 'cat_name' in clsdict:
                meta._registry[cls.cat_name] = cls
                meta._registry_aliases[cls.cat_name] = cls
        return cls

    def __repr__(cls):
		return "<%s for %s>" % (inspect.getmro(cls)[1].__name__, cls.cat_name)

@six.add_metaclass(NodeTypeCategoryRegistry)
class NodeTypeCategory(object):
	__base__ = True
	
	cat_name = None
	type_name = None

	def __init__(self):
		pass

	@classmethod
	def name(cls):
		return cls.cat_name

	@classmethod
	def nodeTypes(self):
		raise NotImplementedError

	@classmethod
	def typeName(cls):
		return cls.type_name


class DirectorNodeTypeCategory(NodeTypeCategory):
	cat_name = 'Director'
	type_name = 'DIR'

class ManagerNodeTypeCategory(NodeTypeCategory):
	cat_name = 'Manager'
	type_name = 'MGR'

class DriverNodeTypeCategory(NodeTypeCategory):
	cat_name = 'Driver'
	type_name = 'ROP'

class ObjectNodeTypeCategory(NodeTypeCategory):
	cat_name = 'Object'
	type_name = 'OBJ'

class CopNetNodeTypeCategory(NodeTypeCategory):
	cat_name = 'CopNet'
	type_name = 'IMG'

class Cop2NodeTypeCategory(NodeTypeCategory):
	cat_name = 'Cop2'
	type_name = 'COP2'