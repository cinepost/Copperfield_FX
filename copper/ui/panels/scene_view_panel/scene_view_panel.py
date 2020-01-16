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

from .layouts import viewport_layouts

logger = logging.getLogger(__name__)


class DisplayOptionsWidget(CollapsableWidget):
    def __init__(self, parent=None):
        CollapsableWidget.__init__(self, parent)

        self.toggle_points_btn = QtWidgets.QToolButton(self)
        self.toggle_points_btn.setCheckable(True)
        self.toggle_points_btn.setObjectName("pinable")
        self.toggle_points_btn.setIcon(QtGui.QIcon('gui/icons/main/scene_view/points.svg'))
        self.toggle_points_btn.setToolTip('Show/hide geometry points')

        self.toggle_normals_btn = QtWidgets.QToolButton(self)
        self.toggle_normals_btn.setCheckable(True)
        self.toggle_normals_btn.setObjectName("pinable")
        self.toggle_normals_btn.setIcon(QtGui.QIcon('gui/icons/main/scene_view/normals.svg'))
        self.toggle_normals_btn.setToolTip('Show/hide geometry normals')

        self.toggle_hud_btn = QtWidgets.QToolButton(self)
        self.toggle_hud_btn.setCheckable(True)
        self.toggle_hud_btn.setObjectName("pinable")
        self.toggle_hud_btn.setIcon(QtGui.QIcon('gui/icons/main/scene_view/hud.svg'))
        self.toggle_hud_btn.setToolTip('Show/hide HUD')

        self.addWidget(self.toggle_points_btn)
        self.addWidget(self.toggle_normals_btn)
        self.addWidget(self.toggle_hud_btn)
        self.addStretch(1)

from .scene_manager import OGL_Scene_Manager


class SceneViewPanel(PathBasedPaneTab):
    def __init__(self):  
        super(SceneViewPanel, self).__init__()

        self._show_points = False
        self.display_options = DisplayOptionsWidget(self)

        self.views_layout = None

        self.views_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        self.views_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.addWidget(self.display_options)
        self.addLayout(self.views_layout)
        

        # layout switching button
        self.layouts_button = QtWidgets.QPushButton(self)
        self.layouts_button.setToolTip('Switch layout')

        mapper = QtCore.QSignalMapper(self)
        layouts_menu = QtWidgets.QMenu()

        for layout_name in viewport_layouts:
            layout = viewport_layouts[layout_name]
            action = QtWidgets.QAction(QtGui.QIcon(layout['icon']), layout['title'], self)
            mapper.setMapping(action, layout_name)

            shortcut = layout.get('shortcut')
            if shortcut:
                action.setShortcut(shortcut)
            
            action.triggered.connect(mapper.map)
            layouts_menu.addAction(action)

        mapper.mapped['QString'].connect(self.makeViewsLayout)
        self.layouts_button.setMenu(layouts_menu)
        self.path_bar_widget.layout.addWidget(self.layouts_button)

        # create default viewports
        self._viewports = {
            "persp" : GeometryViewport(None, panel=self, view_type=GeometryViewport.viewType.PERSP),
            "top"   : GeometryViewport(None, panel=self, view_type=GeometryViewport.viewType.TOP),
            "bottom": GeometryViewport(None, panel=self, view_type=GeometryViewport.viewType.BOTTOM),
            "left"  : GeometryViewport(None, panel=self, view_type=GeometryViewport.viewType.LEFT),
            "right" : GeometryViewport(None, panel=self, view_type=GeometryViewport.viewType.RIGHT),
        }

        # create default views layout
        self.makeViewsLayout(layout_name="single_view")

    @classmethod
    def panelTypeName(cls):
        return "Scene View"

    def viewports(self):
        return tuple([viewports for viewport in self._viewports.values()])

    @QtCore.pyqtSlot(str)
    def makeViewsLayout(self, layout_name="single_view"):
        # clear existing views layout
        for viewport_widget in self._viewports.values():
            viewport_widget.setParent(None)

        clearLayout(self.views_layout, delete_widgets=False)

        layout_scheme = viewport_layouts[layout_name]
        self.layouts_button.setIcon(QtGui.QIcon(layout_scheme['icon']))
        

        if layout_name=="single_view":
            self.views_layout.addWidget(self._viewports["persp"])

        if layout_name=="four_views":
            HSplitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
            HSplitter1.setObjectName("tiny")
            HSplitter1.addWidget(self._viewports["top"])
            HSplitter1.addWidget(self._viewports["persp"])
            
            HSplitter2 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
            HSplitter2.setObjectName("tiny")
            HSplitter2.addWidget(self._viewports["left"])
            HSplitter2.addWidget(self._viewports["bottom"])
            
            VSplitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
            VSplitter.setObjectName("tiny")
            VSplitter.addWidget(HSplitter1)
            VSplitter.addWidget(HSplitter2)
            
            self.views_layout.addWidget(VSplitter)

    @QtCore.pyqtSlot()
    def toggleShowPoints(self):
        self._show_points = not self._show_points
        for view in self.views_layout.children():
            view.repaint()

    @QtCore.pyqtSlot()
    def toggleShowNormals(self):
        self._show_points = not self._show_points
        for view in self.views_layout.children():
            view.repaint()

    @QtCore.pyqtSlot()
    def toggleShowHUD(self):
        self._show_points = not self._show_points
        for view in self.views_layout.children():
            view.repaint()