from PyQt4 import QtGui, QtCore
from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
#from OpenGL.raw.GL.VERSION.GL_1_5 import glBufferData as rawGlBufferData
import math
from PIL import Image

import pyopencl as cl

class ImageviewWidget(QGLWidget):
    def __init__(self, parent=None, engine = None):
        super(ImageviewWidget, self).__init__(parent)
        self.engine = engine
        self.setMinimumWidth(640)
        self.setMinimumHeight(360)
        self.setMouseTracking(True)
        self.isPressed = False
        self.oldx = self.oldy = 0
        self.setNode()

        self.setCursor(QtCore.Qt.CrossCursor)

        self.scale = 1.0 
        self.pivot_x = 0.0
        self.pivot_y = 0.0

    def paintGL(self):
        if not self.isValid():
            return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glDisable( GL_LIGHTING )
        glEnable( GL_TEXTURE_2D )
        if self.node:
            glBindTexture(GL_TEXTURE_2D, self.texid_cl)
        else:
            glBindTexture(GL_TEXTURE_2D, self.texid_gl)    

        glLoadIdentity();
        glTranslated (0.0 + self.pivot_x, 0.0 - self.pivot_y, -10.0);
        glScaled (1.0 * self.scale, 1.0 * self.scale, 1.0);
        glColor4f(1.0, 1.0, 1.0, 1.0);

        glBegin(GL_QUADS)
        glTexCoord2f(0.0,0.0);
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 0.0f, 1.0f);
        glVertex2d(-self.img_half_width, -self.img_half_height);
        glTexCoord2f(1.0,0.0);
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 1.0f, 1.0f);
        glVertex2d(self.img_half_width, -self.img_half_height);
        glTexCoord2f(1.0,1.0);
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 1.0f, 0.0f);
        glVertex2d(self.img_half_width, self.img_half_height);
        glTexCoord2f(0.0,1.0);
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 0.0f, 0.0f);
        glVertex2d(-self.img_half_width, self.img_half_height);
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable( GL_TEXTURE_2D )

        glColor(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2d(-self.img_half_width,self.img_half_height);glVertex2d(self.img_half_width,self.img_half_height);
        glVertex2d(self.img_half_width,self.img_half_height);glVertex2d(self.img_half_width,-self.img_half_height);
        glVertex2d(self.img_half_width,-self.img_half_height);glVertex2d(-self.img_half_width,-self.img_half_height);
        glVertex2d(-self.img_half_width,-self.img_half_height);glVertex2d(-self.img_half_width,self.img_half_height);
        glEnd()

        # draw text
        if self.node:
            node_path = self.node.path
        else:
            node_path = "No output node selected !"    

        self.renderText( 0.0, 0.0, 0.0, node_path ); 

        glFlush()

    def resizeGL(self, width, height):
        self.width, self.height = width, height

        glViewport (0, 0, width, height);
        glMatrixMode (GL_PROJECTION);
        glLoadIdentity();
        glOrtho (-width/2.0, width/2.0, -height/2.0, height/2.0, -10000.0, 10000.0);
        glMatrixMode (GL_MODELVIEW);

    def initializeGL(self):
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glEnable(GL_DEPTH_TEST);
        glColor4f(1.0, 1.0, 1.0, 1.0);

        # bind default texture here  
        self.texid_gl = self.bindTexture(QtGui.QImage("media/deftex_02.jpg"), GL_TEXTURE_2D, GL_RGBA) 
        self.texid_cl = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.texid_cl)
        glTexParameteri(GL_TEXTURE_2D, GL_GENERATE_MIPMAP, GL_FALSE )
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        glBindTexture(GL_TEXTURE_2D, 0)

        self.bindImageTexture()

    def reset_view(self):
        self.scale = 0.0 
        self.pivot_x = 0.0
        self.pivot_y = 0.0
        self.updateGL()

    def bindImageTexture(self):
        if self.node:
            # bind texture from current compy node
            img_cl_buffer = self.node.getOutDevBuffer()

            glBindTexture(GL_TEXTURE_2D, self.texid_cl)
            glFlush()

            print "GL texture : %s" % self.texid_gl
            print "CL texture : %s" % self.texid_cl
            print "Node size: %s %s" % (self.node.width , self.node.height)

            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA32F, self.node.width , self.node.height, 0, GL_RGBA, GL_FLOAT, None)
            display_cl_gl_texture = cl.GLTexture(self.engine.ctx, self.engine.mf.WRITE_ONLY,  GL_TEXTURE_2D, 0, self.texid_cl, 2);    

            pbo = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, pbo)
            rawGlBufferData(GL_ARRAY_BUFFER,  self.node.width * self.node.height, None, GL_STATIC_DRAW)
            glEnableClientState(GL_VERTEX_ARRAY)
            
            try:
                display_pbo_cl = cl.GLBuffer(self.engine.ctx, self.engine.mf.WRITE_ONLY, int(pbo))
            except:
                raise
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
            self.node = self.engine.node(node_path)
            self.bindImageTexture()
            self.image_width = self.node.width
            self.image_height = self.node.height
        else:
            self.node = None
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
        print "mouse press"
        self.isPressed = True

    def mouseReleaseEvent(self, e):
        print "mouse release"
        self.isPressed = False