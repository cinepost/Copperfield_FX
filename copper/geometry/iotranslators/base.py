import six

class RegistryMeta(type):
    def __getitem__(meta, key):
        return meta._registry[key]


@six.add_metaclass(RegistryMeta)
class GeoIORegistry(type):
	_registry = {}
	_registry_by_ext = {}
	_registry_by_mime = {}

	def __new__(meta, name, bases, clsdict):
		cls = super(GeoIORegistry, meta).__new__(meta, name, bases, clsdict)
		if not clsdict.pop('__base__', False):
			meta._registry[name] = cls
			for mime_type in cls.registerMIMETypes():
				meta._registry_by_mime[mime_type[0]] = cls
				if mime_type[1]:
					meta._registry_by_ext[mime_type[1]] = cls # this is used to find a proper translator by filename extension

		return cls

	@classmethod
	def getIOTranslatorByMIME(cls, mime_type):
		return cls._registry_by_mime[mime_type]

	@classmethod
	def getIOTranslatorByExt(cls, ext):
		return cls._registry_by_ext[ext]


@six.add_metaclass(GeoIORegistry)
class GeoBaseIO(object):

	__base__ = True

	@staticmethod 
	def readGeometry(geometry, filename):
		raise NotImplementedError

	@staticmethod
	def saveGeometry(geometry, filename):
		raise NotImplementedError

	@classmethod
	def registerMIMETypes(cls):
		raise NotImplementedError