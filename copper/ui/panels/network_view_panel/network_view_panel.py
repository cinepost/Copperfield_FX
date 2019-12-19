import logging

from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import numpy
import copper
import math

from copper import hou as engine
from copper.op.base import OpRegistry

from copper.ui.signals import signals
from copper.ui.widgets import PathBarWidget, CollapsableWidget
from copper.ui.panels.base_panel import PathBasedPaneTab

from .network_view_widget import NetworkViewWidget 

logger = logging.getLogger(__name__)

class NetworkViewControls(CollapsableWidget):
    def __init__(self, parent=None):
        CollapsableWidget.__init__(self, parent)

        self.snap_to_grid_btn = QtWidgets.QPushButton()
        self.snap_to_grid_btn.setCheckable(True)
        self.snap_to_grid_btn.setIcon(QtGui.QIcon('gui/icons/main/network_view/snap_to_grid.svg'))
        self.snap_to_grid_btn.setStatusTip('Show/hide grid and enable/disable snapping')

        self.addWidget(self.snap_to_grid_btn)
        self.addStretch(1)

class NetworkViewPanel(PathBasedPaneTab):
    def __init__(self):  
        PathBasedPaneTab.__init__(self) 

        self.network_view_controls = NetworkViewControls(self)
        self.network_view_widget = NetworkViewWidget(self)

        self.addWidget(self.network_view_controls)
        self.addWidget(self.network_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Network View"
