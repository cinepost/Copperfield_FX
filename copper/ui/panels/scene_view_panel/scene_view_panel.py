from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import logging
import numpy
from copper import hou
import math

import moderngl

from copper.ui.utils import clearLayout
from copper.ui.signals import signals
from copper.ui.widgets import PathBarWidget, CollapsableWidget
from copper.ui.panels.base_panel import PathBasedPaneTab

from copper.core.vmath import Matrix4, Vector3
from .geometry_viewport import GeometryViewport
from .camera import Camera

from .layouts import viewport_layout_types

logger = logging.getLogger(__name__)


class DisplayOptionsWidget(CollapsableWidget):
    def __init__(self, parent=None):
        CollapsableWidget.__init__(self, parent)

        self.toggle_points_btn = QtWidgets.QToolButton(self)
        self.toggle_points_btn.setCheckable(True)
        self.toggle_points_btn.setObjectName("show_points")
        self.toggle_points_btn.setIcon(QtGui.QIcon('gui/icons/main/scene_view/points.svg'))
        self.toggle_points_btn.setStatusTip('Show/hide geometry points')

        self.addWidget(self.toggle_points_btn)
        self.addStretch(1)

from .scene_manager import OGL_Scene_Manager

class SceneViewPanel(PathBasedPaneTab):
    def __init__(self):  
        super(SceneViewPanel, self).__init__()

        self._show_points = False
        self.display_options = DisplayOptionsWidget(self)
        self.display_options.toggle_points_btn.pressed.connect(self.toggleShowPoints)

        self.views_layout = None

        self.views_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        self.views_layout.setSpacing(2)
        self.views_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.addWidget(self.display_options)
        self.addLayout(self.views_layout)
        

        # layout switching button
        self.layouts_button = QtWidgets.QPushButton("Layouts", self)
        self.layouts_button.setIcon(QtGui.QIcon("gui/icons/main/go-next.svg"))

        mapper = QtCore.QSignalMapper(self)
        layouts_menu = QtWidgets.QMenu()

        for layout in viewport_layout_types:
            action = QtWidgets.QAction(QtGui.QIcon(layout['icon']), layout['name'], self)
            mapper.setMapping(action, layout['name'])
            action.setShortcut(layout['shortcut'])
            action.triggered.connect(mapper.map)
            layouts_menu.addAction(action)

        mapper.mapped['QString'].connect(self.makeViewsLayout)
        self.layouts_button.setMenu(layouts_menu)
        self.path_bar_widget.layout.addWidget(self.layouts_button)

        # create default viewports
        self.viewports = {
            "persp" : GeometryViewport(None, panel=self),
            "top"   : GeometryViewport(None, panel=self),
            "bottom": GeometryViewport(None, panel=self),
            "left"  : GeometryViewport(None, panel=self),
            "right" : GeometryViewport(None, panel=self)
        }

        # create default views layout
        self.makeViewsLayout(layout_name="Single View")

    @classmethod
    def panelTypeName(cls):
        return "Scene View"

    def viewports(self):
        return tuple([viewports for viewport in self.viewports.values()])

    def makeViewsLayout(self, layout_name="Single View"):
        logger.debug("LAYOUT NAME: %s" % layout_name)

        #clear views layout
        clearLayout(self.views_layout, delete_widgets=False)
        logger.debug("Layout : %s" % self.views_layout.count())

        if layout_name=="Single View":
            self.views_layout.addWidget(self.viewports["persp"])

        if layout_name=="Four Views":
            self.views_layout.addWidget(self.viewports["persp"])
            self.views_layout.addWidget(self.viewports["left"])
            self.views_layout.addWidget(self.viewports["top"])
            self.views_layout.addWidget(self.viewports["bottom"])

    @QtCore.pyqtSlot()
    def toggleShowPoints(self):
        self._show_points = not self._show_points
        for view in self.views_layout.children():
            view.repaint()
