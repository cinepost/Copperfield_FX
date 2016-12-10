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

from copper.vmath import Matrix4, Vector3


class SceneViewPanel(NetworkPanel):
    def __init__(self):  
        NetworkPanel.__init__(self) 

        self.scene_view_widget = SceneViewWidget(self, self)
        self.addWidget(self.scene_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Scene View"


class Camera(object):
    def __init__(self, position=[5,5,5], target=[0,0,0], fov_degrees = 45.0, near_plane = 0.1, far_plane = 1000.0):
        self.fov_degrees = self.default_fov_degrees = fov_degrees
        self.orbiting_speed_degrees_per_radians = 300.0

        self.near_plane = self.default_near_plane = near_plane
        self.far_plane = self.default_far_plane = far_plane

        # point of view, or center of camera; the ego-center; the eye-point
        self.position = self.default_position = Vector3(position)

        # point of interest; what the camera is looking at; the exo-center
        self.target = self.default_target = Vector3(target)

        # This is the up vector for the (local) camera space
        self.up = Vector3()

        # This is the up vector for the (global) world space;
        # it is perpendicular to the horizontal (x,z)-plane
        self.ground = Vector3([0,1,0])

        # During dollying (i.e. when the camera is translating into
        # the scene), if the camera gets too close to the target
        # point, we push the target point away.
        # The threshold distance at which such "pushing" of the
        # target point begins is this fraction of near_plane.
        # To prevent the target point from ever being clipped,
        # this fraction should be chosen to be greater than 1.0.
        self.target_push_threshold = 1.3

        # We give these some initial values just as a safeguard
        # against division by zero when computing their ratio.
        self.viewportWidthInPixels = 10
        self.viewportHeightInPixels = 10
        self.viewportRadiusInPixels = 5

        self.build_up()

    def reset(self):
        self.fov_degrees = self.default_fov_degrees
        self.near_plane = self.default_near_plane
        self.far_plane = self.default_far_plane
        self.position = self.default_position
        self.target = self.default_target
        self.build_up()

    def build_up(self):
        t2p = self.position - self.target
        left = -(t2p ^ self.ground).normalized()
        self.up = (t2p ^ left).normalized()

    def setViewportDimensions( self, widthInPixels, heightInPixels ):
        self.viewportWidthInPixels = widthInPixels
        self.viewportHeightInPixels = heightInPixels
        self.viewportRadiusInPixels = 0.5*widthInPixels if (widthInPixels < heightInPixels) else 0.5*heightInPixels

    def transform(self):
        tangent = math.tan( self.fov_degrees/2.0 / 180.0 * math.pi )
        viewportRadius = self.near_plane * tangent
        if self.viewportWidthInPixels < self.viewportHeightInPixels:
            viewportWidth = 2.0*viewportRadius
            viewportHeight = viewportWidth * self.viewportHeightInPixels / float(self.viewportWidthInPixels)
        else:
            viewportHeight = 2.0*viewportRadius
            viewportWidth = viewportHeight * self.viewportWidthInPixels / float(self.viewportHeightInPixels)
        glFrustum(
            - 0.5 * viewportWidth,  0.5 * viewportWidth,    # left, right
            - 0.5 * viewportHeight, 0.5 * viewportHeight,   # bottom, top
            self.near_plane, self.far_plane
            )

        M = Matrix4.lookAt(self.position, self.target, self.up, False)
        glMultMatrixf(M.m)

    # Causes the camera to "orbit" around the target point.
    # This is also called "tumbling" in some software packages.
    def orbit(self,delta_x_pixels, delta_y_pixels):
        pixelsPerDegree = 1000 / float(self.orbiting_speed_degrees_per_radians)
        radiansPerPixel = 1.0 / pixelsPerDegree * math.pi / 180.0

        t2p = self.position - self.target

        M = Matrix4.rotationMatrix( - delta_x_pixels * radiansPerPixel, self.ground )
        t2p = M * t2p
        self.up = M * self.up
        
        right = (self.up.normalized() ^ t2p.normalized()).normalized()
        M = Matrix4.rotationMatrix( delta_y_pixels * radiansPerPixel, right )
        t2p = M * t2p
        self.up = M * self.up
        self.position = self.target + t2p

    # This causes the scene to appear to translate right and up
    # (i.e., what really happens is the camera is translated left and down).
    # This is also called "panning" in some software packages.
    # Passing in negative delta values causes the opposite motion.
    def pan( self, delta_x_pixels, delta_y_pixels ):
        direction = self.target - self.position
        distanceFromTarget = direction.length()
        direction = direction.normalized()

        translationSpeedInUnitsPerRadius = distanceFromTarget * math.tan( self.fov_degrees/2.0 / 180.0 * math.pi )
        pixelsPerUnit = self.viewportRadiusInPixels / translationSpeedInUnitsPerRadius

        right = direction ^ self.up

        translation = right*(- delta_x_pixels / pixelsPerUnit) + self.up*(- delta_y_pixels / pixelsPerUnit)

        self.position = self.position + translation
        self.target = self.target + translation

    # This causes the camera to translate forward into the scene.
    # This is also called "dollying" or "tracking" in some software packages.
    # Passing in a negative delta causes the opposite motion.
    # If ``push_target_distance'' is True, the point of interest translates forward (or backward)
    # *with* the camera, i.e. it's "pushed" along with the camera; otherwise it remains stationary.
    def dolly( self, delta_pixels, push_target_distance = None):
        direction = self.target - self.position
        distanceFromTarget = direction.length()
        direction = direction.normalized()

        translationSpeedInUnitsPerRadius = distanceFromTarget * math.tan( self.fov_degrees/2.0 / 180.0 * math.pi )
        pixelsPerUnit = self.viewportRadiusInPixels / translationSpeedInUnitsPerRadius

        dollyDistance = delta_pixels / pixelsPerUnit

        if not push_target_distance:
            distanceFromTarget -= dollyDistance
            if distanceFromTarget < self.target_push_threshold * self.near_plane:
                distanceFromTarget = self.target_push_threshold * self.near_plane

        self.position += direction * dollyDistance
        self.target = self.position + direction * distanceFromTarget


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
        self.old_mouse_x = self.old_mouse_y = 0
        self.cameras = {
            'persp': Camera(),
        }

        self.current_camera = 'persp'

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

        # Draw minor lines
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

        # Draw major lines
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
                        point_pos = point.position()
                        glVertex3f(point_pos[0], point_pos[1], point_pos[2])

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
        self.cameras[self.current_camera].transform()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Grid
        self.drawSceneGrid()

        # Scene objects
        self.drawSceneObjects()

        glFlush()


    def resizeGL(self, widthInPixels, heightInPixels):
        self.width = widthInPixels
        self.height = heightInPixels
        self.cameras[self.current_camera].setViewportDimensions(widthInPixels, heightInPixels)

        if self.isValid():
            glViewport(0, 0, widthInPixels, heightInPixels)
        

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
                    self.cameras[self.current_camera].pan( delta_x, delta_y )
                else:
                    # orbit camera
                    self.cameras[self.current_camera].orbit(delta_x, delta_y)
            elif int(mouseEvent.buttons()) & QtCore.Qt.RightButton :
                # dolly camera
                self.cameras[self.current_camera].dolly( 3*(delta_x + delta_y), False )
            elif int(mouseEvent.buttons()) & QtCore.Qt.MidButton :
                # pan camera
                self.cameras[self.current_camera].pan( delta_x, delta_y )
            
        self.update()
        
        self.old_mouse_x = mouseEvent.x()
        self.old_mouse_y = mouseEvent.y()


