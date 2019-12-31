import logging

from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import numpy
import copper
import math

from copper import hou
from copper.core.op.base import OpRegistry
from copper.ui.signals import signals


from .node_item import NodeItem, NodeLinkItem

logger = logging.getLogger(__name__)


class NodeFlowScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):      
        QtWidgets.QGraphicsScene.__init__(self, parent) 
        self.nodes_map = {}
        self.sockets_map = {}
        self.network_level = None

        self.gridSizeWidth = 60
        self.gridSizeHeight = 30 
        self.zoomLevel = 1.0
        self.setSceneRect(-100000, -100000, 200000, 200000)

        self.buildNetworkLevel(hou.pwd())

    @QtCore.pyqtSlot()
    def addNode(self, node):
        node_item = NodeItem(node)
        self.addItem(node_item)
        self.nodes_map[node.id()] = node_item
        for socket_item in node_item.socketItems():
            self.sockets_map[socket_item.opDataSocket().id()] = socket_item

        node_item.autoPlace()

    def buildNetworkLevel(self, node):
        self.network_level = node
        self.nodes_map = {}
        self.clear()

        # build node boxes
        for child in node.children():
            self.addNode(child)

        # build links
        for node_item in self.nodes_map.values():
            for connection in node_item.node.inputConnections():
                socket_from = self.sockets_map[connection.inputDataSocket().id()]
                socket_to = self.sockets_map[connection.outputDataSocket().id()]
                link_item = NodeLinkItem(socket_from, socket_to)
                self.addItem(link_item)

    def zoom(self, zoomFactor):
        self.zoomLevel *= zoomFactor

    def drawBackground(self, painter, rect):
        painter.fillRect(rect, QtGui.QColor(42, 42, 42))

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

    def drawForeground(self, painter, rect):
        #painter.drawText(rect, "Network type name")
        pass


    def selectNode(self, node):
        if node.id() not in self.nodes_map:
            # If node is not in map we need to rebuild visual network
            self.buildNetworkLevel(node.parent())

        # highlight selected node
        self.nodes_map[node.id()].select()

    def mouseMoveEvent(self, event):
        super(NodeFlowScene, self).mouseMoveEvent(event)

    def contextMenuEvent(self, event):
        network_node = self.network_level

        menu = QtWidgets.QMenu(event.widget())
        group = QtWidgets.QActionGroup(menu)
        menu.addAction('Tool Menu...')

        add_operators_menu = menu.addMenu("Add")

        node_types = network_node.childTypeCategory().nodeTypes()
        for node_type_name, node_class in node_types.items():
            icon = QtGui.QIcon(node_class.iconName())
            action = add_operators_menu.addAction(icon, node_type_name)
            action.setActionGroup(group)
            action.setData(node_type_name)
        
        group.triggered.connect(self.addOperator)

        menu.exec_(event.screenPos())

    def addOperator(self, action):
        network_node = engine.node(self.network_level)
        network_node.createNode(action.data())
