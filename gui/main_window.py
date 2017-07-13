#!/usr/local/bin/python

import sys, os
import logging
logging.basicConfig(level=logging.DEBUG)

from PyQt4 import QtGui, QtCore, QtOpenGL

from copper.engine import engine
from .tabbed_panel_manager import TabbedPanelManager
from .dialogs import RenderNodeDialog
from .widgets import PlayBarWidget

class Workarea(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setObjectName("Workarea")

        # Basic widgets
        self.timeline_widget = PlayBarWidget()

        # Create layout and place widgets
        VBox = QtGui.QVBoxLayout()    
        VBox.setSpacing(0)
        VBox.setContentsMargins(0, 0, 0, 0)
        HBox = QtGui.QHBoxLayout()
        HBox.setSpacing(0)
        HBox.setContentsMargins(0, 0, 0, 0)
    

        # Add initial panels
        panelMgr1 = TabbedPanelManager(self)
        panelMgr1.addNewPaneTabByType("SceneViewPanel")
        panelMgr1.addNewPaneTabByType("CompositeViewPanel")
        panelMgr1.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding))

        panelMgr2 = TabbedPanelManager(self)
        panelMgr2.addNewPaneTabByType("ParametersPanel")
        panelMgr2.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))

        panelMgr3 = TabbedPanelManager(self)
        panelMgr3.addNewPaneTabByType("NetworkViewPanel")
        panelMgr3.addNewPaneTabByType("TreeViewPanel")
        #panelMgr3.addNewPaneTabByType("PythonShellPanel")
        panelMgr3.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))

        # Set Up inital splitters layout
        VSplitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        VSplitter.setMinimumWidth(370)
        VSplitter.addWidget(panelMgr2)
        VSplitter.addWidget(panelMgr3)

        HSplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        HSplitter.addWidget(panelMgr1)
        HSplitter.addWidget(VSplitter)
        HSplitter.setStretchFactor (0, 1)
        HSplitter.setStretchFactor (1, 0)  

        VBox.addWidget(HSplitter)
        VBox.addWidget(self.timeline_widget)
        self.setLayout(VBox)

        # Connect signals
        self.connect(panelMgr1.maximize_button, QtCore.SIGNAL("clicked()"), self.maximizePanelManager)
        self.connect(panelMgr2.maximize_button, QtCore.SIGNAL("clicked()"), self.maximizePanelManager)
        self.connect(panelMgr3.maximize_button, QtCore.SIGNAL("clicked()"), self.maximizePanelManager)

        # Show workspace
        self.show()

    @QtCore.pyqtSlot()
    def maximizePanelManager(self):
        print "Maximize panel: "

    @QtCore.pyqtSlot()   
    def renderNode(self, node_path):
        RenderNodeDialog.render(node_path)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        if not engine.have_gl:
            print "OpenCL - OpenGL interoperability not supported !!! Abort."
            exit()

        self.initUI()

    def close(self):
        exit()

    def open_project(self, make_test_project=False):
        if make_test_project:
            engine.test_project()
            return

        try:
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', "/Users")
        except:
            raise
        if fname:    
            engine.open_project(str(fname))   

    def save_project(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file', "/Users")    
        if fname:
            engine.save_project(fname)

    def load_style(self):
        sqq_filename="gui/config/copper.stylesheet.qss"
        with open(sqq_filename,"r") as fh:
            self.setStyleSheet(fh.read())

    def initUI(self):
        self.setMinimumWidth(740)
        self.setMinimumHeight(540)
        self.resize(1400, 900)
        self.workarea = Workarea(self)
        self.setCentralWidget(self.workarea)

        exitAction = QtGui.QAction(QtGui.QIcon('gui/icons/main/system-log-out.svg'), 'Exit', self)
        exitAction.setObjectName("ActionExitApp")
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openAction = QtGui.QAction(QtGui.QIcon('gui/icons/main/document-open.svg'), 'Open project', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open project')
        openAction.triggered.connect(self.open_project)

        saveAction = QtGui.QAction(QtGui.QIcon('gui/icons/main/document-save.svg'), 'Save project', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save project')
        saveAction.triggered.connect(self.save_project)


        reloadStylAction = QtGui.QAction(QtGui.QIcon('gui/icons/main/view-refresh.svg'), 'Reload QSS', self)
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