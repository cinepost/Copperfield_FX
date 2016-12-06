from PyQt4 import QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import numpy
import copper
import math

from gui.signals import signals
from gui.widgets import PathBarWidget
from base_panel import NetworkPanel


class SceneViewPanel(NetworkPanel):
    def __init__(self):  
        NetworkPanel.__init__(self) 

        self.scene_view_widget = SceneViewWidget(self, self)
        self.addWidget(self.scene_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Scene View"


class VirtualCamera(object):
    def __init__(self):
        self.pos = numpy.array([0.0, 0.0, 5.0])
        self.target = numpy.array([0.0, 0.0, 0.0])
        self.up = numpy.array([0.0, 1.0, 0.0])

    def gluLookAt(self):
        gluLookAt(self.pos[0], self.pos[1], self.pos[2], self.target[0], self.target[1], self.target[2], self.up[0], self.up[1], self.up[2])

    def orbit(self, phi, theta):
        radius = math.sqrt(math.pow(self.pos[0] - self.target[0], 2) + math.pow(self.pos[1] - self.target[1], 2) + math.pow(self.pos[2] - self.target[2], 2))
        self.pos[0] = self.target[0] + radius * math.cos(theta) * math.sin(phi)
        self.pos[1] = self.target[1] + radius * math.sin(theta) * math.sin(phi)
        self.pos[2] = self.target[0] + radius * math.cos(phi)


class SceneViewWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent, panel):
        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)
        QtOpenGL.QGLWidget.__init__(self, format, parent)
        self.panel = panel
        self.width = 1920
        self.height = 1200
        self.setMinimumSize(640, 360)
        self.orbit_mode = False
        self.camera = VirtualCamera()

        # connect panel signals
        self.panel.signals.copperNodeModified[str].connect(self.updateNodeDisplay)

    def drawBackground(self):
        glDisable(GL_DEPTH_TEST)
        glBegin(GL_QUADS)
        glColor3f(0.39, 0.50, 0.55)
        glVertex2f(0.0, 0.0)
        glVertex2f(self.width, 0.0)

        glColor3f(0.75, 0.78, 0.78)
        glVertex2f(self.width, self.height)
        glVertex2f(0.0, self.height)
        glEnd()
        glEnable(GL_DEPTH_TEST)

    def drawSceneGrid(self):
        grid_step = 0.1
        grid_size = 4.0
        grid_half_size = grid_size / 2.0

        # Minor lines
        lines_quantity = int(grid_size / grid_step) + 1
        glColor3f( 0.35, 0.35, 0.35 )
        glLineWidth(0.5)

        # Draw lines
        glBegin(GL_LINES)
        x_coord = - grid_half_size
        for x in range(lines_quantity):
            glVertex3f(x_coord, 0.0, -grid_half_size)
            glVertex3f(x_coord, 0.0, grid_half_size)
            x_coord += grid_step

        z_coord = - grid_half_size
        for z in range(lines_quantity):
            glVertex3f(-grid_half_size, 0.0, z_coord)
            glVertex3f(grid_half_size, 0.0, z_coord)
            z_coord += grid_step

        glEnd()

        # Major lines
        grid_step *= 10
        lines_quantity = int(grid_size / grid_step) + 1
        glLineWidth(1.0)

        # Draw lines
        glBegin(GL_LINES)
        x_coord = - grid_half_size
        for x in range(lines_quantity):
            glVertex3f(x_coord, 0.0, -grid_half_size)
            glVertex3f(x_coord, 0.0, grid_half_size)
            x_coord += grid_step

        z_coord = - grid_half_size
        for z in range(lines_quantity):
            glVertex3f(-grid_half_size, 0.0, z_coord)
            glVertex3f(grid_half_size, 0.0, z_coord)
            z_coord += grid_step

        glEnd()

        # Draw Origin
        glDisable(GL_DEPTH_TEST)
        glLineWidth(1.0)
        glBegin(GL_LINES)
        # X axis
        glColor3f( 0.95, 0.05, 0.05 )
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.8, 0.0, 0.0)
        # Y axis
        glColor3f( 0.05, 0.95, 0.05 )
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.8, 0.0)
        # z axis
        glColor3f( 0.05, 0.05, 0.95 )
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.8)
        glEnd()

        glEnable(GL_DEPTH_TEST)

    def drawSceneObjects(self):
        glTranslatef(0.0, 0.0, 0.0)

        glPointSize( 3.0 )
        for node in copper.engine.node("/obj").children():
            print "Drawing node: %s" % node.path()
            display_node = node.displayNode()
            if display_node:
                print "Drawing sop node: %s" % display_node.path()
                geometry = display_node.geometry()
                if geometry:
                    print "Drawing geometry for sop node: %s" % display_node.path()
                    glColor3f(0.2,0.3,0.9)
                    glBegin(GL_POINTS)

                    for point in geometry.points():
                        glVertex3f(point.x, point.y, point.z)

                    glEnd()

    @QtCore.pyqtSlot(str)
    def updateNodeDisplay(self, node_path=None):
        # Now using quick and dirty hack to check that only geometry nodes changes reflected in scene view
        if str(node_path).startswith("/obj"):
            self.updateGL()

    def paintGL(self):
        if not self.isValid():
            return

        glClearColor(0.5, 0.5, 0.5, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Drab back plane elements
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.width, self.height, 0.0, -100.0, 100.0)

        # Background
        self.drawBackground()

        # Draw scene
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(self.width)/float(self.height),0.1, 1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.camera.gluLookAt()

        # Grid
        self.drawSceneGrid()

        # Scene objects
        self.drawSceneObjects()

        glFlush()

    def resizeGL(self, width, height):
        self.width = width
        self.height = height
        
        if self.isValid():
            glViewport(0, 0, width, height)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(45.0, float(width)/float(height), 0.1, 1000.0)
            glMatrixMode(GL_MODELVIEW)

    def initializeGL(self):
        glClearDepth( 1.0 )              
        glDepthFunc( GL_LESS )
        glEnable( GL_DEPTH_TEST )
        glEnable( GL_POINT_SMOOTH )
        #glEnable(GL_MULTISAMPLE)
        #glEnable(GL_LINE_SMOOTH)
        glShadeModel( GL_SMOOTH )

        #glMatrixMode(GL_PROJECTION)
        ##lLoadIdentity()                    
        #gluPerspective(45.0,1.33,0.1, 100.0) 
        #glMatrixMode(GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.orbit_mode = True
        self.lastMousePos = event.pos()
        self.setCursor(QtCore.Qt.ClosedHandCursor)

    def mouseReleaseEvent(self, event):
        self.orbit_mode = False
        self.setCursor(QtCore.Qt.OpenHandCursor)

    def mouseMoveEvent(self, event):
        if self.orbit_mode:
            phi = (event.x() - self.lastMousePos.x()) * 0.01
            theta = (event.y() - self.lastMousePos.y()) * 0.01

            print "phi: %s theta: %s" % (phi, theta)

            self.camera.orbit(phi, theta)

            self.updateGL()


