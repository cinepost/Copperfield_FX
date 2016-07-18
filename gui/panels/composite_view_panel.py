from PyQt4 import QtGui, QtCore, QtOpenGL
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

from OpenGL.raw.GL.VERSION.GL_1_5 import glBufferData as rawGlBufferData

import math
from PIL import Image

import pyopencl as cl

from copper import engine
from copper.op.node_type_category import Cop2NodeTypeCategory
from gui.signals import signals
from gui.widgets import PathBarWidget
from base_panel import NetworkPanel

class CompositeViewPanel(NetworkPanel):
    def __init__(self):
        NetworkPanel.__init__(self, network_controls=True)

        self.image_view_widget = CompositeViewWidget(self, self)
        self.addWidget(self.image_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Composite View"


class CompositeViewWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent, panel):
        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)
        QtOpenGL.QGLWidget.__init__(self, format, parent)

        if not self.isValid():
            raise OSError("OpenGL not supported.")

        self.panel = panel
        self.setMouseTracking(True)
        self.setAcceptDrops(True)
        self.isPressed = False
        self.oldx = 0
        self.oldy = 0

        self.font = QtGui.QFont("verdana", 12)
        self.setCursor(QtCore.Qt.CrossCursor)

        self.zoom = 1.0 

        self.node = None
        self.node_path = None
        self.draw_new_node = False
        self.emptyView()

        self.panel.signals.copperSetCompositeViewNode[str].connect(self.setNodeToDisplay)

    def drawCopNodeImageData(self):
        glDisable( GL_LIGHTING )
        glEnable( GL_TEXTURE_2D )
        # bind proper texture to display
        if self.node:
            # texture from COP_Node iamge data
            if self.draw_new_node:
                try:
                    self.buildCopImageDataTexture()
                except:
                    raise 

                self.draw_new_node = False

            glBindTexture(GL_TEXTURE_2D, self.node_gl_tex_id)

            glBegin(GL_QUADS)
            glTexCoord2f(0.0,0.0)
            glVertex2d(-self.img_half_width, self.img_half_height)
            glTexCoord2f(1.0,0.0)
            glVertex2d(self.img_half_width, self.img_half_height)
            glTexCoord2f(1.0,1.0)
            glVertex2d(self.img_half_width, -self.img_half_height)
            glTexCoord2f(0.0,1.0);
            glVertex2d(-self.img_half_width, -self.img_half_height)
            glEnd()
        else:
            # default texture
            glBindTexture(GL_TEXTURE_2D, self.null_gl_tex_id)    

            glBegin(GL_QUADS)
            glTexCoord2f(0.0,0.0)
            glVertex2d(-self.img_half_width, -self.img_half_height)
            glTexCoord2f(1.0,0.0)
            glVertex2d(self.img_half_width, -self.img_half_height)
            glTexCoord2f(1.0,1.0)
            glVertex2d(self.img_half_width, self.img_half_height)
            glTexCoord2f(0.0,1.0);
            glVertex2d(-self.img_half_width, self.img_half_height)
            glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable( GL_TEXTURE_2D )

    def paintGL(self):
        if not self.isValid():
            return

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        glTranslated (0.0, 0.0, -10.0)
        glScaled (1.0 * self.zoom, 1.0 * self.zoom, 1.0)
        glColor4f(1.0, 1.0, 1.0, 1.0)

        # draw image data
        self.drawCopNodeImageData()

        # draw outline
        glColor(.5, .5, .5)
        glBegin(GL_LINES)
        glVertex2d(-self.img_half_width,self.img_half_height);glVertex2d(self.img_half_width,self.img_half_height)
        glVertex2d(self.img_half_width,self.img_half_height);glVertex2d(self.img_half_width,-self.img_half_height)
        glVertex2d(self.img_half_width,-self.img_half_height);glVertex2d(-self.img_half_width,-self.img_half_height)
        glVertex2d(-self.img_half_width,-self.img_half_height);glVertex2d(-self.img_half_width,self.img_half_height)
        glEnd()

        # switch to 2D for text overlay
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho( 0, self.view_width, self.view_height, 0, -1, 1 )

        if self.node_path:
            glColor3f(0, 1, 0)
            self.renderText( 10, 20, self.node_path, self.font )

            glColor3f(.5, .5, .5)
            self.renderText( 10, 34, "%sx%s" % (self.image_width, self.image_height), self.font )

        # revert to 3D
        glLoadIdentity()
        glOrtho(-self.view_width / 2.0, self.view_width / 2.0, -self.view_height / 2.0, self.view_height / 2.0, -100.0, 100.0)
        glMatrixMode(GL_MODELVIEW)

        glFlush()

    def resizeGL(self, width, height):
        self.view_width = width
        self.view_height = height
        if self.isValid() and self.view_width > 0 and self.view_height > 0:
            glViewport(0, 0, self.view_width, self.view_height)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(-self.view_width / 2.0, self.view_width / 2.0, -self.view_height / 2.0, self.view_height / 2.0, -100.0, 100.0)
            glMatrixMode(GL_MODELVIEW)

    def initializeGL(self):
        glClearDepth(1.0)              
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_LINE_SMOOTH)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glDisable(GL_DEPTH_TEST)
        glColor4f(1.0, 1.0, 1.0, 1.0)

        # bind default texture here  
        self.null_gl_tex_id = self.bindTexture(QtGui.QImage("media/deftex_02.jpg"), GL_TEXTURE_2D, GL_RGBA) 
        glBindTexture(GL_TEXTURE_2D, self.null_gl_tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_GENERATE_MIPMAP, GL_FALSE )
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glBindTexture(GL_TEXTURE_2D, 0)

        self.node_gl_tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.node_gl_tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_GENERATE_MIPMAP, GL_FALSE )
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glBindTexture(GL_TEXTURE_2D, 0)

    def reset_view(self):
        self.scale = 0.0 
        self.pivot_x = 0.0
        self.pivot_y = 0.0
        self.updateGL()

    def buildCopImageDataTexture(self):
        if not cl.have_gl():
            raise BaseException("No OpenGL interop !!!")

        if self.node:
            # bind texture from current compy node
            cl_image_buffer = self.node.getCookedData()

            glBindTexture(GL_TEXTURE_2D, 0)
            glBindTexture(GL_TEXTURE_2D, self.node_gl_tex_id)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA32F, self.node.xRes(),  self.node.yRes(), 0, GL_RGB, GL_FLOAT, None)
            glBindTexture(GL_TEXTURE_2D, 0)

            print "Node size: %s %s" % (self.node.xRes(), self.node.yRes())

            node_gl_texture = cl.GLTexture(engine.openclContext(), cl.mem_flags.WRITE_ONLY, GL_TEXTURE_2D, 0, self.node_gl_tex_id, 2) 

            # Aquire OpenGL texture object
            cl.enqueue_acquire_gl_objects(engine.openclQueue(), [node_gl_texture])
            
            # copy OpenCL buffer to OpenGl texture
            cl.enqueue_copy_image(engine.openclQueue(), cl_image_buffer, node_gl_texture, (0,0), (0,0), (self.node.xRes(), self.node.yRes()), wait_for=None)

            # Release OpenGL texturte object
            cl.enqueue_release_gl_objects(engine.openclQueue(), [node_gl_texture])
            engine.openclQueue().finish()


    @QtCore.pyqtSlot(str)    
    def setNodeToDisplay(self, node_path = None):
        if node_path:
            print "Showing node %s" % node_path
            node_path = str(node_path)
            if self.node_path != node_path:
                self.node = engine.node(node_path)
                self.node_path = node_path
                self.node.cook()
                self.image_width = self.node.xRes()
                self.image_height = self.node.yRes()
                self.img_half_width = self.image_width / 2.0
                self.img_half_height = self.image_height / 2.0
                self.draw_new_node = True
  
        else:
            self.emptyView()

        self.updateGL()

    def emptyView(self):
        self.node = None
        self.node_path = None
        self.image_width = 1280
        self.image_height = 720
        self.ar = 1.0 * self.image_height / self.image_width
        self.img_half_width = self.image_width / 2.0
        self.img_half_height = self.image_height / 2.0

    def wheelEvent(self, event):
         # Zoom Factor
        zoomInFactor = 1.05
        zoomOutFactor = 1 / zoomInFactor

        # Zoom
        if event.delta() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor

        self.zoom *= zoomFactor
        self.updateGL()

    def mouseMoveEvent(self, mouseEvent):
        if int(mouseEvent.buttons()) != QtCore.Qt.NoButton :
            # user is dragging
            delta_x = mouseEvent.x() - self.oldx
            delta_y = self.oldy - mouseEvent.y()
            if int(mouseEvent.buttons()) & QtCore.Qt.LeftButton :
                if int(mouseEvent.buttons()) & QtCore.Qt.MidButton :
                    pass
                    #self.camera.dollyCameraForward( 3*(delta_x+delta_y), False )
                else:
                    pass
                    #self.camera.orbit(self.oldx,self.oldy,mouseEvent.x(),mouseEvent.y())
            elif int(mouseEvent.buttons()) & QtCore.Qt.MidButton :
                pass
                #self.camera.translateSceneRightAndUp( delta_x, delta_y )
            self.update()
        self.oldx = mouseEvent.x()
        self.oldy = mouseEvent.y()

    def mouseDoubleClickEvent(self, mouseEvent):
        print "double click"

    def mousePressEvent(self, e):
        self.isPressed = True

    def mouseReleaseEvent(self, e):
        self.isPressed = False

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            node_path = str(event.mimeData().text())
            node = engine.node(node_path)
            if node:
                if node.type().category().name() == "Cop2":
                    event.acceptProposedAction()

    def dropEvent(self, event):
        node_path = event.mimeData().text()
        signals.copperSetCompositeViewNode.emit(str(node_path))
        event.acceptProposedAction()


