import six

class RegistryMeta(type):
    def __getitem__(meta, key):
        return meta._registry[key]


@six.add_metaclass(RegistryMeta)
class OpRegistry(type):
	_registry = {}
	_registry_by_type = {}

	def __new__(meta, name, bases, clsdict):
		cls = super(OpRegistry, meta).__new__(meta, name, bases, clsdict)
		if not clsdict.pop('__base__', False):
			meta._registry[name] = cls
			meta._registry[cls.type().nameWithCategory()] = cls # this is used to find a proper node by it's type name like "file", "blur" and so in cojunction with category
			
			# this is used to list all allowable node sub types, ex: for Obj node allowed childs is Sop
			if cls.type().category.typeName() in meta._registry_by_type:
				meta._registry_by_type[cls.type().category.typeName()][cls.type().name()] = cls
			else:
				meta._registry_by_type[cls.type().category.typeName()] = {cls.type().name(): cls}

		return cls