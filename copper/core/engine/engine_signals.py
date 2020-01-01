import uuid
from PyQt5 import QtCore

from copper.core.op.op_node import OP_Node

class EngineSignals(QtCore.QObject):
    cookNodeData = QtCore.pyqtSignal(uuid.UUID) # ask engine to cook node data using node uuid
    cookNodeData = QtCore.pyqtSignal(OP_Node)   # ask engine to cook node data using node path
    getNodeByPath = QtCore.pyqtSignal(str)   	# ask engine for a node by it's path string
    getNodeById = QtCore.pyqtSignal(int)   		# ask engine for a node by it's id

    nodeSelected = QtCore.pyqtSignal(OP_Node)	# fired by the engine when node selected e.g hou.cd(node_path), hou.pwd(node_or_path)
    nodeCreated  = QtCore.pyqtSignal(OP_Node)	# fired by the engine when new node created
    nodeModified = QtCore.pyqtSignal(OP_Node)	# fired by the engine when new node created

    def __init__(self):  
        QtCore.QObject.__init__(self)

signals = EngineSignals()