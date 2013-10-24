from PyQt4 import QtGui, QtCore
from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

class ImageviewWidget(QGLWidget):
    node = None # Node to display

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

        glDepthFunc( GL_LEQUAL );
        glEnable( GL_DEPTH_TEST );
        glEnable( GL_CULL_FACE );
        glFrontFace( GL_CCW );
        glDisable( GL_LIGHTING );
        glShadeModel( GL_FLAT );

        glColor(1.0, 1.0, 1.0)
        glBegin(GL_LINE_STRIP)
        glVertex(-1,-1,-1)
        glVertex( 1,-1,-1)
        glVertex( 1, 1,-1)
        glVertex(-1, 1,-1)
        glVertex(-1,-1, 1)
        glVertex( 1,-1, 1)
        glVertex( 1, 1, 1)
        glVertex(-1, 1, 1)
        glEnd()
        glColor(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex( 0, 0, 0)
        glVertex( 1, 0, 0)
        glEnd()
        glColor(0.0, 1.0, 0.0)
        glBegin(GL_LINES)
        glVertex( 0, 0, 0)
        glVertex( 0, 1, 0)
        glEnd()
        glColor(0.0, 0.0, 1.0)
        glBegin(GL_LINES)
        glVertex( 0, 0, 0)
        glVertex( 0, 0, 1)
        glEnd()

        glFlush()

    def resizeGL(self, widthInPixels, heightInPixels):
        glViewport(0, 0, widthInPixels, heightInPixels)

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)

        # glMatrixMode(GL_PROJECTION)
        # glLoadIdentity()

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