import sys, os
import logging

from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL

from copper import hou
from .pane import Pane
from .dialogs import RenderNodeDialog
from .widgets import PlayBarWidget
from .context_manager import ContextManager

logger = logging.getLogger(__name__)

class Workarea(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setObjectName("Workarea")

        # Basic widgets
        self.timeline_widget = PlayBarWidget()

        # Create layout and place widgets
        VBox = QtWidgets.QVBoxLayout()
        VBox.setSpacing(0)
        VBox.setContentsMargins(0, 0, 0, 0)
        HBox = QtWidgets.QHBoxLayout()
        HBox.setSpacing(0)
        HBox.setContentsMargins(0, 0, 0, 0)


        # Add initial panels
        panel_mgrs = []
        panel_mgr_1 = Pane(self)
        panel_mgr_1.addNewPaneTabByType("SceneViewPanel")
        panel_mgr_1.addNewPaneTabByType("CompositeViewPanel")
        #panel_mgr_1.addNewPaneTabByType("PythonShellPanel")
        panel_mgr_1.setSizePolicy(QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        panel_mgrs += [panel_mgr_1]

        panel_mgr_2 = Pane(self)
        panel_mgr_2.addNewPaneTabByType("ParametersPanel")
        panel_mgr_2.setSizePolicy(QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        panel_mgrs += [panel_mgr_2]

        panel_mgr_3 = Pane(self)
        panel_mgr_3.addNewPaneTabByType("NetworkViewPanel")
        panel_mgr_3.addNewPaneTabByType("TreeViewPanel")
        panel_mgr_3.setSizePolicy(QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        panel_mgrs += [panel_mgr_3]        

        # Set Up inital splitters layout
        VSplitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        VSplitter.setMinimumWidth(370)
        VSplitter.addWidget(panel_mgr_2)
        VSplitter.addWidget(panel_mgr_3)

        HSplitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        HSplitter.addWidget(panel_mgr_1)
        HSplitter.addWidget(VSplitter)
        HSplitter.setStretchFactor (0, 1)
        HSplitter.setStretchFactor (1, 0)  

        VBox.addWidget(HSplitter)
        VBox.addWidget(self.timeline_widget)
        self.setLayout(VBox)

        # Connect signals
        for panel_mgr in panel_mgrs:
            panel_mgr.maximize_button.clicked.connect(self.maximizePanelManager)

        # Show workspace
        self.show()

    @QtCore.pyqtSlot()
    def maximizePanelManager(self):
        logger.debug("Maximize panel: %s" % self)

    @QtCore.pyqtSlot()   
    def renderNode(self, node_path):
        RenderNodeDialog.render(node_path)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        from copper.core.config import Config
        Config()._has_ui = True

        if not hou.OpenCL.have_gl():
            logger.warning("OpenCL - OpenGL interoperability not supported !!!")

        self.initUI()

    def close(self):
        exit()

    def open_project(self, make_test_project=False):
        if make_test_project:
            hou.hipFile.load(None) # build test project
            return

        try:
            fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', "/Users")
        except:
            raise
        if fname:    
            hou.open_project(str(fname))   

    def save_project(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', "/Users")    
        if fname:
            hou.save_project(fname)

    def load_style(self):
        sqq_filename="gui/config/copper.stylesheet.qss"
        with open(sqq_filename,"r") as fh:
            self.setStyleSheet(fh.read())

    def initUI(self):
        ContextManager.get_qt_context(self)
        self.setMinimumWidth(960)
        self.setMinimumHeight(640)
        self.resize(1600, 900)
        self.workarea = Workarea(self)
        self.setCentralWidget(self.workarea)

        exitAction = QtWidgets.QAction(QtGui.QIcon('gui/icons/main/system-log-out.svg'), 'Exit', self)
        exitAction.setObjectName("ActionExitApp")
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openAction = QtWidgets.QAction(QtGui.QIcon('gui/icons/main/document-open.svg'), 'Open project', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open project')
        openAction.triggered.connect(self.open_project)

        saveAction = QtWidgets.QAction(QtGui.QIcon('gui/icons/main/document-save.svg'), 'Save project', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save project')
        saveAction.triggered.connect(self.save_project)


        reloadStylAction = QtWidgets.QAction(QtGui.QIcon('gui/icons/main/view-refresh.svg'), 'Reload QSS', self)
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