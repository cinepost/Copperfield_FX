from PyQt4 import QtGui, QtCore

class ParamsWidget(QtGui.QWidget):
  
    def __init__(self, parent=None):      
        super(ParamsWidget, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setMinimumWidth(320)

        layout = QtGui.QVBoxLayout()
        self.label = QtGui.QLabel('Parameters')
        layout.addWidget(self.label)
        self.setLayout(layout)      