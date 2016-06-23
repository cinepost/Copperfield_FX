from PyQt4 import QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import numpy
import copper
import math

from gui.widgets import PathBarWidget
from base_panel import BasePanel

class NetworkViewPanel(BasePanel):
    def __init__(self, parent=None, engine=None):  
        BasePanel.__init__(self, parent) 
        self.initUI()

    def initUI(self):
        self.path_bar_widget = PathBarWidget(self)
        self.network_view_widget = NetworkViewWidget(self)

        self.setNetworkControlsWidget(self.path_bar_widget)
        self.addWidget(self.network_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Network View"

    @classmethod
    def hasNetworkControls(cls):
        return True

class NodeItem(QtGui.QGraphicsItem):
    def __init__(self, parent=None, scene=None):      
        QtGui.QGraphicsItem.__init__(self, parent, scene) 
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)

    def paint(self, painter, option, widget=None):
        pen = QtGui.QPen()
        pen.setCosmetic(True)

        if option.state & QtGui.QStyle.State_Selected:
            pen.setWidth(3)
            painter.fillRect(QtCore.QRectF(-20,-10,40,10), QtGui.QColor(196, 196, 196))
            painter.setPen(QtGui.QColor(250, 200, 128))
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
            if value == True:
                # do stuff if selected
                pass
            else:
                # do stuff if not selected
                pass

        elif change == QtGui.QGraphicsItem.ItemPositionChange:
            # snap to grid code here
            print "Item moved"

        return QtGui.QGraphicsItem.itemChange(self, change, value)


class NodeFlowScene(QtGui.QGraphicsScene):
    def __init__(self, parent=None, engine=None):      
        QtGui.QGraphicsScene.__init__(self, parent) 
        self.gridSizeWidth = 180
        self.gridSizeHeight = 80 
        self.zoomLevel = 1.0
        self.initUI()

    def initUI(self):
        self.setSceneRect(-100000, -100000, 200000, 200000)
        
        # Test node
        self.addNode()
        self.addNode()

    def addNode(self):
        node = NodeItem()
        self.addItem(node)

    def zoom(self, zoomFactor):
        self.zoomLevel *= zoomFactor

    def drawBackground(self, painter, rect):
        if self.zoomLevel < 0.1:
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

    def mousePressEvent(self, event):
        picked_item = self.itemAt(event.scenePos())

        # Bring picked items to front
        if picked_item:
            for item in self.items():
                item.setZValue(0)

            picked_item.setZValue(1)

        super(NodeFlowScene, self).mousePressEvent(event) # propogate event to items

class NetworkViewWidget(QtGui.QGraphicsView):
    def __init__(self, parent=None, engine=None):  
        QtGui.QGraphicsView.__init__(self, parent) 
        self.initUI()

    def initUI(self):
        self.scene = NodeFlowScene(self)
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
        self.scene.zoom(zoomFactor) # This is used by scene view to determine current viewport zoom

        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())

    def keyPressEvent(self, event):
        if event.modifiers() == QtCore.Qt.AltModifier:
            self.setInteractive(False)
            self.setDragMode( QtGui.QGraphicsView.ScrollHandDrag )

    def keyReleaseEvent(self, event):
        self.setInteractive(True)
        self.setDragMode( QtGui.QGraphicsView.RubberBandDrag )



