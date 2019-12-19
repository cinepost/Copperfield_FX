from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

from OpenGL.raw.GL.VERSION.GL_1_5 import glBufferData as rawGlBufferData

import math
import logging
from PIL import Image

import numpy as np
import pyopencl as cl

from copper import hou
from copper.op.node_type_category import Cop2NodeTypeCategory
from copper.ui.signals import signals
from copper.ui.widgets import PathBarWidget
from .base_panel import PathBasedPaneTab

logger = logging.getLogger(__name__)

class CompositeViewPanel(PathBasedPaneTab):
    def __init__(self):
        PathBasedPaneTab.__init__(self, network_controls=True)

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
        self.rebuild_node_image = False
        self.emptyView()

        # connect panel signals
        self.panel.signals.copperSetCompositeViewNode[str].connect(self.setNodeToDisplay)
        #self.panel.signals.copperNodeModified[str].connect(self.updateNodeDisplay)


    def drawCopNodeImageData(self):
        glDisable( GL_LIGHTING )
        glEnable( GL_TEXTURE_2D )

        # texture from COP_Node iamge data
        if self.rebuild_node_image:
            try:
                self.buildCopImageDataTexture()
            except:
                raise 

            self.rebuild_node_image = False

        # draw node extents
        bounds = list(self.node.imageBounds())
        bounds[0] -= self.image_width//2
        bounds[2] -= self.image_width//2
        bounds[1] -= self.image_height//2
        bounds[3] -= self.image_height//2

        #draw bounds grid
        glColor(0.25, 0.25, 0.25)
        glBegin(GL_LINES)
        for dx in range(1, bounds[2] - bounds[0], 256):
            glVertex2d(bounds[0] + dx,bounds[1]);glVertex2d(bounds[0] + dx,bounds[3])

        for dy in range(1, bounds[3] - bounds[1], 256):
            glVertex2d(bounds[0], bounds[1] + dy);glVertex2d(bounds[2], bounds[1] + dy)

        glEnd()

        glColor(.05, .15, .85)
        glBegin(GL_LINES)
        glVertex2d(bounds[0],bounds[3]);glVertex2d(bounds[2],bounds[3])
        glVertex2d(bounds[2],bounds[3]);glVertex2d(bounds[2],bounds[1])
        glVertex2d(bounds[2],bounds[1]);glVertex2d(bounds[0],bounds[1])
        glVertex2d(bounds[0],bounds[1]);glVertex2d(bounds[0],bounds[3])
        glEnd()

        # Draw actual image data
        glBindTexture(GL_TEXTURE_2D, self.node_gl_tex_id)

        glColor(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0,0.0)
        glVertex2d(-self.image_width/2, self.image_height/2)
        glTexCoord2f(1.0,0.0)
        glVertex2d(self.image_width/2, self.image_height/2)
        glTexCoord2f(1.0,1.0)
        glVertex2d(self.image_width/2, -self.image_height/2)
        glTexCoord2f(0.0,1.0);
        glVertex2d(-self.image_width/2, -self.image_height/2)
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
        if self.node:
            self.drawCopNodeImageData()

        # draw outline
        glDisable(GL_MULTISAMPLE)
        glDisable(GL_LINE_SMOOTH)
        glColor(.5, .5, .5)
        glBegin(GL_LINES)
        glVertex2d(-self.image_width/2,self.image_height/2);glVertex2d(self.image_width/2,self.image_height/2)
        glVertex2d(self.image_width/2,self.image_height/2);glVertex2d(self.image_width/2,-self.image_height/2)
        glVertex2d(self.image_width/2,-self.image_height/2);glVertex2d(-self.image_width/2,-self.image_height/2)
        glVertex2d(-self.image_width/2,-self.image_height/2);glVertex2d(-self.image_width/2,self.image_height/2)
        glEnd()
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_LINE_SMOOTH)

        # switch to 2D for text overlay
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho( 0, self.view_width, self.view_height, 0, -1, 1 )

        if self.node:
            glColor3f(0, 1, 0)
            self.renderText( 10, 20, self.node.path(), self.font )

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
        glTexEnvf(GL_TEXTURE_FILTER_CONTROL, GL_TEXTURE_LOD_BIAS, -1) # Uncomment to keep texture sharp

        # bind display node texture
        self.node_gl_tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.node_gl_tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glBindTexture(GL_TEXTURE_2D, 0)

    def reset_view(self):
        self.scale = 0.0 
        self.pivot_x = 0.0
        self.pivot_y = 0.0
        self.updateGL()

    def buildCopImageDataTexture(self):
        if not self.node:
            return

        image_width, image_height = self.node.xRes(), self.node.yRes()
        logger.debug("Node size to display: %s %s" % (image_width, image_height))

        cl_image = self.node.getCookedData()
        cl_ctx = hou.openclContext()
        cl_queue = hou.openclQueue()

        event = None

        glBindTexture(GL_TEXTURE_2D, self.node_gl_tex_id)

        if cl.have_gl():
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA32F, image_width, image_height, 0, GL_RGB, GL_FLOAT, None)
            node_gl_texture = cl.GLTexture(cl_ctx, cl.mem_flags.WRITE_ONLY, GL_TEXTURE_2D, 0, self.node_gl_tex_id, 2) 

            # Aquire OpenGL texture object
            cl.enqueue_acquire_gl_objects(cl_queue, [node_gl_texture])
            
            # copy OpenCL buffer to OpenGl texture
            cl.enqueue_copy_image(cl_queue, cl_image, node_gl_texture, (0,0), (0,0), (image_width, image_height), wait_for=(event,))

            # Release OpenGL texturte object
            cl.enqueue_release_gl_objects(cl_queue, [node_gl_texture])
            hou.openclQueue().finish()
        else:
            mapped_buff = cl.enqueue_map_image(cl_queue, cl_image, cl.map_flags.READ, (0,0), (image_width, image_height), (image_height, image_width, 4), np.float32, 'C')
            texture_data = mapped_buff[0].copy()
            mapped_buff[0].base.release(cl_queue)

            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA32F, image_width, image_height, 0, GL_RGBA, GL_FLOAT, texture_data)


        glGenerateMipmap(GL_TEXTURE_2D)  #Generate mipmaps now!!!
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glBindTexture(GL_TEXTURE_2D, 0)


    @QtCore.pyqtSlot(str)
    def updateNodeDisplayOld(self, node_path=None):
        node = hou.node(node_path)
        if node and node == self.node: # ensure we a re updating the same node as shown before
            logger.debug("Updating node %s for display" % node.path())
            if node.needsToCook():
                self.node.cook()
            
            #self.image_width = self.node.xRes()
            #self.image_height = self.node.yRes()
            #self.rebuild_node_image = True

            #self.updateGL()

    @QtCore.pyqtSlot()
    def updateNodeDisplay(self):
        self.image_width = self.node.xRes()
        self.image_height = self.node.yRes()
        self.rebuild_node_image = True

        self.updateGL()

    @QtCore.pyqtSlot(str)    
    def setNodeToDisplay(self, node_path=None):
        node = hou.node(node_path)
        if node:
            if self.node != node:
                logger.debug("Setting node %s as current to display" % node_path)
                self.node = node
                self.node.signals.opCookingDone.connect(self.updateNodeDisplay)
                if self.node.needsToCook():
                    self.node.cook()
                
                #self.image_width = self.node.xRes()
                #self.image_height = self.node.yRes()
                self.rebuild_node_image = True
  
        else:
            self.emptyView()

        #self.updateGL()

    def emptyView(self):
        self.node = None
        self.node_path = None
        self.image_width = 1280
        self.image_height = 720
        self.ar = 1.0 * self.image_height / self.image_width
        
    def wheelEvent(self, event):
         # Zoom Factor
        zoomInFactor = 1.05
        zoomOutFactor = 1 / zoomInFactor

        # Zoom
        delta = event.angleDelta() / 8

        if delta.y() > 0:
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
        pass

    def mousePressEvent(self, e):
        self.isPressed = True

    def mouseReleaseEvent(self, e):
        self.isPressed = False

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            node_path = str(event.mimeData().text())
            node = hou.node(node_path)
            if node:
                if node.type().category().name() == "Cop2":
                    event.acceptProposedAction()

    def dropEvent(self, event):
        node_path = event.mimeData().text()
        signals.copperSetCompositeViewNode.emit(str(node_path))
        event.acceptProposedAction()


