import sys, os
from PyQt4 import QtGui, QtCore, QtOpenGL

import compy

from widgets import TimelineWidget
from widgets import ParamsWidget
from widgets import NodeViewerWidget
from widgets import ImageviewWidget
from widgets import TreeNodeViewerWidget
from widgets import PythonWidget

os.environ['PYOPENCL_COMPILER_OUTPUT'] = "1"

class Workarea(QtGui.QWidget):
    def __init__(self, parent=None, engine=None):
        super(Workarea, self).__init__(parent)
        self.engine = engine
        self.engine.set_network_change_callback(self.rebuild_widgets)

        # Init out engine and widgets first
        self.parm_view  = ParamsWidget(self, engine = self.engine)
        self.time_view  = TimelineWidget(self)
        self.img_view   = ImageviewWidget(self, engine = self.engine)
        self.tree_view  = TreeNodeViewerWidget(self, engine = self.engine, viewer = self.img_view, params = self.parm_view)
        self.node_view  = NodeViewerWidget(self)
        self.python_view = PythonWidget(self, engine = self.engine)

        # Now init our UI 
        self.initUI()
        
    def initUI(self): 

        # Create layout and place widgets     
        HBox = QtGui.QHBoxLayout(self)
        
        tabs = QtGui.QTabWidget()
        tabs.addTab(self.node_view, "Node view")
        tabs.addTab(self.tree_view, "Tree view")
        tabs.addTab(self.python_view, "Interactive shell")

        VSplitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        VSplitter.addWidget(self.img_view)
        VSplitter.addWidget(self.time_view)
        VSplitter.addWidget(tabs)

        HSplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        HSplitter.addWidget(VSplitter)
        HSplitter.addWidget(self.parm_view)        

        HBox.addWidget(HSplitter)
        self.setLayout(HBox)
        self.show()
       
    def rebuild_widgets(self):
        print "Network change callback called by engine..."
        self.tree_view.emit(QtCore.SIGNAL('network_changed'))    

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.engine = compy.CreateEngine("GPU")
        if not self.engine.have_gl:
            print "OpecCL - OpenGL interoperability not supported !!! Abort."
            exit()
            
        self.initUI()

    def close(self):
        exit()

    def open_project(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname:    
            self.engine.open_project(fname)   

    def save_project(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file', '/home')    
        if fname:
            self.engine.save_project(fname)

    def initUI(self):      
        self.workarea = Workarea(self, engine=self.engine)
        self.setCentralWidget(self.workarea)


        exitAction = QtGui.QAction(QtGui.QIcon('icons/glyphicons_388_exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openAction = QtGui.QAction(QtGui.QIcon('icons/glyphicons_358_file_import.png'), 'Open project', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open project')
        openAction.triggered.connect(self.open_project)

        saveAction = QtGui.QAction(QtGui.QIcon('icons/glyphicons_359_file_export.png'), 'Save project', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save project')
        saveAction.triggered.connect(self.save_project)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        viewMenu = menubar.addMenu('&View')

        helpManu = menubar.addMenu('&Help')
        
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(openAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        
        #self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle("Bare Metal Composer")
        self.statusBar().showMessage('Ready...')
        self.show()       

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icons/biohazard.png'))
    win = Window()
    sys.exit(app.exec_())