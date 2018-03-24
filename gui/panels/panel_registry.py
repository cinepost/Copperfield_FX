import six
import inspect 

from PyQt5 import QtCore

class PanelRegistryMeta(type):
    def __getitem__(meta, key):
        return meta._registry[key]


@six.add_metaclass(PanelRegistryMeta)
class PanelRegistry(type(QtCore.QObject)):
    _registry = {}

    def __new__(meta, name, bases, clsdict):
        cls = super(PanelRegistry, meta).__new__(meta, name, bases, clsdict)
        if not clsdict.pop('__base__', False):
            meta._registry[name] = cls

        return cls

    def __repr__(cls):
        return "<%s for %s>" % (inspect.getmro(cls)[1].__name__, cls.panelTypeName())