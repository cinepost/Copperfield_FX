from PyQt4 import QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import numpy
import copper
import math

from gui.utils import clearLayout
from gui.signals import signals
from gui.widgets import PathBarWidget, CollapsableWidget
from gui.panels.base_panel import NetworkPanel

from copper.vmath import Matrix4, Vector3
from .camera import Camera
from .ogl_objcache import OGL_Scene_Manager

from .layouts import viewport_layout_types


class DisplayOptionsWidget(CollapsableWidget):
    def __init__(self, parent=None):
        CollapsableWidget.__init__(self, parent)

        self.snap_to_grid_btn = QtGui.QPushButton()
        self.snap_to_grid_btn.setCheckable(True)
        self.snap_to_grid_btn.setIcon(QtGui.QIcon('gui/icons/main/network_view/snap_to_grid.svg'))
        self.snap_to_grid_btn.setStatusTip('Show/hide grid and enable/disable snapping')

        self.addWidget(self.snap_to_grid_btn)
        self.addStretch(1)



class SceneViewPanel(NetworkPanel):
    def __init__(self):  
        NetworkPanel.__init__(self) 

        self.display_options = DisplayOptionsWidget(self)

        self.views_layout = None

        self.views_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
        self.views_layout.setSpacing(2)
        self.addLayout(self.views_layout)
        self.addWidget(self.display_options)

        # layout switching button
        self.layouts_button = QtGui.QPushButton("Layouts", self)
        self.layouts_button.setIcon(QtGui.QIcon("gui/icons/main/go-next.svg"))

        mapper = QtCore.QSignalMapper(self)
        layouts_menu = QtGui.QMenu()

        for layout in viewport_layout_types:
            action = QtGui.QAction(QtGui.QIcon(layout['icon']), layout['name'], self)
            mapper.setMapping(action, layout['name'])
            action.setShortcut(layout['shortcut'])
            action.triggered.connect(mapper.map)
            layouts_menu.addAction(action)

        mapper.mapped['QString'].connect(self.makeViewsLayout)
        self.layouts_button.setMenu(layouts_menu)
        self.path_bar_widget.layout.addWidget(self.layouts_button)

        # create default viewports
        persp = SceneViewWidget(None, self)
        top   = SceneViewWidget(None, self, persp)
        bottom= SceneViewWidget(None, self, persp)
        left  = SceneViewWidget(None, self, persp)
        right = SceneViewWidget(None, self, persp)
        self.viewports = {
            "persp": persp,
            "top": top,
            "bottom": bottom,
            "left": left,
            "right": right
        }

        # create default views layout
        self.makeViewsLayout()


    @classmethod
    def panelTypeName(cls):
        return "Scene View"


    def makeViewsLayout(self, layout_name="Single View"):
        print "LAYOUT NAME: %s" % layout_name

        #clear views layout
        clearLayout(self.views_layout, delete_widgets=False)
        print "Layout : %s" % self.views_layout.count()

        self.views_layout.addWidget(self.viewports["persp"])

        if layout_name=="Four Views":
            self.views_layout.addWidget(self.viewports["top"])
            self.views_layout.addWidget(self.viewports["top"])
            self.views_layout.addWidget(self.viewports["persp"])


class SceneViewWidget(QtOpenGL.QGLWidget):

    OGL_Scene_Manager = OGL_Scene_Manager()
    
    def __init__(self, parent, panel=None, share_widget=None):
        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)

       # QGLContext context, QWidget parent = None, QGLWidget shareWidget = None, Qt.WindowFlags flags = 0
        
        QtOpenGL.QGLWidget.__init__(self, format, parent, share_widget)
        self.pt_font = QtGui.QFont("verdana", 8)
        self.panel = panel
        self.width = 1920
        self.height = 1200
        self.setMinimumSize(160, 160)
        self.orbit_mode = False
        self.old_mouse_x = self.old_mouse_y = 0
        self.cameras = {
            'persp': Camera(),
        }

        self.current_camera = 'persp'

        # connect panel signals
        self.panel.signals.copperNodeModified[str].connect(self.updateNodeDisplay)

        print "SceneViewWidget created"

    def minimumSizeHint(self):
        return QtCore.QSize(200, 200)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def drawBackground(self, background_image_name=""):
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


    def drawSceneObjects(self):
        glPolygonMode(GL_BACK, GL_LINE)
        #glPolygonMode(GL_BACK, GL_POINT)

        glTranslatef(0.0, 0.0, 0.0)

        for node in copper.engine.node("/obj").children():
            ogl_obj_cache = SceneViewWidget.OGL_Scene_Manager.getObjNodeGeometry(node)

            if ogl_obj_cache:
                print "Drawing node: %s" % node.path()

                transform = node.worldTransform()
                glPushMatrix()
                glMultMatrixf(transform.m)

                # draw points
                glColor4f(0.0, 0.0, 1.0, 1.0)
                if ogl_obj_cache.pointsCount() > 0:
                    print "Drawing points for: %s" % node.path()
                    glPointSize( 3.0 )
                    glBindBuffer (GL_ARRAY_BUFFER, ogl_obj_cache.pointsVBO())
                    print "binded"

                    glEnableClientState(GL_VERTEX_ARRAY)

                    glVertexPointer (3, GL_FLOAT, 0, None)
                    glDrawArrays (GL_POINTS, 0, ogl_obj_cache.pointsCount())

                    glDisableClientState(GL_VERTEX_ARRAY)

                    print "drawed"
                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0) # reset


                # draw polygons
                glColor4f(1.0, 1.0, 1.0, 1.0)
                glUseProgram(SceneViewWidget.OGL_Scene_Manager.defaultShaderProgram())
                if ogl_obj_cache.polyCount() > 0:
                    print "Drawing %s polys for: %s" % (ogl_obj_cache.polyCount(), node.path())

                    glEnable(GL_LIGHTING)

                    glBindBuffer (GL_ARRAY_BUFFER, ogl_obj_cache.pointsVBO())
                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ogl_obj_cache.polyIndicesVBO())

                    glEnableClientState(GL_VERTEX_ARRAY)

                    glVertexPointer (3, GL_FLOAT, 0, None)
                    glDrawElements(GL_TRIANGLES, ogl_obj_cache.polyCount()*3, GL_UNSIGNED_INT, None)

                    glDisableClientState(GL_VERTEX_ARRAY)

                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
                    glBindBuffer (GL_ARRAY_BUFFER, 0)

                    glDisable(GL_LIGHTING)

                glPopMatrix()
                glUseProgram(0)

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

        # Draw background
        self.drawBackground(background_image_name = self.viewport.getBackgroundImageName())

        # Draw scene
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # Place viewport camera
        self.viewport.buildFrustum()
        M = self.viewport.getTransform()

        glMultMatrixf( M.m )
        glMatrixMode( GL_MODELVIEW )
        glLoadIdentity()

        # Place default light
        glLightfv(GL_LIGHT0, GL_POSITION, [0,0,0,0])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5,0.5,0.5,1.0]);

        # Draw grid
        self.drawSceneGrid()

        # Scene objects
        self.drawSceneObjects()
        glFlush()

        # Draw overlay
        self.drawOverlay()

        #glFlush()

    def drawOverlay(self):
        glClear( GL_DEPTH_BUFFER_BIT );

        glPushMatrix() #reset
        glLoadIdentity() #modelview

        glMatrixMode( GL_PROJECTION ) #set ortho camera
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, self.width, self.height, 0)

        glMatrixMode( GL_MODELVIEW )

        glDisable( GL_DEPTH_TEST ) # necessary if you want to draw things in the order you call them

        self.drawHUD() # Actually does the drawing

        glEnable( GL_DEPTH_TEST )

        glMatrixMode( GL_PROJECTION )
        glPopMatrix()
        glMatrixMode( GL_MODELVIEW ) 
        glPopMatrix()


    def drawHUD(self):
        pass


    def resizeGL(self, widthInPixels, heightInPixels):
        self.width = widthInPixels
        self.height = heightInPixels
        self.viewport.setViewportDimensions(widthInPixels, heightInPixels)

        if self.isValid():
            glViewport(0, 0, widthInPixels, heightInPixels)
        

    def initializeGL(self):
        glClearDepth( 1.0 )              
        #glDepthFunc( GL_LESS )
        glEnable( GL_DEPTH_TEST )
        glEnable( GL_POINT_SMOOTH )
        #glEnable(GL_MULTISAMPLE)
        #glEnable(GL_LINE_SMOOTH)
        glShadeModel( GL_SMOOTH )

        SceneViewWidget.OGL_Scene_Manager.buildShaderPrograms() # build shader programs for OGL_Scene_Manager


    @property
    def viewport(self):
        return self.cameras[self.current_camera]


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


