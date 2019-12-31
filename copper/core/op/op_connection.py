import inspect
import logging

from .op_data_socket import OP_DataSocket
from .op_node import OP_Node

logger = logging.getLogger(__name__)

class OP_Connection(object):
    def __init__(self, input_node_socket, output_node_socket):
        assert isinstance(input_node_socket, OP_DataSocket)
        assert isinstance(output_node_socket, OP_DataSocket)

        self._input_node_socket = input_node_socket
        self._output_node_socket = output_node_socket

    def inputNode(self) -> OP_Node:
        '''
        Return the node on the input side of this connection.
        '''
        return self._input_node_socket.node()

    def outputNode(self) -> OP_Node:
        '''
        Return the node on the output side of this connection.
        '''
        return self._output_node_socket.node()

    def inputDataSocket(self) -> OP_DataSocket:
        return self._input_node_socket

    def outputDataSocket(self) -> OP_DataSocket:
        return self._output_node_socket