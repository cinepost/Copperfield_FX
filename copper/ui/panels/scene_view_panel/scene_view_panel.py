from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import logging
import numpy
from copper import hou
import math

import moderngl

from copper.ui.utils import clearLayout
from copper.ui.signals import signals
from copper.ui.widgets import PathBarWidget, CollapsableWidget
from copper.ui.panels.base_panel import PathBasedPaneTab

from copper.vmath import Matrix4, Vector3
from .camera import Camera
from .ogl_objcache import OGL_Scene_Manager

from .layouts import viewport_layout_types

logger = logging.getLogger(__name__)


class DisplayOptionsWidget(CollapsableWidget):
    def __init__(self, parent=None):
        CollapsableWidget.__init__(self, parent)

        self.toggle_points_btn = QtWidgets.QToolButton(self)
        self.toggle_points_btn.setCheckable(True)
        self.toggle_points_btn.setObjectName("show_points")
        self.toggle_points_btn.setIcon(QtGui.QIcon('gui/icons/main/scene_view/points.svg'))
        self.toggle_points_btn.setStatusTip('Show/hide geometry points')

        self.addWidget(self.toggle_points_btn)
        self.addStretch(1)



class SceneViewPanel(PathBasedPaneTab):
    def __init__(self):  
        PathBasedPaneTab.__init__(self) 

        self._show_points = False
        self.display_options = DisplayOptionsWidget(self)
        self.display_options.toggle_points_btn.pressed.connect(self.toggleShowPoints)

        self.views_layout = None

        self.views_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        self.views_layout.setSpacing(2)
        self.views_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.addWidget(self.display_options)
        self.addLayout(self.views_layout)
        

        # layout switching button
        self.layouts_button = QtWidgets.QPushButton("Layouts", self)
        self.layouts_button.setIcon(QtGui.QIcon("gui/icons/main/go-next.svg"))

        mapper = QtCore.QSignalMapper(self)
        layouts_menu = QtWidgets.QMenu()

        for layout in viewport_layout_types:
            action = QtWidgets.QAction(QtGui.QIcon(layout['icon']), layout['name'], self)
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
        logger.debug("LAYOUT NAME: %s" % layout_name)

        #clear views layout
        clearLayout(self.views_layout, delete_widgets=False)
        logger.debug("Layout : %s" % self.views_layout.count())

        self.views_layout.addWidget(self.viewports["persp"])

        if layout_name=="Four Views":
            self.views_layout.addWidget(self.viewports["top"])
            self.views_layout.addWidget(self.viewports["top"])
            self.views_layout.addWidget(self.viewports["persp"])

    @QtCore.pyqtSlot()
    def toggleShowPoints(self):
        self._show_points = not self._show_points
        for view in self.views_layout.children():
            view.repaint()


class SceneViewWidget(QtOpenGL.QGLWidget):

    OGL_Scene_Manager = OGL_Scene_Manager()
    
    def __init__(self, parent, panel=None, share_widget=None):
        format = QtOpenGL.QGLFormat()
        format.setVersion(3, 3)
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

        logger.debug("SceneViewWidget created")

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
        #glPolygonMode(GL_BACK, GL_LINE)

        #glTranslatef(0.0, 0.0, 0.0)

        for node in hou.node("/obj").children():
            ogl_obj_cache = SceneViewWidget.OGL_Scene_Manager.getObjNodeGeometry(node)

            if ogl_obj_cache:
                logger.debug("Drawing node: %s" % node.path())

                transform = node.worldTransform()
                #glPushMatrix()
                #glMultMatrixf(transform.m)

                # draw points
                if self.panel._show_points:
                    #glColor4f(0.0, 0.0, 1.0, 1.0)
                    if ogl_obj_cache.pointsCount() > 0:
                        logger.debug("Drawing points for: %s" % node.path())
                        glPointSize( 3.0 )
                        glBindBuffer (GL_ARRAY_BUFFER, ogl_obj_cache.pointsVBO())

                        glEnableClientState(GL_VERTEX_ARRAY)

                        glVertexPointer (3, GL_FLOAT, 0, None)
                        glDrawArrays (GL_POINTS, 0, ogl_obj_cache.pointsCount())

                        glDisableClientState(GL_VERTEX_ARRAY)

                        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0) # reset

                # draw polygons
                #glUseProgram(SceneViewWidget.OGL_Scene_Manager.defaultShaderProgram())
                if len(node.displayNode().geometry()._points) > 0: #ogl_obj_cache.polyCount() > 0:
                    logger.debug("Drawing geometry for: %s" % node.path())
                    #vao = self.ctx.simple_vertex_array(SceneViewWidget.OGL_Scene_Manager.m.program,  vbo, 'in_vert', 'in_color')
                    vao = self.ctx.simple_vertex_array(SceneViewWidget.OGL_Scene_Manager.m.program, ogl_obj_cache.pointsVBO(), "in_vert")
                    vao.render(moderngl.LINE_STRIP)
                    """
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
                    """
                #glPopMatrix()
                glUseProgram(0)

    @QtCore.pyqtSlot(str)
    def updateNodeDisplay(self, node_path=None):
        # Now using quick and dirty hack to check that only geometry nodes changes reflected in scene view
        if str(node_path).startswith("/obj"):
            self.updateGL()

    def paintGL(self):
        self.ctx = moderngl.create_context(require=330)
        SceneViewWidget.OGL_Scene_Manager.setCtx(self.ctx)
        self.screen = self.ctx.detect_framebuffer()
        self.init()
        self.render()
        self.paintGL = self.render


    def render(self):
        self.screen.use()
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Drab back plane elements
        #glMatrixMode(GL_MODELVIEW)
        #glLoadIdentity()
        #glMatrixMode(GL_PROJECTION)
        #glLoadIdentity()
        #glOrtho(0.0, self.width, self.height, 0.0, -100.0, 100.0)

        # Draw background
        #self.drawBackground(background_image_name = self.viewport.getBackgroundImageName())

        # Draw scene
        #glMatrixMode(GL_PROJECTION)
        #glLoadIdentity()

        # Place viewport camera
        #self.viewport.buildFrustum()
        M = self.viewport.getTransform()

        #glMultMatrixf( M.m )
        #glMatrixMode( GL_MODELVIEW )
        #glLoadIdentity()

        # Place default light
        #glLightfv(GL_LIGHT0, GL_POSITION, [0,0,0,0])
        #glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5,0.5,0.5,1.0]);

        # Draw grid
        #self.drawSceneGrid()

        # Scene objects
        self.drawSceneObjects()
        #glFlush()

        # Draw overlay
        #self.drawOverlay()

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
        pass

    def init(self):
        glClearDepth( 1.0 )              
        #glDepthFunc( GL_LESS )
        glEnable( GL_DEPTH_TEST )
        #glEnable( GL_POINT_SMOOTH )
        #glEnable(GL_MULTISAMPLE)
        #glEnable(GL_LINE_SMOOTH)
        #glShadeModel( GL_SMOOTH )

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

