from PyQt4 import QtGui, QtCore

class CopperWidget(object):
    def __init__(self):      
        self.connect(self, QtCore.SIGNAL("signalCopperNodeSelected( PyQt_PyObject )"), self.copperNodeSelected)

    @QtCore.pyqtSlot(str)   
    def copperNodeSelected(self, node_path):
    	print "Emitting signalCopperNodeSelected signal from %s to %s" % (self.__class__.__name__, self.parent().__class__.__name__)

        self.parent().emit( QtCore.SIGNAL( "signalCopperNodeSelected( PyQt_PyObject )" ), node_path )
        print "%s node path changed to %s" %  (self.__class__.__name__, node_path)