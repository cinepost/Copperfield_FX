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
        self.node = node

    def paintGL(self):
        glMatrixMode( GL_PROJECTION )
        glLoadIdentity()
        glMatrixMode( GL_MODELVIEW );
        glLoadIdentity();

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glDisable( GL_LIGHTING )
        glEnable( GL_TEXTURE_2D )
        glBindTexture(GL_TEXTURE_2D, self.texid)

        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex2d(-.5,.5);
        glTexCoord2f(1.0, 1.0); glVertex2d(.5,.5);
        glTexCoord2f(1.0, 0.0); glVertex2d(.5,-.5);
        glTexCoord2f(0.0, 0.0); glVertex2d(-.5,-.5);
        glEnd()

        glDisable( GL_TEXTURE_2D )
        glColor(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2d(-.5,.5);glVertex2d(.5,.5);
        glVertex2d(.5,.5);glVertex2d(.5,-.5);
        glVertex2d(.5,-.5);glVertex2d(-.5,-.5);
        glVertex2d(-.5,-.5);glVertex2d(-.5,.5);
        glEnd()

        glFlush()

    def resizeGL(self, width, height):
        self.width, self.height = width, height
        glViewport(0, 0, width, height)

    def initializeGL(self):
        img = Image.open("media/deftex_02.jpg")
        ix, iy, image = img.size[0], img.size[1], img.tostring()

        self.bindImageTexture()

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # the window corner OpenGL coordinates are (-+1, -+1)
        glOrtho(-1, 1, -1, 1, -1, 1)

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
    def setNode(self, node):
        self.node = node
        glBindTexture(GL_TEXTURE_2D, self.texid)
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(
            GL_TEXTURE_2D, 0, 3, self.node.width, self.node.height, 0,
            GL_RGBA, GL_UNSIGNED_BYTE, self.node.get_out_buffer
        )


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