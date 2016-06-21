from PyQt4 import QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

from path_bar_widget import PathBarWidget

import numpy
import copper
import math 

class NodeItem(QtGui.QGraphicsItem):
    def __init__(self, parent = None, scene = None):      
        super(NodeItem, self).__init__(parent, scene)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)

    def paint(self, painter, option, widget=None):
        painter.drawRoundedRect(-20,-10,40,10, 1, 1);

    def boundingRect(self):
        return QtCore.QRectF(-20,-10,40,10)

class NodeFlowScene(QtGui.QGraphicsScene):
    gridSizeWidth = 180
    gridSizeHeight = 80 
    scaleSize = 1.0
    def __init__(self, parent, engine=None):      
        super(NodeFlowScene, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setSceneRect(-100000,-100000,200000,200000)
        self.addItem(NodeItem())

    def scale(self, scaleSize):
        self.scaleSize *= scaleSize

    def drawBackground(self, painter, rect):
        if self.scaleSize < 0.1:
            # Gris size is too small to display
            painter.fillRect(rect, QtGui.QColor(32, 32, 32))

        else:
            # Draw grid
            left = rect.left() - (rect.left() % self.gridSizeWidth)
            top = rect.top() - (rect.top() % self.gridSizeHeight)
     
            lines = []
     
            x = left
            while x < rect.right():
                lines.append( QtCore.QLineF(x, rect.top(), x, rect.bottom()) )
                x += self.gridSizeWidth

            y = top
            while y < rect.bottom():
                lines.append( QtCore.QLineF(rect.left(), y, rect.right(), y) )
                y += self.gridSizeHeight

            painter.fillRect(rect, QtGui.QColor(32, 32, 32))
            pen = QtGui.QPen(QtGui.QColor(64, 64, 64), 1)
            pen.setCosmetic(True)
            painter.setPen(pen)
            painter.drawLines(lines)

class NodeFlowEditorWidget(QtGui.QGraphicsView):
    def __init__(self, parent, engine=None):      
        super(NodeFlowEditorWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.scene = NodeFlowScene(self)
        text = self.scene.addText("GraphicsView rotated clockwise")
        text.setPos(0,0)
        self.setScene(self.scene)
        self.setMouseTracking(True)
        self.setInteractive(True) 

        ## No need to see scroll bars in flow editor
        self.setHorizontalScrollBarPolicy ( QtCore.Qt.ScrollBarAlwaysOff )
        self.setVerticalScrollBarPolicy ( QtCore.Qt.ScrollBarAlwaysOff )

        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)
        self.setViewport( QtOpenGL.QGLWidget(format) ) # Force OpenGL rendering mode.
        self.setViewportUpdateMode( QtGui.QGraphicsView.FullViewportUpdate )
        self.setDragMode( QtGui.QGraphicsView.ScrollHandDrag )
        #self.setSceneRect(-2000,-2000,2000,2000)

    def wheelEvent(self, event):
         # Zoom Factor
        zoomInFactor = 1.05
        zoomOutFactor = 1 / zoomInFactor

        # Set Anchors
        self.setTransformationAnchor(QtGui.QGraphicsView.NoAnchor)
        self.setResizeAnchor(QtGui.QGraphicsView.NoAnchor)

        # Save the scene pos
        oldPos = self.mapToScene(event.pos())

        # Zoom
        if event.delta() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)

        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())

###############


def glCircle(x,y, radius, segments=10):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    t = 0.0
    for i in range(segments+1):
        glVertex2f(x+math.sin(t)*radius, y+math.cos(t)*radius)
        t += math.pi/segments
    glEnd()

class Draggable:
    def isInShape(self, x,y):
        raise NotImplementedError()
        
    def startDrag(self, dragObject):
        pass
        
    def updateDrag(self, dragObject):
        pass
        
    def drawDrag(self, dragObject):
        pass
        
    def dropDrag(self, dragObject):
        pass

class FlowNode(QtCore.QObject, Draggable):
    nodeFont = None # initialized on first construction

    def __init__(self, parent, node, viewPort, pos_x=0.0, pos_y=0.0):
        QtCore.QObject.__init__(self, parent)
        self.fontLineHeight = 8
        self.viewPort = viewPort
        self.node = node
        self.inputs = []
        
        self.properties = {}

        if self.node:
            self.title = self.node.name()
            self.node.setPos(pos_x, pos_y) 
        else:
            self.title = "untitled" 
             
    def path(self):
        return self.node.path()

    def setPos(self, pos_x, pos_y):
        if self.node:
            self.node.setPos(pos_x, pos_y)   

    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def draw(self, selected=False):
        half_width = self.node.width / 2.0
        half_height = self.node.height / 2.0
        x1 = ( self.node.x_pos - half_width ) * self.viewPort.zoom + self.viewPort.pos_x
        y1 = ( self.node.y_pos - half_height ) * self.viewPort.zoom + self.viewPort.pos_y
        x2 = ( self.node.x_pos + half_width ) * self.viewPort.zoom + self.viewPort.pos_x
        y2 = ( self.node.y_pos + half_height ) * self.viewPort.zoom + self.viewPort.pos_y

        # node shadow
        if selected:
            glColor4f(1.0, 0.7, 0.1, 1.0)
            glRectf(x1 - 2.0, y1 - 2.0, x2 + 2.0, y2 + 2.0)
        else:
            glColor4f(0.0, 0.0, 0.0, 0.5)
            glRectf(x1 - 1.0, y1 - 1.0, x2 + 1.0, y2 + 1.0)
        
        # node border
        glColor4f(0.5, 0.5, 0.5, 1.0)
        glRectf(x1, y1, x2, y2)
        
        # node
        if selected:
            glColor4f(0.6, 0.6, 0.6, 1.0)
        else:
            glColor4f(0.5, 0.5, 0.5, 1.0)
        glRectf(x1 + 1.0, y1 + 1.0, x2 - 1.0, y2 - 1.0)
        
        # draw inputs
        if self.viewPort.zoom > 0.2 and 1 < 0:
            i = 0
            inputs = self.node.inputs()
            inputs_area_width = width * 0.8
            inputs_spacing_size = inputs_area_width * 0.2
            input_width = inputs_area_width - inputs_spacing_size * (len(inputs) - 1)
            input_height = height * 0.25
            input_h_offset = (width - inputs_area_width) / 2.0
            for input in inputs:
                ix1 = x1 + input_h_offset + (input_width + inputs_spacing_size) * i
                iy1 = y1 - input_height
                ix2 = x1 + input_h_offset + (input_width + inputs_spacing_size) * i + input_width
                iy2 = y1
                if selected:
                    glColor4f(1.0, 0.7, 0.1, 1.0)
                    glRectf(ix1 - 2, iy1 - 2, ix2 + 2, iy2)

                glColor4f(0.6, 0.6, 0.6, 1.0)
                glRectf(ix1, iy1, ix2, iy2)
                i += 1
        
        glColor4f(0.85, 0.85, 0.85, 1.0)
        #self.nodeFont.setBold(True)
        self.parent().renderText(x2 + 4, y2, self.title) # works only if parent is qglWidget ;)
        #self.nodeFont.setBold(False)

    def isInShape(self, cursor_pos_x, cursor_pos_y):
        half_width = self.node.width / 2.0
        half_height = self.node.height / 2.0
        x1 = ( self.node.x_pos - half_width ) * self.viewPort.zoom + self.viewPort.pos_x
        y1 = ( self.node.y_pos - half_height ) * self.viewPort.zoom + self.viewPort.pos_y
        x2 = ( self.node.x_pos + half_width ) * self.viewPort.zoom + self.viewPort.pos_x
        y2 = ( self.node.y_pos + half_height ) * self.viewPort.zoom + self.viewPort.pos_y
        return x1 <= cursor_pos_x <= x2 and y1 <= cursor_pos_y <= y2
        
    def startDrag(self, dragObject):
        dragObject.custom = (dragObject.startX / self.viewPort.zoom - self.node.x_pos + self.viewPort.pos_x, dragObject.startY / self.viewPort.zoom - self.node.y_pos + self.viewPort.pos_y)
        
    def updateDrag(self, dragObject):
        self.node.x_pos = (dragObject.x - dragObject.custom[0]) / self.viewPort.zoom
        self.node.y_pos = (dragObject.y - dragObject.custom[1]) / self.viewPort.zoom

    def drawDrag(self, dragObject):
        pass

    def __str__(self):
        return "FlowNode '%s'" % self.title
        
    def __repr__(self):
        return "<FlowNode '%s'>" % self.title

class NodeFlowEditorWidgetZ(QtGui.QWidget):
    def __init__(self, parent, engine=None):      
        super(NodeFlowEditorWidgetZ, self).__init__(parent)
        self.engine = engine
        self.initUI()

    def initUI(self):
        vbox = QtGui.QVBoxLayout(self)
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)

        path_bar = PathBarWidget(self)
        node_editor = NodeEditorWorkareaWidget(self, self.engine)

        vbox.addWidget(path_bar)
        vbox.addWidget(node_editor)
        
        self.setLayout(vbox)

    def copy(self):
        return NodeFlowEditorWidget(None, engine=self.engine)


class NodeEditorWorkareaWidget(QtOpenGL.QGLWidget):
    
    dragModeDraggingEmpty = 0
    dragModeDraggingNode = 1
    dragModeDraggingOrigin = 4 # workarea dragging/panning mode
    dragModeDraggingConnectionInToOut = 2
    dragModeDraggingConnectionOutToIn = 3
    
    class DragObject:
        def __init__(self, startX, startY, draggable):
            self.startX = startX
            self.startY = startY
            self.draggable = draggable
            self.custom = None
            self.x = startX
            self.y = startY
            self.draggable.startDrag(self)
            
        def update(self, currentX, currentY):
            self.x = currentX
            self.y = currentY
            self.draggable.updateDrag(self)
            
        def drop(self):
            self.draggable.dropDrag(self)
            
        def draw(self):
            self.draggable.drawDrag(self)

    class ViewPort:
        def __init__(self, pos_x=0.0, pos_y=0.0, width=100, height=100, zoom=1.0):
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.width = width
            self.height = height
            self.zoom = zoom

        def setSize(self, width, height):
            self.width = width
            self.height = height

    class Pointer:
        def __init__(self):
            self.x = 0.0
            self.y = 0.0

    def __init__(self, parent, engine, path="/"):
        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)
        QtOpenGL.QGLWidget.__init__(self, format, parent)
        if not self.isValid():
            raise OSError("OpenGL not supported.")

        self.viewPort = self.ViewPort()
        self.pointer = self.Pointer()
        self.panningMode = False
        self.engine = engine
        self.zoom = 1.0
        self.zoomWheelResolution = 12.0
        self.zoomWheelCounter = self.zoomWheelResolution
        self.zoomMin = 0.05
        self.zoomMax = 5.0
        self.network_label = None
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        self.nodes = []
        self.connections = []
        
        self.dragObject = None
        self.selectedNode = None
        
        self.buildNodeGraph(path)

    def buildNodeGraph(self, path="/"):
        self.nodes = []
        self.connections = []
        
        try:
            self.network_label = self.engine.node(path).__network_label__
        except:
            self.network_label = None

        i = 0
        dx = 170
        dy = 80
        for node in self.engine.node(path).children():
            self.addNode(node, dx * i, dy * i)
            i += 1

        self.updateGL()

    def initializeGL(self):
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_BLEND)
        
    def resizeGL(self, width, height):
        if self.isValid() and width > 0 and height > 0:        
            self.viewPort.setSize(width, height)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluOrtho2D(0, width, height, 0)
            glViewport(0, 0, width, height)
        
    def paintGL(self):
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glClearColor(0.12, 0.12, 0.12, 1.0)
        glClear(GL.GL_COLOR_BUFFER_BIT)

        # draw grid
        if self.zoom > 0.1:
            glColor4f(0.2, 0.24, 0.30, numpy.clip(self.viewPort.zoom * self.viewPort.zoom, 0.0, 1.0))
            glBegin(GL_LINES)
            for x in range(10):
                glVertex3f(x * 170, 0, 0)
                glVertex3f(x * 170, self.viewPort.height, 0)

            for y in range(10):
                glVertex3f(0, y * 80 , 0)
                glVertex3f(self.viewPort.width, y * 80, 0)
            
            glEnd()


        for node in reversed(self.nodes):
            node.draw(selected=(node is self.selectedNode))
        
        #for connection in self.connections:
        #    connection.draw()
            
        #if self.dragObject:
        #    self.dragObject.draw()

        if self.network_label:
            glColor4f(1, 1, 1, 0.25)
            self.renderText(10, 160, 0, self.network_label, QtGui.QFont("Helvetica", 120, 1, False))

    def addNode(self, node, x=0.0, y=0.0):
        node = FlowNode(self, node, self.viewPort)
        node.setPos(x, y)
        self.nodes.append(node)

    def selectNode(self, node):
        self.selectedNode = node
        self.updateGL()

    def pickKnob(self, x, y):
        return False
        #for node in self.nodes:
        #    for knob in node.knobs:
        #        if knob.isInShape(x,y):
        #            return knob
                    
    def pickNode(self, x, y):
        for node in self.nodes:
            if node.isInShape(x, y):
                self.selectedNode = node
                return node

        self.selectedNode = None

    def mousePressEvent(self, event):
        x, y =  event.x(), event.y() 
        self.pointer.x = x
        self.pointer.y = y
        if event.button() & QtCore.Qt.LeftButton:
            node = self.pickNode(x, y)
            if node:
                self.dragObject = self.DragObject(x, y, node)
                i = self.nodes.index(node)
                self.nodes[0], self.nodes[i] = self.nodes[i], self.nodes[0]
                self.selectNode(node)
                self.updateGL() # updateGL because z-order has changed
                return
            
            knob = self.pickKnob(x, y)
            if knob:
                self.dragObject = self.DragObject(x, y, knob)
                return
            
            else:
                self.panningMode = True
                pass

            self.selectNode(None)
                
        elif event.button() & QtCore.Qt.RightButton:
            knob = self.pickKnob(x, y)
            if knob:
                connections = list(self.findConnections(knob))
                if knob.type == FlowKnob.knobTypeOutput and len(connections) > 1:
                    if QtWidgets.QMessageBox.question(self.parent(), "Delete Connection", "Do you really want to delete all connections from this output?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.No:
                        return
                for connection in connections:
                    self.connections.remove(connection)
                    del connection
                self.updateGL()

    def contextMenuEvent(self, event):
        menu = QtGui.QMenu(parent=self.parent())
        
        x,y = event.x(), event.y()
        node = self.pickNode(x,y)
        if node:
            action = menu.addAction("Delete node")
            action.triggered.connect(functools.partial(self.deleteNode, node))
        elif self.pickKnob(x,y) is None:
            for i, func in enumerate(self.functions):
                if func not in self.outputFunctions:
                    action = menu.addAction(camelCaseToWords(func.__name__))
                    action.triggered.connect(functools.partial(self.addNode, func, x, y)) # lambda does not work in this case!! 
        menu.popup(event.globalPos())

    def wheelEvent(self,event):
        old_zoom = self.zoom
        counter_max = self.zoomWheelResolution * (self.zoomMax - .5) / 2
        self.zoomWheelCounter += event.delta() / 120.0
        self.zoomWheelCounter = numpy.clip(self.zoomWheelCounter, 0, counter_max)
        z = float(self.zoomWheelCounter) / float(self.zoomWheelResolution)
        zoom = numpy.clip(z * z, self.zoomMin, self.zoomMax)

        self.viewPort.zoom = zoom
        self.updateGL()

    def mouseDoubleClickEvent(self, event):
        x, y = event.x(), event.y()
        node = self.pickNode(x,y)
        if node:
            self.emit( QtCore.SIGNAL( "signalCopperNodeSelected( PyQt_PyObject )" ), node.path() )
            self.buildNodeGraph(node.path())

    def mouseReleaseEvent(self, event):
        if self.dragObject:
            try:
                self.dragObject.update(event.x(), event.y())
                self.dragObject.drop()
            finally:
                self.dragObject = None
                self.updateGL()
        else:
            self.panningMode = False

    def mouseMoveEvent(self, event):
        if self.dragObject:
            self.dragObject.update(event.x(), event.y())
            self.updateGL()
        elif self.panningMode:
            self.viewPort.pos_x += event.x() - self.viewPort.pos_x
            self.viewPort.pos_y += event.y() - self.viewPort.pos_y
            #self.resizeGL(self.viewPort.width, self.viewPort.height)
            self.updateGL()

    def keyPressEvent(self, event):
        self.parent().keyPressEvent(event)
