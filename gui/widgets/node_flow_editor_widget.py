from PyQt4 import QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

from path_bar_widget import PathBarWidget

import numpy
import copper
import math 

class NodeItem(QtGui.QGraphicsItem):
    def __init__(self, parent=None, scene=None):      
        QtGui.QGraphicsItem.__init__(self, parent, scene) 
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)

    def paint(self, painter, option, widget=None):
        pen = QtGui.QPen()
        pen.setCosmetic(True)

        if option.state == QtGui.QStyle.State_Selected:
            pen.setWidth(2)
            painter.fillRect(QtCore.QRectF(-20,-10,40,10), QtGui.QColor(196, 196, 196))
            painter.setPen(QtGui.QColor(250, 250, 128))
            painter.drawRect(-20,-10,40,10)
        else:
            pen.setWidth(1)
            painter.fillRect(QtCore.QRectF(-20,-10,40,10), QtGui.QColor(160, 160, 160))
            painter.setPen(QtGui.QColor(128, 128, 128))
            painter.drawRect(-20,-10,40,10)


        painter.setPen(QtGui.QColor(128, 128, 128))
        painter.drawText(24, 0, "Nodename1")

    def boundingRect(self):
        return QtCore.QRectF(-20,-10,40,10)


    def itemChange(self, change, value):
        if change == QtGui.QGraphicsItem.ItemSelectedChange:
            print "Node selection changed"
            if value == True:
                # do stuff if selected
                pass
            else:
                # do stuff if not selected
                pass

        elif change == QtGui.QGraphicsItem.ItemPositionChange:
            # snap to grid code here
            pass

        return QtGui.QGraphicsItem.itemChange(self, change, value)


class NodeFlowScene(QtGui.QGraphicsScene):
    gridSizeWidth = 180
    gridSizeHeight = 80 
    scaleSize = 1.0
    def __init__(self, parent=None, engine=None):      
        QtGui.QGraphicsScene.__init__(self, parent) 
        self.initUI()

    def initUI(self):
        self.setSceneRect(-100000,-100000,200000,200000)
        
        # Test node
        node = NodeItem()
        node.setSelected(True)
        self.addItem(node)
        

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
    def __init__(self, parent=None, engine=None):      
        QtGui.QGraphicsView.__init__(self, parent) 
        self.engine = engine
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
        self.setDragMode( QtGui.QGraphicsView.RubberBandDrag )
        #self.setDragMode( QtGui.QGraphicsView.ScrollHandDrag )

    def copy(self):
        return NodeFlowEditorWidget(None, engine=self.engine)

    @classmethod
    def panelTypeName(cls):
        return "Network View"

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

