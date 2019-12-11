import logging

from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import numpy
import copper
import math

from copper import hou as engine
from copper.op.base import OpRegistry
from gui.signals import signals


from .node_item import NodeItem

logger = logging.getLogger(__name__)


class NodeFlowScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):      
        QtWidgets.QGraphicsScene.__init__(self, parent) 
        self.nodes_map = {}

        self.gridSizeWidth = 60
        self.gridSizeHeight = 30 
        self.zoomLevel = 1.0
        self.setSceneRect(-100000, -100000, 200000, 200000)

    @QtCore.pyqtSlot()
    def addNode(self, node_path=None):
        if node_path:
            node = engine.node(node_path)
            if node:
                node_item= NodeItem(node)
                self.addItem(node_item)
                self.nodes_map[node_path] = node_item
                node_item.autoPlace()

    def buildNetworkLevel(self, node_path=None):
        node = engine.node(node_path)
        if node:
            self.network_level = node_path
            self.nodes_map = {}
            self.clear()

            # build node boxes
            for child in node.children():
                self.addNode(child.path())

            # build links

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


    def selectNode(self, node_path):
        if node_path not in self.nodes_map:
            # If node is not in map we need to rebuild visual network
            self.buildNetworkLevel(engine.node(node_path).parent().path())

        # highlight selected node
        self.nodes_map[node_path].select()

    def contextMenuEvent(self, event):
        network_node = engine.node(self.network_level)

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
        network_node.createNode(action.data().toPyObject())
