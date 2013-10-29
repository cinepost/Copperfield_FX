from PyQt4 import QtGui, QtCore
from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from PIL import Image

class ImageviewWidget(QGLWidget):
    def __init__(self, parent=None, node = None):
        super(ImageviewWidget, self).__init__(parent)
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
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glDisable( GL_LIGHTING )
        glEnable( GL_TEXTURE_2D )
        glBindTexture(GL_TEXTURE_2D, self.texid)

        glLoadIdentity();
        glTranslated (0.0 + self.pivot_x, 0.0 - self.pivot_y, -10.0);
        glScaled (1.0 * self.scale, 1.0 * self.scale, 1.0);
        glColor4f(1.0, 1.0, 1.0, 1.0);

        glBegin(GL_QUADS)
        glTexCoord2f(0.0,0.0);
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 0.0f, 1.0f);
        glVertex2d(-self.image_width/2.0, -self.image_height/2.0);
        glTexCoord2f(1.0,0.0);
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 1.0f, 1.0f);
        glVertex2d(self.image_width/2.0, -self.image_height/2.0);
        glTexCoord2f(1.0,1.0);
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 1.0f, 0.0f);
        glVertex2d(self.image_width/2.0, self.image_height/2.0);
        glTexCoord2f(0.0,1.0);
        #glMultiTexCoord2fARB(GL_TEXTURE0_ARB, 0.0f, 0.0f);
        glVertex2d(-self.image_width/2.0, self.image_height/2.0);
        glEnd()

        glDisable( GL_TEXTURE_2D )
        glColor(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2d(-1.0,self.ar);glVertex2d(1.0,self.ar);
        glVertex2d(1.0,self.ar);glVertex2d(1.0,-self.ar);
        glVertex2d(1.0,-self.ar);glVertex2d(-1.0,-self.ar);
        glVertex2d(-1.0,-self.ar);glVertex2d(-1.0,self.ar);
        glEnd()

        glFlush()

    def resizeGL(self, width, height):
        self.width, self.height = width, height
        #glViewport(0, 0, width, height)

        glViewport (0, 0, width, height);
        glMatrixMode (GL_PROJECTION);
        glLoadIdentity();
        glOrtho (-width/2.0, width/2.0, -height/2.0, height/2.0, -10000.0, 10000.0);
        glMatrixMode (GL_MODELVIEW);

    def initializeGL(self):
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glDisable(GL_DEPTH_TEST);
        glColor4f(1.0, 1.0, 1.0, 1.0);

        self.bindImageTexture()

    def reset_view(self):
        self.scale = 0.0 
        self.pivot_x = 0.0
        self.pivot_y = 0.0
        self.updateGL()

    def bindImageTexture(self):
        if self.node:
            # bind texture from current compy node
            pass
        else:
            # bind default texture here
            image = QtGui.QImage("media/deftex_02.jpg")    
            self.texid = self.bindTexture(image, GL_TEXTURE_2D, GL_RGBA) 

        glGenerateMipmap(GL_TEXTURE_2D);  #Generate num_mipmaps number of mipmaps here.
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);

    @QtCore.pyqtSlot()    
    def setNode(self, node = None):
        if node:
            self.node = node
            self.bindImageTexture()
            self.image_width = self.node.width
            self.image_height = self.node.height
        else:
            self.node = None
            self.image_width = 1920
            self.image_height = 1080
            self.ar = 1.0 * self.image_height / self.image_width    


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