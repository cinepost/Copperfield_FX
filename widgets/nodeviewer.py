from PyQt4 import QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *
import numpy
import compy
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
        self.selected = False
        self.knobs = []
        
        #if not self.isOutput():
        #    self.knobs.append(FlowKnob(self, FlowKnob.knobTypeOutput, "Output"))
        
        self.properties = {}

        if self.node:
            self.title = self.node.name()
        else:
            self.title = "untitled" 

        #if self.node:
        #    for parameter in signature.parameters.values():
        #        property = Property(name=parameter.name, type=parameter.annotation, value=parameter.default)
        #        
        #        if property.type == SynthParameters:
        #            property = property._replace(hasKnob=False, hasEditable=False)
        #        else:
        #            property = property._replace(hasKnob=property.type.hasKnob, hasEditable=property.type.hasEditable)
        #            
        #        if property.hasKnob:
        #            knob = FlowKnob(self, FlowKnob.knobTypeInput, property.name, self.getInputKnobCount())
        #            self.knobs.append(knob)
        #            property = property._replace(knob=knob)
        #        
        #        self.properties[parameter.name] = property
             
    def path(self):
        return self.node.path()

    def setPos(self, x=20, y=20):
        if self.node:
            self.node.setPos(x, y)   

    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def draw(self, selected=False, zoom=1.0):
        textOffset = 3
        x = self.node.x_pos * zoom
        y = self.node.y_pos * zoom
        dw = x + self.node.width * zoom
        dh = y + self.node.height * zoom

        # node shadow
        if self.selected:
            glColor4f(1.0, 0.7, 0.1, 1.0)
            glRectf(x - 2.0, y - 2.0, dw + 2.0, dh + 2.0)
        else:
            glColor4f(0.0, 0.0, 0.0, 0.5)
            glRectf(x - 1.0, y - 1.0, dw + 1.0, dh + 1.0)
        
        # node border
        glColor4f(0.5, 0.5, 0.5, 1.0)
        glRectf(x, y, dw, dh)
        
        # node
        if self.selected:
            glColor4f(0.6, 0.6, 0.6, 1.0)
        else:
            glColor4f(0.5, 0.5, 0.5, 1.0)
        glRectf(x + 1.0, y + 1.0, dw - 1.0, dh - 1.0)
        
        for knob in self.knobs:
            knob.draw(textOffset=textOffset)
        
        glColor4f(0.85, 0.85, 0.85, 1.0)
        #self.nodeFont.setBold(True)
        self.parent().renderText(x + textOffset, y - (self.fontLineHeight)/2, self.title) # works only if parent is qglWidget ;)
        #self.nodeFont.setBold(False)

    def isInShape(self, xpos, ypos, zoom=1.0):
        x = self.node.x_pos * zoom
        y = self.node.y_pos * zoom
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

class NodeEditorWidget(QtGui.QWidget):
    def __init__(self, parent, engine):      
        super(NodeEditorWidget, self).__init__(parent)
        self.engine = engine
        self.initUI()
        
    def initUI(self):
        vbox = QtGui.QVBoxLayout(self)

        path = QtGui.QLineEdit("/")
        node_editor = NodeEditorWorkareaWidget(self, self.engine)

        vbox.addWidget(path)
        vbox.addWidget(node_editor)
        
        self.setLayout(vbox)

class NodeEditorWorkareaWidget(QtOpenGL.QGLWidget):
    
    dragModeDraggingEmpty = 0
    dragModeDraggingNode = 1
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

        self.engine = engine
        self.setMinimumWidth(1280)
        self.setMinimumHeight(360)
        self.zoom = 1.0
        self.zoomWheelResolution = 12.0
        self.zoomWheelCounter = self.zoomWheelResolution
        self.zoomMin = 0.05
        self.zoomMax = 5.0
        self.network_label = None
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.overlayFont = QtGui.QFont("Helvetica", 20, 100, False)

        #self.functions = functions
        #self.outputFunctions = outputFunctions
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
        
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, w, h, 0)
        
    def paintGL(self):
        glClearColor(0.12, 0.12, 0.12, 1.0)
        glClear(GL.GL_COLOR_BUFFER_BIT)

        for node in reversed(self.nodes):
            node.draw(selected=(node is self.selectedNode), zoom=self.zoom)
        
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
        for node in self.nodes:
            for knob in node.knobs:
                if knob.isInShape(x,y):
                    return knob
                    
    def pickNode(self, x, y):
        for node in self.nodes:
            if node.isInShape(x,y, zoom=self.zoom):
                for n in self.nodes:
                    n.unselect()

                node.select()
                return node

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
        menu = QtWidgets.QMenu(parent=self.parent())
        
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
        self.buildNodeGraph(node.path())

    def mouseReleaseEvent(self, event):
        if self.dragObject:
            try:
                self.dragObject.update(event.x(), event.y())
                self.dragObject.drop()
            finally:
                self.dragObject = None
                self.updateGL()

    def mouseMoveEvent(self, event):
        if self.dragObject:
            self.dragObject.update(event.x(), event.y())
            self.updateGL()

    def keyPressEvent(self, event):
        self.parent().keyPressEvent(event)
