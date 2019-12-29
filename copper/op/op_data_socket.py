import inspect
import logging

from .op_node import OP_Node
from .op_data import OP_DataBase
from copper.copper_object import CopperObject

logger = logging.getLogger(__name__)

class OP_DataSocket(CopperObject):
    def __init__(self, node, name, data_cls):
        super(OP_DataSocket, self).__init__()
        assert isinstance(name, str), "name is not a string"
        self._name = name

        assert issubclass(node.__class__, OP_Node), "%s is not sublass of OP_Node" % node.__class__
        self._node = node

        assert inspect.isclass(data_cls), "data_cls is not a class"
        assert issubclass(data_cls, OP_DataBase), "%s is not a sublcass of OP_DataBase" % data_cls

        self._data_cls = data_cls

    def setNode(self, node):
        self._node = node

    def node(self):
        return self._node

    def name(self):
        return self._name

    def isConnected(self):
        if self._node: return True
        return False

    def canConnect(self, op_data_socket):
        if self._data_cls == op_data_socket._data_cls:
            return True

        return False
