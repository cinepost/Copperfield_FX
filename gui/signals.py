from PyQt4 import QtCore

class Signals(QtCore.QObject):
	copperNodeSelected = QtCore.pyqtSignal(str, name='copperNodeSelected')
	copperSetCompositeViewNode = QtCore.pyqtSignal(str, name='copperSetCompositeViewNode')
	copperNodeCreated = QtCore.pyqtSignal(str, name='copperNodeCreated')
	copperNodeModified = QtCore.pyqtSignal(str, name='copperNodeModified')

	def __init__(self, parent=None):  
		QtCore.QObject.__init__(self, parent)


signals = Signals()