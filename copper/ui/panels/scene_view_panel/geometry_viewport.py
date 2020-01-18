from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import time
import logging
import numpy as np
from copper import hou
import math
from PIL import Image

import threading
import moderngl

from copper.core.op.op_node import OP_Node
from copper.obj import ObjNode
from copper.ui.utils import clearLayout
from copper.ui.signals import signals
from copper.ui.widgets import PathBarWidget, CollapsableWidget
from copper.ui.panels.base_panel import PathBasedPaneTab
from copper.renderers import Workbench

from copper.core.vmath import Matrix4, Vector3
from .camera import Camera

from .scene_manager import OGL_Scene_Manager, scene_manager
from .scene_manager.drawable import QuadFS

from pyrr import Matrix44

from .qmodernglwidget import QModernGLWidget

from moderngl_window.opengl.vao import VAO

logger = logging.getLogger(__name__)


class HUD_Info():
    def __init__(self):
        self.fps = 0

class Pixmap_Overlay(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setPixmap()
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.Qt.WA_TransparentForMouseEvents, True)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground, True) 

    def setPixmap(self, pixmap=None):
        if pixmap:
            self._pixmap = pixmap
            self.paintEvent = self._paintEvent
        else:
            self.paintEvent = self._paintEventNull

    def _paintEventNull(self, event):
        pass

    def _paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self._pixmap)
        painter.end()

class Signals(QtCore.QObject):
    request_aa_pass = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):  
        QtCore.QObject.__init__(self, parent)

from enum import IntEnum

class GeometryViewport(QModernGLWidget):

    class viewType(IntEnum):
        PERSP = 0
        TOP = 1
        BOTTOM = 2
        LEFT = 3
        RIGHT = 4
        FRONT = 5
        BACK = 6
    
    def __init__(self, parent, panel=None, view_type=0, share_widget=None, scene_manager=None):
        super(GeometryViewport, self).__init__(parent)

        # panel section
        self.panel = panel
        self.setMinimumSize(160, 160)
        self.setSizePolicy(QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        # mouse interactions
        self.orbit_mode = False
        self.old_mouse_x = self.old_mouse_y = 0

        # some viewport stuff
        self.cameras = {
            'persp': Camera(),
            'top': Camera(position=[10,0,0], is_perspective=False),
            'left': Camera(position=[0,0,10], is_perspective=False),
        }

        if view_type == GeometryViewport.viewType.PERSP:
            self.current_camera = 'persp'
        elif view_type == GeometryViewport.viewType.TOP:
            self.current_camera = 'top'
        else:
            self.current_camera = 'left'

        self._show_points = None
        self._show_normals = None
        self._show_hud = None
        self._init_done = False

        self.scene_manager = OGL_Scene_Manager()

        self._width, self._height = None, None

        # offscreen render target / offscreen HUD pixmap
        self.offscreen = None
        self.offscreen2 = None
        self.hud_pixmap = None

        # helpers
        self.m_identity = Matrix44.identity() # just a helper

        # HUD seciton
        self.hud_font = QtGui.QFont("verdana", 8)
        self.hud_info = HUD_Info()
        self.hud_overlay = Pixmap_Overlay()
        self.hud_overlay.setParent(self)
        self.hud_overlay.hide()

        # connect panel signals
        #self.panel.signals.copperNodeModified[OP_Node].connect(self.updateNodeDisplay)

        # connect panel buttons signals
        self.panel.display_options.toggle_points_btn.pressed.connect(self.toggleShowPoints)
        self.panel.display_options.toggle_normals_btn.pressed.connect(self.toggleShowNormals)
        self.panel.display_options.toggle_hud_btn.pressed.connect(self.toggleShowHUD)

        # aa signalling
        self.signals = Signals(self)

        # scene manager signals
        self.scene_manager.signals.geometryUpdated.connect(self.updateGeometryDisplay)

        logger.debug("GeometryViewport widget created")

    def minimumSizeHint(self):
        return QtCore.QSize(200, 200)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def drawSceneObjects(self, m_view, m_proj):
        for drawable in self.scene_manager.objects():
            # draw polygons
            drawable.uniformWrite("model", self.m_identity.astype('f4').tobytes())
            drawable.uniformWrite("view", m_view.astype('f4').tobytes())
            drawable.uniformWrite("projection", m_proj.astype('f4').tobytes())
            drawable.draw(show_points = self._show_points)
        
    @QtCore.pyqtSlot()
    def toggleShowPoints(self):
        self._show_points = not self._show_points
        self.update()

    @QtCore.pyqtSlot()
    def toggleShowNormals(self):
        self._show_normals = not self._show_normals
        self.update()

    @QtCore.pyqtSlot()
    def toggleShowHUD(self):
        self._show_hud = not self._show_hud
        if self._show_hud:
            self.hud_overlay.show()
        else:
            self.hud_overlay.hide()

    @QtCore.pyqtSlot()
    def updateGeometryDisplay(self):
        # Now using quick and dirty hack to check that only geometry nodes changes reflected in scene view
        self.update()

    @QtCore.pyqtSlot()
    def handleRenderedSample(self):
        self.makeCurrent()
        self.offscreen2_diffuse.write(self.renderer.image_data)
        self.update()

    @QtCore.pyqtSlot()
    def handleFinishedSamples(self):
        pass

    def init(self):
        if not self._init_done:
            self.makeCurrent()
            self.ctx.point_size = 2.0
            self.scope = None
            
            self.buildOffscreen(self.ctx.viewport[2], self.ctx.viewport[3])
            self.scene_manager.init()

            # A fullscreen quad just for rendering one pass to offscreen textures
            self.quad_fs = QuadFS(self)
            self.quad_fs.program['m_model'].write(Matrix44.identity().astype('f4').tobytes())
            self.quad_fs.program['m_view'].write(Matrix44.identity().astype('f4').tobytes())
            self.quad_fs.program['m_proj'].write(Matrix44.orthogonal_projection(-1, 1, 1, -1, 1, 10).astype('f4').tobytes())

            # init renderer
            self.renderer = Workbench()
            self.renderer.signals.sample_rendered.connect(self.handleRenderedSample)

            self.thread = QtCore.QThread()
            self.thread.start()

            self.renderer.moveToThread(self.thread)
            self.renderer.pause.connect(self.renderer.stop)
            self.renderer.start.connect(self.renderer.run)
            #self.renderer.start.emit(self.ctx.viewport[2], self.ctx.viewport[3])
            
            self._init_done = True

    def renderHUD(self, aa_pass_num):
        if aa_pass_num == 0:
            # render aa pass independent HUD info
            self.hud_pixmap.fill(QtGui.QColor(0, 0, 0, 0))
            painter = QtGui.QPainter(self.hud_pixmap)
            painter.setPen(QtGui.QColor(255, 128, 16))
            painter.setFont(self.hud_font)
            painter.drawText(10, 20, "FPS: %.1f" % self.hud_info.fps)
            painter.end()
            self.hud_overlay.update()
        else:
            # render aa pass dependent HUD info
            pass

    def resetProgressiveRender(self):
        #self.rendering_thread.join()
        self._progressive_render_started = False
        self.renderer.resetProgressiveRender()

    def render(self):
        #print("GeometryViewport render")
        
        self.makeCurrent()
        start_time = time.time()

        m_view = self.activeCamera.getTransform()
        m_proj = self.activeCamera.getProjection()

        # Render the scene to offscreen buffer
        self.offscreen.use()
        self.offscreen.clear(0.0, 0.0, 0.0, 0.0)
    

        self.ctx.multisample = True
        self.ctx.disable(moderngl.DEPTH_TEST)

        # Render guides

        self.ctx.enable(moderngl.DEPTH_TEST)
        # TODO: we might also want to pass model matrix so we can get different grid orientations instead of rebuilding grid
        self.scene_manager.grid.view.write(m_view.astype('f4').tobytes())
        self.scene_manager.grid.projection.write(m_proj.astype('f4').tobytes())
        self.scene_manager.grid.draw()

        self.scene_manager.origin.model.write(Matrix44.identity().astype('f4').tobytes())
        self.scene_manager.origin.view.write(m_view.astype('f4').tobytes())
        self.scene_manager.origin.projection.write(m_proj.astype('f4').tobytes())
        self.scene_manager.origin.draw()

        # draw guides
        self.drawSceneObjects(m_view, m_proj)

        # ---

        # Activate the window screen as the render target
        self.ctx.disable(moderngl.DEPTH_TEST)
        self.screen.clear(0.0, 1.0, 0.0, 1.0)
        self.screen.use()

        # Image from renderer        
        self.offscreen2_diffuse.use(location=0)
        self.quad_fs.render()
        

        # Render offscreen guides buffer over of screen
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_equation = moderngl.FUNC_ADD
        self.ctx.blend_func = moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA
        self.offscreen_diffuse.use(location=0)
        self.quad_fs.render()
        self.ctx.disable(moderngl.BLEND)

        self.ctx.finish()

        time_now = time.time()
        self.hud_info.fps = 1.0 / (time_now - start_time)

        # render hud surface
        self.renderHUD(0)


    def buildOffscreen(self, width, height):
        buffer_size = (width, height)
        # offscreen render target
        if self.offscreen:
            self.offscreen.release()
            self.offscreen_diffuse.release()
            self.offscreen_normals.release()
            self.offscreen_depth.release()

        self.offscreen_diffuse = self.ctx.texture(buffer_size, 4, dtype='f2') # RGBA color/diffuse layer
        self.offscreen_normals = self.ctx.texture(buffer_size, 4, dtype='f2') # Textures for storing normals (16 bit floats)
        self.offscreen_depth = self.ctx.depth_texture(buffer_size) # Texture for storing depth values

        # create a framebuffer we can render to
        self.offscreen = self.ctx.framebuffer(
            color_attachments=[
                self.offscreen_diffuse,
                self.offscreen_normals
            ],
            depth_attachment=self.offscreen_depth,
        )
        self.offscreen.viewport = (0, 0, width, height)

        if self.offscreen2:
            self.offscreen2.release()
            self.offscreen2_diffuse.release()
            self.offscreen2_depth.release()

        self.offscreen2_diffuse = self.ctx.texture(buffer_size, 4, dtype='f1') # RGBA color/diffuse layer
        self.offscreen2_depth = self.ctx.depth_texture(buffer_size) # Texture for storing depth values

        # create a framebuffer we can render to
        self.offscreen2 = self.ctx.framebuffer(
            color_attachments=[
                self.offscreen2_diffuse,
            ],
            depth_attachment=self.offscreen2_depth,
        )
        self.offscreen2.viewport = (0, 0, width, height)

        # offscreen hud pixmap
        if self.hud_pixmap:
            self.hud_pixmap = None

        if not self.hud_pixmap:
            self.hud_pixmap = QtGui.QPixmap(width, height)
            self.hud_overlay.setPixmap(self.hud_pixmap)

    def resize(self, width, height):
        self._width, self._height = width, height
        self.renderer.pause.emit()
        self.makeCurrent()
        self.activeCamera.setViewportDimensions(width, height)
        self.ctx.viewport = (0, 0, width, height)

        self.screen = self.ctx.detect_framebuffer(self.defaultFramebufferObject())

        self.buildOffscreen(width, height)
        self.hud_overlay.resize(width, height)

        self.renderer.start.emit(width, height)

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

            self.old_mouse_x = mouseEvent.x()
            self.old_mouse_y = mouseEvent.y()
            
            self.renderer._camera = self.activeCamera
            self.renderer.start.disconnect()
            self.renderer.start.connect(self.renderer.run)
            self.renderer.start.emit(self._width, self._height)
            
            self.update()

    # hou module stuff
    def camera(self) -> ObjNode or None:
        '''
        If the viewport is currently looking through a camera or light (not necessarily locked to it), this returns an object representing the camera/light’s node. 
        Returns None if the viewport is not looking through a camera/light.
        '''
        return None