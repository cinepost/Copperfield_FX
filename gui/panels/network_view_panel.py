from PyQt4 import QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import numpy
import copper
import math

from copper import engine
from gui.signals import signals
from gui.widgets import PathBarWidget, CollapsableWidget
from base_panel import BasePanel

class NetworkViewPanel(BasePanel):
    def __init__(self):  
        BasePanel.__init__(self, network_controls = True) 

        self.network_view_widget = NetworkViewWidget(self)
        self.network_view_controls = NetworkViewControls(self)

        self.addWidget(self.network_view_controls)
        self.addWidget(self.network_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Network View"

    def nodeSelected(self, node_path = None):
        pass


class NetworkViewControls(CollapsableWidget):
    def __init__(self, parent=None):
        CollapsableWidget.__init__(self, parent)

        self.addWidget(QtGui.QLabel("huypizda"))

class NodeItem(QtGui.QGraphicsItem):
    def __init__(self, node):      
        QtGui.QGraphicsItem.__init__(self)
        self.node = node
             
        if self.node.iconName():
            self.icon = QtGui.QIcon(self.node.iconName())
        else:
            self.icon = None

        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)

    def autoPlace(self):
        scene = self.scene()
        items_rect = scene.itemsBoundingRect()

        if self.node.pos_x is None or self.node.pos_y is None:
            self.node.pos_x = items_rect.right() + 20
            self.node.pos_y = items_rect.bottom() + 20

        self.setPos(self.node.pos_x, self.node.pos_y)

    def paint(self, painter, option, widget=None):
        pen = QtGui.QPen()
        pen.setCosmetic(True)

        if option.state & QtGui.QStyle.State_Selected:
            pen.setWidth(3)
            painter.fillRect(QtCore.QRectF(-20,-5,40,10), QtGui.QColor(196, 196, 196))
            painter.setPen(QtGui.QColor(250, 200, 128))
            painter.drawRect(-20,-5,40,10)
        else:
            pen.setWidth(1)
            painter.fillRect(QtCore.QRectF(-20,-5,40,10), QtGui.QColor(160, 160, 160))
            painter.setPen(QtGui.QColor(128, 128, 128))
            painter.drawRect(-20,-5,40,10)

        ## Paint icon if there is one
        if self.icon:
            painter.drawPixmap(-4, -4, 8, 8, self.icon.pixmap(QtCore.QSize(64,64)));
            #self.icon.paint(painter, QtCore.QRect(-8,-8,8,8))

        painter.setPen(QtGui.QColor(128, 128, 128))
        painter.drawText(24, 0, self.node.name())

    def boundingRect(self):
        return QtCore.QRectF(-20,-5,40,10)


    def itemChange(self, change, value):
        if change == QtGui.QGraphicsItem.ItemSelectedChange:
            if value == True:
                # do stuff if selected
                signals.copperNodeSelected[str].emit(self.node.path()) 
            else:
                # do stuff if not selected
                pass

        elif change == QtGui.QGraphicsItem.ItemPositionChange:
            # snap to grid code here
            print "Item moved"

        return QtGui.QGraphicsItem.itemChange(self, change, value)


class NodeFlowScene(QtGui.QGraphicsScene):
    def __init__(self, parent=None):      
        QtGui.QGraphicsScene.__init__(self, parent) 
        self.gridSizeWidth = 180
        self.gridSizeHeight = 80 
        self.zoomLevel = 1.0

        self.setSceneRect(-100000, -100000, 200000, 200000)

    @QtCore.pyqtSlot()
    def addNode(self, node_path=None):
        if node_path:
            node = engine.node(node_path)
            if node:
                node_item= NodeItem(node)
                self.addItem(node_item)
                node_item.autoPlace()

    def buildNetworkLevel(self, node_path=None):
        node = engine.node(node_path)
        if node:
            self.clear()
            for child in node.children():
                self.addNode(child.path())

    def zoom(self, zoomFactor):
        self.zoomLevel *= zoomFactor

    def drawBackground(self, painter, rect):
        painter.fillRect(rect, QtGui.QColor(48, 48, 48))

        if self.zoomLevel > 0.1:
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

    def mouseDoubleClickEvent(self, event):
        picked_item = self.itemAt(event.scenePos())
        self.buildNetworkLevel(picked_item.node)


class NetworkViewWidget(QtGui.QGraphicsView):
    def __init__(self, parent=None):  
        QtGui.QGraphicsView.__init__(self, parent)

        self.setObjectName("network_widget")

        self.network_level = "/"

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

        ## As a debug we always set new panel widget to "/"
        self.setNetworkLevel("/obj")


        ## Connect engine signals
        signals.copperNodeCreated[str].connect(self.copperNodeCreated)

    @QtCore.pyqtSlot(str)
    def copperNodeCreated(self, node_path):
        print "Network View node created %s" % node_path
        node = engine.node(str(node_path))
        if node:
            if self.network_level == node.parent().path():
                self.scene.addNode(str(node_path))

    def setNetworkLevel(self, node_path):
        self.network_level = node_path
        self.scene.buildNetworkLevel(node_path)

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



