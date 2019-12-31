from PyQt5 import QtCore

from copper.core.op.op_node import OP_Node

class Signals(QtCore.QObject):
	copperNodeSelected = QtCore.pyqtSignal(OP_Node, name='copperNodeSelected')
	copperSetCompositeViewNode = QtCore.pyqtSignal(OP_Node, name='copperSetCompositeViewNode')
	copperNodeCreated = QtCore.pyqtSignal(OP_Node, name='copperNodeCreated')
	copperNodeModified = QtCore.pyqtSignal(OP_Node, name='copperNodeModified')
	copperParmModified = QtCore.pyqtSignal(OP_Node, name='copperParmModified')

	def __init__(self, parent=None):  
		QtCore.QObject.__init__(self, parent)


signals = Signals()