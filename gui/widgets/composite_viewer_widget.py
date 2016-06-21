from PyQt4 import QtGui, QtCore
from PyQt4 import QtOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

from OpenGL.raw.GL.VERSION.GL_1_5 import glBufferData as rawGlBufferData

import math
from PIL import Image

import pyopencl as cl

from path_bar_widget import PathBarWidget

class CompositeViewerWidget(QtGui.QFrame):
    def __init__(self, parent, engine = None):
        super(CompositeViewerWidget, self).__init__(parent)
        self.engine = engine
        vbox = QtGui.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)

        path_bar = PathBarWidget(self)
        image_viewer = CompositeViewerWorkareaWidget(self, engine)

        vbox.addWidget(path_bar)
        vbox.addWidget(image_viewer)
        self.setLayout(vbox)

    def copy(self):
        return CompositeViewerWidget(None, engine=self.engine)

class CompositeViewerWorkareaWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None, engine = None):
        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)
        QtOpenGL.QGLWidget.__init__(self, format, parent)
        if not self.isValid():
            raise OSError("OpenGL not supported.")

        self.engine = engine
        self.setMouseTracking(True)
        self.isPressed = False
        self.oldx = self.oldy = 0
        self.setNode()

        self.setCursor(QtCore.Qt.CrossCursor)

        self.scale = 1.0 
        self.pivot_x = 0.0
        self.pivot_y = 0.0

        self.node = None
        self.node_path = None
        self.draw_new_node = False

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

            glBindTexture(GL_TEXTURE_2D, self.texid_cl)
        else:
            # default texture
            glBindTexture(GL_TEXTURE_2D, self.texid_gl)    

        glBegin(GL_QUADS)
        glTexCoord2f(0.0,0.0)
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 0.0f, 1.0f);
        glVertex2d(-self.img_half_width, -self.img_half_height)
        glTexCoord2f(1.0,0.0)
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 1.0f, 1.0f);
        glVertex2d(self.img_half_width, -self.img_half_height)
        glTexCoord2f(1.0,1.0)
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 1.0f, 0.0f);
        glVertex2d(self.img_half_width, self.img_half_height)
        glTexCoord2f(0.0,1.0);
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 0.0f, 0.0f);
        glVertex2d(-self.img_half_width, self.img_half_height)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable( GL_TEXTURE_2D )

    def paintGL(self):
        if not self.isValid():
            return

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glLoadIdentity()
        glTranslated (0.0 + self.pivot_x, 0.0 - self.pivot_y, -10.0)
        glScaled (1.0 * self.scale, 1.0 * self.scale, 1.0)
        glColor4f(1.0, 1.0, 1.0, 1.0)

        self.drawCopNodeImageData()

        glColor(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2d(-self.img_half_width,self.img_half_height);glVertex2d(self.img_half_width,self.img_half_height)
        glVertex2d(self.img_half_width,self.img_half_height);glVertex2d(self.img_half_width,-self.img_half_height)
        glVertex2d(self.img_half_width,-self.img_half_height);glVertex2d(-self.img_half_width,-self.img_half_height)
        glVertex2d(-self.img_half_width,-self.img_half_height);glVertex2d(-self.img_half_width,self.img_half_height)
        glEnd()

        # draw text
        if self.node_path:
            self.renderText( 0.0, 0.0, 0.0, self.node_path ) 
        else:
            self.renderText( 0.0, 0.0, 0.0, "No output node selected !" )    

        glFlush()

    def resizeGL(self, width, height):
        if self.isValid() and width > 0 and height > 0:
            glViewport(0, 0, width, height)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(-width/2.0, width/2.0, -height/2.0, height/2.0, -100.0, 100.0)
            glMatrixMode(GL_MODELVIEW)

    def initializeGL(self):
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_LINE_SMOOTH)
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDisable(GL_DEPTH_TEST)
        glColor4f(1.0, 1.0, 1.0, 1.0)

        # bind default texture here  
        self.texid_gl = self.bindTexture(QtGui.QImage("media/deftex_02.jpg"), GL_TEXTURE_2D, GL_RGBA) 
        self.texid_cl = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.texid_cl)
        glTexParameteri(GL_TEXTURE_2D, GL_GENERATE_MIPMAP, GL_FALSE )
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glBindTexture(GL_TEXTURE_2D, 0)

    def reset_view(self):
        self.scale = 0.0 
        self.pivot_x = 0.0
        self.pivot_y = 0.0
        self.updateGL()

    def buildCopImageDataTexture(self):
        if self.node:
            # bind texture from current compy node
            img_cl_buffer = self.node.getOutDevBuffer()

            #glBindTexture(GL_TEXTURE_2D, self.texid_cl)
            glBindTexture(GL_TEXTURE_2D, 0)

            print "Node size: %s %s" % (self.node.getWidth() , self.node.getHeight())

            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA32F, self.node.getWidth() , self.node.getHeight(), 0, GL_RGBA, GL_FLOAT, None)
            display_cl_gl_texture = cl.GLTexture(self.engine.ctx, self.engine.mf.WRITE_ONLY,  GL_TEXTURE_2D, 0, self.texid_cl, 2)    
            self.engine.queue.finish()

            #pbo = glGenBuffers(1)
            #glBindBuffer(GL_ARRAY_BUFFER, pbo)
            #rawGlBufferData(GL_ARRAY_BUFFER,  self.node.width * self.node.height, None, GL_STATIC_DRAW)
            #glEnableClientState(GL_VERTEX_ARRAY)
            
            #try:
            #    display_pbo_cl = cl.GLBuffer(self.engine.ctx, self.engine.mf.WRITE_ONLY, int(pbo))
            #except:
            #    raise
            #cl.enqueue_acquire_gl_objects(queue, [coords_dev])
            #prog.generate_sin(queue, (n_vertices,), None, coords_dev)
            #cl.enqueue_release_gl_objects(queue, [coords_dev])

            print "Binding texture"
            glBindTexture(GL_TEXTURE_2D, 0)
            print "Binding done"

    @QtCore.pyqtSlot()    
    def setNode(self, node_path = None):
        if node_path:
            print "Showing node %s" % node_path
            
            if self.node_path != node_path:
                self.node = self.engine.node(node_path)
                self.node_path = node_path
                self.node.cook()
                self.image_width = self.node.getWidth()
                self.image_height = self.node.getHeight()
                self.draw_new_node = True
  
        else:
            self.node = None
            self.node_path = None
            self.image_width = 1920
            self.image_height = 1080
            self.ar = 1.0 * self.image_height / self.image_width

        self.img_half_width = self.image_width / 2.0
        self.img_half_height = self.image_height / 2.0
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