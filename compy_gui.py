import sys, os
from PyQt4 import QtGui, QtCore, QtOpenGL

import copper
from gui.dialogs import RenderNodeDialog

from gui.widgets import TabbedPanelWidget
from gui.widgets import TimeLineWidget
from gui.widgets import ParametersEditorWidget
from gui.widgets import NodeFlowEditorWidget
from gui.widgets import NodeTreeEditorWidget
from gui.widgets import CompositeViewerWidget
from gui.widgets import PythonShellWidget

from gui.widgets.copper_widget import CopperWidget

os.environ['PYOPENCL_COMPILER_OUTPUT'] = "1"

class Workarea(QtGui.QWidget, CopperWidget):
    def __init__(self, parent=None, engine=None):
        QtGui.QWidget.__init__(self, parent)
        CopperWidget.__init__(self)
        self.engine = engine
        self.engine.set_network_change_callback(self.rebuild_widgets)
        self.setObjectName("Workarea")

        # Init out engine and widgets first
        self.parmetersEditor    = ParametersEditorWidget(self, engine = self.engine)
        self.imageViewer        = CompositeViewerWidget(self, engine = self.engine)
        self.nodeTree           = NodeTreeEditorWidget(self, engine = self.engine, viewer = self.imageViewer, params = self.parmetersEditor)
        self.nodeFlow           = NodeFlowEditorWidget(self, engine = self.engine)
        self.timeLine           = TimeLineWidget(self)
        #self.python_view = PythonWidget(self, engine = self.engine)

        # Now init our UI 
        self.initUI()
        
    def initUI(self): 

        # Create layout and place widgets
        VBox = QtGui.QVBoxLayout()    
        VBox.setContentsMargins(0, 0, 0, 0)
        HBox = QtGui.QHBoxLayout()
        HBox.setContentsMargins(0, 0, 0, 0)
        VBox.addLayout(HBox)
        VBox.addWidget(self.timeLine)

        panel1 = TabbedPanelWidget(engine=self.engine)
        panel1.setAllowedPanelTypes([ParametersEditorWidget, CompositeViewerWidget, NodeTreeEditorWidget, NodeFlowEditorWidget])
        panel1.addPaneTab(self.imageViewer)

        panel2 = TabbedPanelWidget(engine=self.engine)
        panel2.setAllowedPanelTypes([ParametersEditorWidget, CompositeViewerWidget, NodeTreeEditorWidget, NodeFlowEditorWidget])
        panel2.addPaneTab(self.parmetersEditor)

        panel3 = TabbedPanelWidget(engine=self.engine)
        panel3.setAllowedPanelTypes([ParametersEditorWidget, CompositeViewerWidget, NodeTreeEditorWidget, NodeFlowEditorWidget])
        panel3.addPaneTab(self.nodeFlow)
        panel3.addPaneTab(self.nodeTree)
        #tabs.addTab(self.python_view, "Interactive shell")

        VSplitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        VSplitter.setMinimumWidth(370)
        VSplitter.addWidget(panel2)
        VSplitter.addWidget(panel3)

        HSplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        HSplitter.addWidget(panel1)
        HSplitter.addWidget(VSplitter)
        HSplitter.setStretchFactor (0, 1)
        HSplitter.setStretchFactor (1, 0)   

        HBox.addWidget(HSplitter)
        self.setLayout(VBox)
        self.show()
       
    def rebuild_widgets(self):
        print "Network change callback called by engine..."
        self.tree_view.emit(QtCore.SIGNAL('network_changed'))

    @QtCore.pyqtSlot()   
    def renderNode(self, node_path):
        RenderNodeDialog.render(self.engine, node_path)        

class Window(QtGui.QMainWindow):
    def __init__(self, engine):
        super(Window, self).__init__()
        self.engine = engine
        if not self.engine.have_gl:
            print "OpecCL - OpenGL interoperability not supported !!! Abort."
            exit()

        self.initUI()

    def close(self):
        exit()

    def open_project(self):
        try:
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', "/Users")
        except:
            raise
        if fname:    
            self.engine.open_project(str(fname))   

    def save_project(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file', "/Users")    
        if fname:
            self.engine.save_project(fname)

    def load_style(self):
        sqq_filename="media/copper.stylesheet.qss"
        with open(sqq_filename,"r") as fh:
            self.setStyleSheet(fh.read())

    def initUI(self):
        self.setMinimumWidth(740)
        self.setMinimumHeight(540)
        self.resize(1400, 900)
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


        reloadStylAction = QtGui.QAction(QtGui.QIcon('icons/glyphicons_082_roundabout.png'), 'Reload QSS', self)
        reloadStylAction.setShortcut('Ctrl+R')
        reloadStylAction.setStatusTip('Reload style')
        reloadStylAction.triggered.connect(self.load_style)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(reloadStylAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        viewMenu = menubar.addMenu('&View')

        helpManu = menubar.addMenu('&Help')
        
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(reloadStylAction)
        toolbar.addAction(openAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)
        
        self.setWindowTitle("Copperfield")
        self.statusBar().showMessage('Ready...')
        self.show()       

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('Plastique'))

    app.setWindowIcon(QtGui.QIcon('icons/biohazard.png'))

    engine = copper.CreateEngine("GPU")
    engine.test_project()

    win = Window(engine)
    win.load_style()
    sys.exit(app.exec_())