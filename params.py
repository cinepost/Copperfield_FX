from PyQt4 import QtGui, QtCore

class ParamsWidget(QtGui.QWidget):
  
    def __init__(self, parent=None):      
        super(ParamsWidget, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setMinimumWidth(320)

        layout = QtGui.QVBoxLayout()
        self.label = QtGui.QLabel('Test')
        layout.addWidget(self.label)
        self.setLayout(layout)

    def resizeEvent(self, event):
        # Create a square base size of 10x10 and scale it to the new size maintaining aspect ratio.
        new_size = QtCore.QSize(10, 10)
        new_size.scale(event.size(), QtCore.Qt.KeepAspectRatio)
        self.resize(new_size)        