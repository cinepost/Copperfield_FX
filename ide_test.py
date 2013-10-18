import sys
from PyQt4 import QtGui, QtCore, QtOpenGL

from compy.engines import CLC_Engine

from timeline import TimelineWidget
from params import ParamsWidget
from nodeviewer import NodeViewerWidget

class Workarea(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Workarea, self).__init__(parent)
        
        # Init out engine and widgets first
        self.node_view = NodeViewerWidget(self)
        self.parm_view = ParamsWidget(self)
        self.time_view = TimelineWidget(self)

        # Now init our UI 
        self.initUI()
        
    def initUI(self):      
        hbox = QtGui.QHBoxLayout(self)

        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(self.node_view)
        splitter1.addWidget(self.parm_view)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.time_view)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        self.show()
        
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize() 

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.engine = CLC_Engine("GPU")
        self.initUI()
    
    def open(self):
        print "Open scene..."

    def initUI(self):      
        self.workarea = Workarea(self)
        self.setCentralWidget(self.workarea)

        exitAction = QtGui.QAction(QtGui.QIcon('icons/glyphicons_388_exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openAction = QtGui.QAction(QtGui.QIcon('icons/glyphicons_358_file_import.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file')
        openAction.triggered.connect(self.open)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        viewMenu = menubar.addMenu('&View')

        helpManu = menubar.addMenu('&Help')
        
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(openAction)
        toolbar.addAction(exitAction)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Compy Job Assembler')
        self.statusBar().showMessage('Ready...')
        self.show()       

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())