from PyQt4 import QtGui, QtCore

class TreeNodeViewerWidget(QtGui.QTreeWidget):
  
    def __init__(self, parent=None):      
        super(TreeNodeViewerWidget, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QtGui.QVBoxLayout()
        self.label = QtGui.QLabel('Test')
        layout.addWidget(self.label)
        self.setLayout(layout)       