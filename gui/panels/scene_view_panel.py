from PyQt4 import QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import numpy
import copper
import math

from copper import engine
from gui.signals import signals
from gui.widgets import PathBarWidget
from base_panel import BasePanel

class SceneViewPanel(BasePanel):
    def __init__(self):  
        BasePanel.__init__(self) 

        self.path_bar_widget = PathBarWidget()
        self.network_view_widget = SceneViewWidget()

        self.setNetworkControlsWidget(self.path_bar_widget)
        self.addWidget(self.network_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Network View"

    @classmethod
    def hasNetworkControls(cls):
        return True


class SceneViewWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.width = 640
        self.height = 480
        self.setMinimumSize(640, 480)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(-2.5, 0.5, -6.0)
        glColor3f( 1.0, 1.5, 0.0 );
        glPolygonMode(GL_FRONT, GL_FILL);

        glBegin(GL_TRIANGLES)
        glVertex3f(2.0,-1.2,0.0)
        glVertex3f(2.6,0.0,0.0)
        glVertex3f(2.9,-1.2,0.0)
        glEnd()

        glFlush()

    def resizeGL(self, width, height):
        self.width = width
        self.height = height

    def initializeGL(self):
        glClearDepth(1.0)              
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()                    
        gluPerspective(45.0,1.33,0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW)


