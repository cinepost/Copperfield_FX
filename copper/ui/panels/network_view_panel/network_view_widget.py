import logging
from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt

from copper import hou
from copper.core.op.op_node import OP_Node

from .node_flow_scene import NodeFlowScene

logger = logging.getLogger(__name__)


class NetworkViewWidget(QtWidgets.QGraphicsView):
    def __init__(self, parent, panel):  
        QtWidgets.QGraphicsView.__init__(self, parent)
        self.panel = panel
        self.setObjectName("network_widget")

        self.scene = NodeFlowScene(self)
        self.setScene(self.scene)
        self.setMouseTracking(True)
        self.setInteractive(True) 

        self.setSizePolicy(QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding))

        ## No need to see scroll bars in flow editor
        self.setHorizontalScrollBarPolicy ( QtCore.Qt.ScrollBarAlwaysOff )
        self.setVerticalScrollBarPolicy ( QtCore.Qt.ScrollBarAlwaysOff )

        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)
        self.setViewport( QtOpenGL.QGLWidget(format) ) # Force OpenGL rendering mode.
        self.setViewportUpdateMode( QtWidgets.QGraphicsView.FullViewportUpdate )
        self.setDragMode( QtWidgets.QGraphicsView.RubberBandDrag )

        ## As a debug we always set new panel widget to current node
        self.setNetworkLevel(hou.pwd())

        ## Connect panel signals
        self.panel.signals.copperNodeCreated[OP_Node].connect(self.copperNodeCreated)
        self.panel.signals.copperNodeSelected[OP_Node].connect(self.copperNodeSelected)

    def sizeHint(self):
        return QtCore.QSize(200, 200)

    @QtCore.pyqtSlot(OP_Node)
    def copperNodeCreated(self, node):
        if self.scene.network_level == node.parent():
            self.scene.addNode(node)

    @QtCore.pyqtSlot(OP_Node)
    def copperNodeSelected(self, node):
        self.scene.selectNode(node)

    def setNetworkLevel(self, node):
        self.scene.buildNetworkLevel(node)

    def wheelEvent(self, event):
         # Zoom Factor
        zoomInFactor = 1.05
        zoomOutFactor = 1 / zoomInFactor

        # Set Anchors
        self.setTransformationAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)

        # Save the scene pos
        oldPos = self.mapToScene(event.pos())

        # Zoom
        if event.angleDelta().y() > 0:
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

    def mouseDoubleClickEvent(self, event):
        picked_item = self.itemAt(event.pos())
        if picked_item:
            self.scene.buildNetworkLevel(picked_item.node)

    def keyPressEvent(self, event):
        if event.modifiers() == QtCore.Qt.AltModifier:
            self.setInteractive(False)
            self.setDragMode( QtWidgets.QGraphicsView.ScrollHandDrag )

    def keyReleaseEvent(self, event):
        self.setInteractive(True)
        self.setDragMode( QtWidgets.QGraphicsView.RubberBandDrag )

    def mouseMoveEvent(self, event):
        super(NetworkViewWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        # Bring picked items to front
        picked_item = self.itemAt(event.pos())
        if picked_item:
            for item in self.items():
                item.setZValue(0)

            picked_item.setZValue(1)

        super(NetworkViewWidget, self).mousePressEvent(event) # propogate event to items
