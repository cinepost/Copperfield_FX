from PyQt4 import QtGui, QtCore
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT

class PythonWidget(QtGui.QTextEdit):

    def __init__(self, parent=None):
        super(PythonWidget, self).__init__()

