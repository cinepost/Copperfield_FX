from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import logging
import numpy as np
from copper import hou
import math

import moderngl

from copper.obj import ObjNode
from copper.ui.utils import clearLayout
from copper.ui.signals import signals
from copper.ui.widgets import PathBarWidget, CollapsableWidget
from copper.ui.panels.base_panel import PathBasedPaneTab

from copper.vmath import Matrix4, Vector3
from .camera import Camera
from .ogl_objcache import OGL_Scene_Manager
from .drawable import *

from .layouts import viewport_layout_types

logger = logging.getLogger(__name__)


from pyrr import Matrix44


from .qmodernglwidget import QModernGLWidget

class GeometryViewport(QModernGLWidget):

    OGL_Scene_Manager = OGL_Scene_Manager()
    
    def __init__(self, parent, panel=None, share_widget=None):
        super(GeometryViewport, self).__init__(parent)

        self.pt_font = QtGui.QFont("verdana", 8)
        self.panel = panel
        self.setMinimumSize(160, 160)
        self.orbit_mode = False
        self.old_mouse_x = self.old_mouse_y = 0
        self.cameras = {
            'persp': Camera(),
        }

        self.current_camera = 'persp'

        self.m_identity = Matrix44.identity() # just a helper

        # connect panel signals
        self.panel.signals.copperNodeModified[str].connect(self.updateNodeDisplay)

        logger.debug("SceneViewWidget created")

    def minimumSizeHint(self):
        return QtCore.QSize(200, 200)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def drawSceneObjects(self, m_view, m_proj):
        for node in hou.node("/obj").children():
            ogl_obj_cache = GeometryViewport.OGL_Scene_Manager.getObjNodeGeometry(node)

            if ogl_obj_cache:
                logger.debug("Drawing node: %s" % node.path())

                transform = node.worldTransform()

                # draw points
                if self.panel._show_points:
                    pass

                # draw polygons
                if len(node.displayNode().geometry().pointsRaw()) > 0:
                    logger.debug("Drawing geometry for: %s" % node.path())
                    ogl_obj_cache.model.write(self.m_identity.astype('f4').tobytes())
                    ogl_obj_cache.view.write(m_view.astype('f4').tobytes())
                    ogl_obj_cache.projection.write(m_proj.astype('f4').tobytes())
                    ogl_obj_cache.draw()

    @QtCore.pyqtSlot(str)
    def updateNodeDisplay(self, node_path=None):
        # Now using quick and dirty hack to check that only geometry nodes changes reflected in scene view
        if str(node_path).startswith("/obj"):
            self.update()

    def init(self):
        GeometryViewport.OGL_Scene_Manager.setCtx(self.ctx)
        GeometryViewport.OGL_Scene_Manager.buildShaderPrograms() # build shader programs for OGL_Scene_Manager

        # background
        self.background = SimpleBackground(self)

        # grid
        self.grid = SimpleGrid(self)

        # origin
        self.origin = SimpleOrigin(self)


    def render(self):
        m_view = self.activeCamera.getTransform()
        m_proj = self.activeCamera.getProjection()
        self.screen.use()

        self.ctx.clear(1.0, 1.0, 1.0)
        self.background.draw()

        # TODO: we might also want to pass model matrix so we can get different grid orientations instead of rebuilding grid
        self.grid.view.write(m_view.astype('f4').tobytes())
        self.grid.projection.write(m_proj.astype('f4').tobytes())
        self.grid.draw()

        self.origin.model.write(self.m_identity.astype('f4').tobytes())
        self.origin.view.write(m_view.astype('f4').tobytes())
        self.origin.projection.write(m_proj.astype('f4').tobytes())
        self.origin.draw()

        # geometry
        self.drawSceneObjects(m_view, m_proj)

    def draw(self):
        self.render()


    def resize(self, width, height):
        self.activeCamera.setViewportDimensions(width, height)
        self.ctx.viewport = (0, 0, width, height)

    def initializeGL(self):
        pass

    @property
    def activeCamera(self):
        return self.cameras[self.current_camera]


    def mousePressEvent(self, mouseEvent):
        self.orbit_mode = True
        self.old_mouse_x = mouseEvent.x()
        self.old_mouse_y = mouseEvent.y()
        self.setCursor(QtCore.Qt.ClosedHandCursor)


    def mouseReleaseEvent(self, mouseEvent):
        self.orbit_mode = False
        self.setCursor(QtCore.Qt.OpenHandCursor)


    def mouseMoveEvent(self, mouseEvent):
        if int(mouseEvent.buttons()) != QtCore.Qt.NoButton :
            # user is orbiting camera
            delta_x = mouseEvent.x() - self.old_mouse_x
            delta_y = self.old_mouse_y - mouseEvent.y()
            
            if int(mouseEvent.buttons()) & QtCore.Qt.LeftButton :
                if mouseEvent.modifiers() == QtCore.Qt.AltModifier :
                    # pan camera
                    self.activeCamera.pan( delta_x, delta_y )
                else:
                    # orbit camera
                    self.activeCamera.orbit(delta_x, delta_y)
            elif int(mouseEvent.buttons()) & QtCore.Qt.RightButton :
                # dolly camera
                self.activeCamera.dolly( 3*(delta_x + delta_y), False )
            elif int(mouseEvent.buttons()) & QtCore.Qt.MidButton :
                # pan camera
                self.activeCamera.pan( delta_x, delta_y )
            
        self.update()
        
        self.old_mouse_x = mouseEvent.x()
        self.old_mouse_y = mouseEvent.y()


    # hou module stuff
    def camera(self) -> ObjNode or None:
        '''
        If the viewport is currently looking through a camera or light (not necessarily locked to it), this returns an object representing the camera/light’s node. 
        Returns None if the viewport is not looking through a camera/light.
        '''
        return None