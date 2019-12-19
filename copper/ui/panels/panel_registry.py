import six
import inspect 
import logging

from PyQt5 import QtCore


logger = logging.getLogger(__name__)

class PanelRegistryMeta(type):
    def __getitem__(meta, key):
        if key in meta._registry.keys():
            return meta._registry[key]

        logger.error("Error getting panel class \"%s\" from panel registry!!!" % key)
        return None

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