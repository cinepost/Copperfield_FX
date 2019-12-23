from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import logging
import numpy as np
from copper import hou
import math

import moderngl

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

        # connect panel signals
        self.panel.signals.copperNodeModified[str].connect(self.updateNodeDisplay)

        logger.debug("SceneViewWidget created")

    def minimumSizeHint(self):
        return QtCore.QSize(200, 200)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def drawSceneObjects(self):
        #glPolygonMode(GL_BACK, GL_LINE)

        #glTranslatef(0.0, 0.0, 0.0)

        for node in hou.node("/obj").children():
            ogl_obj_cache = SceneViewWidget.OGL_Scene_Manager.getObjNodeGeometry(node)

            if ogl_obj_cache:
                logger.debug("Drawing node: %s" % node.path())

                transform = node.worldTransform()
                #glPushMatrix()
                #glMultMatrixf(transform.m)

                # draw points
                if self.panel._show_points:
                    #glColor4f(0.0, 0.0, 1.0, 1.0)
                    if ogl_obj_cache.pointsCount() > 0:
                        logger.debug("Drawing points for: %s" % node.path())
                        glPointSize( 3.0 )
                        glBindBuffer (GL_ARRAY_BUFFER, ogl_obj_cache.pointsVBO())

                        glEnableClientState(GL_VERTEX_ARRAY)

                        glVertexPointer (3, GL_FLOAT, 0, None)
                        glDrawArrays (GL_POINTS, 0, ogl_obj_cache.pointsCount())

                        glDisableClientState(GL_VERTEX_ARRAY)

                        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0) # reset

                # draw polygons
                #glUseProgram(SceneViewWidget.OGL_Scene_Manager.defaultShaderProgram())
                if len(node.displayNode().geometry()._points) > 0: #ogl_obj_cache.polyCount() > 0:
                    logger.debug("Drawing geometry for: %s" % node.path())
                    #vao = self.ctx.simple_vertex_array(SceneViewWidget.OGL_Scene_Manager.m.program,  vbo, 'in_vert', 'in_color')
                    vao = self.ctx.simple_vertex_array(SceneViewWidget.OGL_Scene_Manager.m.program, ogl_obj_cache.pointsVBO(), "in_vert")
                    vao.render(moderngl.LINE_STRIP)
                    """
                    glEnable(GL_LIGHTING)

                    glBindBuffer (GL_ARRAY_BUFFER, ogl_obj_cache.pointsVBO())
                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ogl_obj_cache.polyIndicesVBO())

                    glEnableClientState(GL_VERTEX_ARRAY)

                    glVertexPointer (3, GL_FLOAT, 0, None)
                    glDrawElements(GL_TRIANGLES, ogl_obj_cache.polyCount()*3, GL_UNSIGNED_INT, None)

                    glDisableClientState(GL_VERTEX_ARRAY)

                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
                    glBindBuffer (GL_ARRAY_BUFFER, 0)

                    glDisable(GL_LIGHTING)
                    """
                #glPopMatrix()
                glUseProgram(0)

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

        mvp = m_proj *m_view
        self.grid.mvp.write(mvp.astype('f4').tobytes())
        self.grid.draw()

        self.origin.mvp.write(mvp.astype('f4').tobytes())
        self.origin.draw()

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


