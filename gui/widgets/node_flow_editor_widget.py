from PyQt4 import QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

from path_bar_widget import PathBarWidget

import numpy
import copper
import math 

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

    def __init__(self, node, parent=None):
        QtCore.QObject.__init__(self, parent)
        self.fontLineHeight = 8
        self.node = node
        self.inputs = []
        
        self.properties = {}

        if self.node:
            self.title = self.node.name()
        else:
            self.title = "untitled" 
             
    def path(self):
        return self.node.path()

    def setPos(self, x=20, y=20):
        if self.node:
            self.node.setPos(x, y)   

    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def draw(self, selected=False, offset=(0,0), zoom=1.0):
        x1 = self.node.x_pos * zoom + offset[0]
        y1 = self.node.y_pos * zoom + offset[1]
        width = self.node.width * zoom
        height = self.node.height * zoom
        x2 = x1 + width
        y2 = y1 + height

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
        if zoom > 0.2:
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
        self.parent().renderText(x2 + 4, y2 - height / 2.0, self.title) # works only if parent is qglWidget ;)
        #self.nodeFont.setBold(False)

    def isInShape(self, xpos, ypos, offset=(0,0), zoom=1.0):
        x = self.node.x_pos * zoom + offset[0]
        y = self.node.y_pos * zoom + offset[1]
        dw = x + self.node.width * zoom
        dh = y + self.node.height * zoom
        return x <= xpos <= dw and y <= ypos <= dh
        
    def startDrag(self, dragObject):
        dragObject.custom = (dragObject.startX - self.node.x_pos, dragObject.startY - self.node.y_pos)
        
    def updateDrag(self, dragObject):
        self.node.x_pos = dragObject.x - dragObject.custom[0]
        self.node.y_pos = dragObject.y - dragObject.custom[1]

    def drawDrag(self, dragObject):
        pass

    def __str__(self):
        return "FlowNode '%s'" % self.title
        
    def __repr__(self):
        return "<FlowNode '%s'>" % self.title

class NodeFlowEditorWidget(QtGui.QWidget):
    def __init__(self, parent, engine):      
        super(NodeFlowEditorWidget, self).__init__(parent)
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

class NodeEditorWorkareaWidget(QtOpenGL.QGLWidget):
    
    dragModeDraggingEmpty = 0
    dragModeDraggingNode = 1
    dragModeDraggingOrigin = 4 # workarea dragging/panning mode
    dragModeDraggingConnectionInToOut = 2
    dragModeDraggingConnectionOutToIn = 3
    
    class DragObject:
        def __init__(self, startX, startY, draggable, zoom):
            self.startX = startX / zoom
            self.startY = startY / zoom
            self.zoom = zoom
            self.draggable = draggable
            self.custom = None
            self.x = startX
            self.y = startY
            self.draggable.startDrag(self)
            
        def update(self, currentX, currentY):
            self.x = currentX / self.zoom
            self.y = currentY / self.zoom
            self.draggable.updateDrag(self)
            
        def drop(self):
            self.draggable.dropDrag(self)
            
        def draw(self):
            self.draggable.drawDrag(self)

    def __init__(self, parent, engine, path="/"):
        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)
        QtOpenGL.QGLWidget.__init__(self, format, parent)
        if not self.isValid():
            raise OSError("OpenGL not supported.")

        self.origin_x = 0.0
        self.origin_y = 0.0
        self.panningMode = False
        self.engine = engine
        self.zoom = 1.0
        self.zoomWheelResolution = 12.0
        self.zoomWheelCounter = self.zoomWheelResolution
        self.zoomMin = 0.05
        self.zoomMax = 5.0
        self.network_label = None
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        #self.overlayFont = QtGui.QFont("Helvetica", 20, 100, False)

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
        dx = 130
        dy = 50
        for node in self.engine.node(path).children():
            self.addNode(node, dx * i, dy * i)
            i += 1

        self.updateGL()

    def initializeGL(self):
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_BLEND)
        
    def resizeGL(self, w, h):
        self.work_area_width = w
        self.work_area_height = h
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, w, h, 0)
        glViewport(0, 0, w, h)
        
    def paintGL(self):
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glClearColor(0.12, 0.12, 0.12, 1.0)
        glClear(GL.GL_COLOR_BUFFER_BIT)

        # draw grid
        if self.zoom > 0.1:
            glColor4f(0.2, 0.24, 0.30, numpy.clip(self.zoom * self.zoom, 0.0, 1.0))
            glBegin(GL_LINES)
            for x in range(10):
                glVertex3f(x * 170 * self.zoom + self.origin_x, 0, 0)
                glVertex3f(x * 170 * self.zoom + self.origin_x, self.work_area_height, 0)

            for y in range(10):
                glVertex3f(0, y * 80 * self.zoom + self.origin_y, 0)
                glVertex3f(self.work_area_width, y * 80 * self.zoom + self.origin_y, 0)
            
            glEnd()


        for node in reversed(self.nodes):
            node.draw(selected=(node is self.selectedNode), offset=(self.origin_x, self.origin_y), zoom=self.zoom)
        
        #for connection in self.connections:
        #    connection.draw()
            
        #if self.dragObject:
        #    self.dragObject.draw()

        if self.network_label:
            glColor4f(1, 1, 1, 0.25)
            self.renderText(10, 160, 0, self.network_label, QtGui.QFont("Helvetica", 120, 1, False))

    def addNode(self, node, x, y):
        node = FlowNode(node, self)
        node.setPos(x, y)
        self.nodes.append(node)
        #self.selectNode(node)

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
            if node.isInShape(x, y, offset=(self.origin_x, self.origin_y), zoom=self.zoom):
                self.selectedNode = node
                return node

        self.selectedNode = None

    def mousePressEvent(self, event):
        x, y = event.x(), event.y() 
        if event.button() & QtCore.Qt.LeftButton:
            node = self.pickNode(x,y)
            if node:
                self.dragObject = self.DragObject(x, y, node, self.zoom)
                i = self.nodes.index(node)
                self.nodes[0], self.nodes[i] = self.nodes[i], self.nodes[0]
                self.selectNode(node)
                self.updateGL() # updateGL because z-order has changed
                return
            
            knob = self.pickKnob(x,y)
            if knob:
                self.dragObject = self.DragObject(x, y, knob, self.zoom)
                return
            
            else:
                self.panningMode = True
                pass

            self.selectNode(None)
                
        elif event.button() & QtCore.Qt.RightButton:
            knob = self.pickKnob(x,y)
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
        counter_max = self.zoomWheelResolution * (self.zoomMax - .5) / 2
        self.zoomWheelCounter += event.delta() / 120.0
        self.zoomWheelCounter = numpy.clip(self.zoomWheelCounter, 0, counter_max)
        z = float(self.zoomWheelCounter) / float(self.zoomWheelResolution)
        self.zoom = numpy.clip(z * z, self.zoomMin, self.zoomMax)
        self.updateGL()

    def mouseDoubleClickEvent(self, event):
        x, y = event.x(), event.y()
        node = self.pickNode(x,y)
        if node:
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
            self.origin_x = event.x()
            self.origin_y = event.y()
            self.updateGL()

    def keyPressEvent(self, event):
        self.parent().keyPressEvent(event)
