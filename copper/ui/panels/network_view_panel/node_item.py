import logging

from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *

import numpy
import copper
import math

#from copper import hou as engine
from copper.core.engine import signals as engine_signals
from copper.core.op.op_node import OP_Node
from copper.core.op.base import OpRegistry
from copper.ui.signals import signals


logger = logging.getLogger(__name__)


def next_greater_power_of_2(x):  
    return 2**(x-1).bit_length()


class NodeLinkItem(QtWidgets.QGraphicsItem):
    def __init__(self, socket_item_from = None, socket_item_to = None):
        QtWidgets.QGraphicsItem.__init__(self)

        self.setAcceptHoverEvents(True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        #self.setCacheMode(QtWidgets.QGraphicsItem.DeviceCoordinateCache)

        self._socket_item_from = socket_item_from
        self._socket_item_to = socket_item_to
        self._pos_from = None
        self._pos_to = None
        self._hovered = False

    def paint(self, painter, option, widget=None):
        if not self._hovered:
            pen = QtGui.QPen(Qt.Qt.black, 1.0)
        else:
            pen = QtGui.QPen(QtGui.QColor(255, 128, 16), 1.5);

        pen.setCosmetic(True)
        painter.setPen(pen)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

        painter.drawPath(self.buildPath());

    def buildPath(self) -> QtGui.QPainterPath:
        p = QtGui.QPainterPath()
        pos_to, pos_from = self._socket_item_to.scenePos(), self._socket_item_from.scenePos()
        p.moveTo(pos_from)

        dx = pos_to.x() - pos_from.x()
        dy = pos_to.y() - pos_from.y()

        ctr1 = QtCore.QPointF(pos_from.x() + dx * 0.25, pos_from.y() + dy * 0.1)
        ctr2 = QtCore.QPointF(pos_from.x() + dx * 0.75, pos_from.y() + dy * 0.9)

        p.cubicTo(ctr1, ctr2, pos_to)
        return p

    def shape(self):
        # TODO: make stroker width zoom independent
        stroker = QtGui.QPainterPathStroker()
        stroker.setWidth(1.0)
        return stroker.createStroke(self.buildPath())

    def boundingRect(self):
        return QtCore.QRectF(self._socket_item_from.scenePos(), self._socket_item_to.scenePos())

    def setFromSocketItem(self, socket_item):
        self._socket_item_from = socket_item

    def setToSocketItem(self, socket_item):
        self._socket_item_to = socket_item

    def setPosFrom(self, pos):
        self._pos_from = pos

    def setPosTo(self, pos):
        self._pos_to = pos

    def updatePos(self):
        if self._socket_item_from:
            self._pos_from = self._socket_item_from.pos()

        if self._socket_item_to:
            self._pos_to = self._socket_item_to.pos()

    def hoverEnterEvent(self, event):
        super(NodeLinkItem, self).hoverEnterEvent(event)
        self.prepareGeometryChange()
        self._hovered = True

    def hoverLeaveEvent(self, event):
        super(NodeLinkItem, self).hoverLeaveEvent(event)
        self.prepareGeometryChange()
        self._hovered = False


class NodeSocketItem(QtWidgets.QGraphicsItem):
    INPUT_SOCKET = 1
    OUTPUT_SOCKET = 2

    STACK_LEFT = 1
    STACK_RIGHT = 2
    STACK_TOP = 3
    STACK_BOTTOM = 4

    def __init__(self, parent, op_data_socket, socket_type=None, stack_side=STACK_TOP):
        QtWidgets.QGraphicsItem.__init__(self, parent)
        self.stack_side = stack_side
        self.node = parent.node
        self._link_items = []
        self._op_data_socket = op_data_socket
        self._socket_type = socket_type
        self.socket_color = QtGui.QColor(128, 128, 128)
        self.setAcceptHoverEvents(True)
        self.setZValue(self.parentItem().zValue() - 100)
        self.putInPlace()

        self.setCacheMode(QtWidgets.QGraphicsItem.DeviceCoordinateCache)


    def paint(self, painter, option, widget=None):
        # LOD here. Do not draw socket if the viewport scale factor is less than 0.5
        device_transfrom = 1.0 / painter.deviceTransform().m11()
        socket_rect = self.boundingRect()
        socket_outline_rect = self.boundingRect().adjusted(-device_transfrom, -device_transfrom, device_transfrom, device_transfrom)

        painter.fillRect(socket_outline_rect, QtGui.QColor(16, 16, 16))
        painter.fillRect(socket_rect, self.socket_color)

    def boundingRect(self):
        # LOD here. Do not draw socket if the viewport scale factor is less than 0.5
        socket_width = self.size().width()
        socket_height = self.size().height()
        return QtCore.QRectF(-socket_width/2, -socket_height/2, socket_width, socket_height)

    def size(self):
        if self.stack_side in [NodeSocketItem.STACK_TOP, NodeSocketItem.STACK_BOTTOM]:
            return QtCore.QSizeF(9, 2.25)
        else:
            return QtCore.QSizeF(2.25, 9)

    def opDataSocket(self):
        return self._op_data_socket

    def putInPlace(self):
        node_item = self.parentItem()
        parent_size = node_item.size()
        
        if self.stack_side in [NodeSocketItem.STACK_TOP, NodeSocketItem.STACK_BOTTOM]:
    
            if self.stack_side == NodeSocketItem.STACK_TOP:
                self.setPos(0, -(parent_size.height() / 2 + self.size().height() / 2))
            else:
                self.setPos(0, (parent_size.height() / 2 + self.size().height() / 2))

            # we need to place sockets once again so they accupy all the available space on the edge
            existing_sockets = node_item.inputSocketItems(self.stack_side)
            if existing_sockets:
                total_sockets_count = len(existing_sockets) + 1
                sockets_distance = node_item.size().width() / total_sockets_count
                socket_position = (sockets_distance / 2) - node_item.size().width() / 2

                for existing_socket in existing_sockets:
                    existing_socket.setX(socket_position)
                    socket_position += sockets_distance

                self.setX(socket_position)



        elif self.stack_side in [NodeSocketItem.STACK_LEFT, NodeSocketItem.STACK_RIGHT]:
            pass

from enum import Flag, auto

class NodeItem(QtWidgets.QGraphicsItem):
    class Display(Flag):
        CLEAN = 0
        FAILED = auto()

    def __init__(self, node):      
        QtWidgets.QGraphicsItem.__init__(self)
        self.node = node
        self._inputs = {NodeSocketItem.STACK_TOP: [], NodeSocketItem.STACK_LEFT: [], NodeSocketItem.STACK_RIGHT: [], NodeSocketItem.STACK_BOTTOM: []}
        self._outputs = {NodeSocketItem.STACK_TOP: [], NodeSocketItem.STACK_LEFT: [], NodeSocketItem.STACK_RIGHT: [], NodeSocketItem.STACK_BOTTOM: []}
        self._selected_indirect = False # this flag shows us that this node selected outside the widget
        self._display_flags = self.Display(self.Display.CLEAN)

        if self.node.iconName():
            self.icon = QtGui.QIcon(self.node.iconName())
        else:
            self.icon = None
        
        self.setAcceptHoverEvents(True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

        self.setCacheMode(QtWidgets.QGraphicsItem.DeviceCoordinateCache)

        # create input sockets
        for op_data_socket in self.node.inputDataSockets():
            socket_item = NodeSocketItem(self, op_data_socket, socket_type=NodeSocketItem.INPUT_SOCKET, stack_side=NodeSocketItem.STACK_TOP)
            self._inputs[NodeSocketItem.STACK_TOP].append(socket_item)

        # create output sockets
        for op_data_socket in self.node.outputDataSockets():
            socket_item = NodeSocketItem(self, op_data_socket, socket_type=NodeSocketItem.OUTPUT_SOCKET, stack_side=NodeSocketItem.STACK_BOTTOM)
            self._outputs[NodeSocketItem.STACK_BOTTOM].append(socket_item)

        # connect signals
        #self.node.signals.opCookingStarted.connect(self.nodeMarkClean)
        #self.node.signals.opCookingFailed.connect(self.nodeMarkFailed)

    def inputSocketItems(self, stack_side=None):
        if not stack_side:
            ''' return all input socket items '''
            return tuple([item for sublist in self._inputs.values() for item in sublist]) # used to flatten list of lists

        return tuple(self._inputs[stack_side])

    def outputSocketItems(self, stack_side=None):
        if not stack_side:
            ''' return all output socket items '''
            return tuple([item for sublist in self._outputs.values() for item in sublist]) # used to flatten list of lists

        return tuple(self._outputs[stack_side])

    def socketItems(self):
        '''
        return all available socket items
        '''
        return self.inputSocketItems() + self.outputSocketItems()

    def autoPlace(self):
        scene = self.scene()
        items_rect = scene.itemsBoundingRect()

        pos = self.node.position()
        if pos[0] is None or pos[1] is None:
            self.node.setPosition((items_rect.right() + 20, items_rect.bottom() + 20))

        self.setPos(self.node.position()[0], self.node.position()[1])

    def paint(self, painter, option, widget=None):
        device_scale_factor = 1.0 / painter.deviceTransform().m11()
        
        if painter.deviceTransform().m11() > 0.75:
            [socket.show() for socket in self.childItems()]
        else:
            [socket.hide() for socket in self.childItems()]

        pen = QtGui.QPen()
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)

        node_rect = self.boundingRect().adjusted(device_scale_factor, device_scale_factor, -device_scale_factor, -device_scale_factor)
        node_outline_rect = self.boundingRect()
        node_color = QtGui.QColor(160, 160, 160)
        if option.state & QtWidgets.QStyle.State_Selected:
            node_color = QtGui.QColor(196, 196, 196)
            # Draw selection border
            painter.fillPath(self.outlinePath(painter), QtGui.QBrush(QtGui.QColor(250, 190, 64)))

        # Draw node box itself
        painter.fillRect(node_outline_rect, QtGui.QColor(16, 16, 16))
        painter.fillRect(node_rect, node_color)

        # Draw error pattern if need
        if self.node.errors():
            error_brush = QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.BDiagPattern)
            matrix = error_brush.matrix()
            matrix.scale(device_scale_factor * 0.75, device_scale_factor * 0.75)
            error_brush.setMatrix(matrix)
            painter.fillRect(node_rect, error_brush)

        ## Paint icon if there is one
        icon_size = next_greater_power_of_2(int(max(min(8 / device_scale_factor, 64), 8)))
        if self.icon and icon_size > 8:
            pixmap = self.icon.pixmap(icon_size, icon_size)
            painter.drawPixmap(-3, -3, 6, 6, pixmap)

        font = painter.font()
        font.setPointSize(4)
        painter.setFont(font)
        painter.setPen(QtGui.QColor(192, 192, 192))
        painter.drawText(self.size().width() / 2 + 1, 1, self.node.name())

    def boundingRect(self):
        socket_width = self.size().width()
        socket_height = self.size().height()
        return QtCore.QRectF(-socket_width/2, -socket_height/2, socket_width, socket_height)

    def outlinePath(self, painter):
        device_transfrom = 1.0 / painter.deviceTransform().m11()
        border_width = 2.0 *device_transfrom
        path = QtGui.QPainterPath()
        path.addRect(self.boundingRect().adjusted(-border_width, -border_width, border_width, border_width))
        border_width = 3.0 *device_transfrom
        for child_item in self.childItems():
            if child_item.isVisible():
                child_path = QtGui.QPainterPath()
                child_rect = child_item.mapRectToParent(child_item.boundingRect()).adjusted(-border_width, -border_width, border_width, border_width)
                child_path.addRect(child_rect)
                path += child_path

        return path

    def size(self):
        return QtCore.QSizeF(38, 10)

    def select(self):
        ''' This method is used to select node when Network View panel recieves signal copperNodeSelected.
            We need this to avoid signals loop. Because copperNodeSelected signal was fired by other widget, 
            this copper node is already selected, so we need only update graphics item without sending signal
            again.
        '''
        self._selected_indirect = True
        for item in self.scene().selectedItems(): item.setSelected(False)
        self.setSelected(True)
        self._selected_indirect = False

    def inputConnections(self):
        return []

    def outputConnections(self):
        return []

    def itemChange(self, change, value, direct=True):
        ''' direct argument shows us that shit node wa selected inside the items scene. Otherwise don't propagate copperNodeSelected signal.
            Just change item state.
        '''
        if change == QtWidgets.QGraphicsItem.ItemSelectedChange:
            if value == True:
                # do stuff if selected
                if not self._selected_indirect:
                    engine_signals.nodeSelected[OP_Node].emit(self.node) 
            else:
                # do stuff if unselected
                pass

        elif change == QtWidgets.QGraphicsItem.ItemPositionChange:
            # snap to grid code here
            scene = self.scene()
            new_pos = value #QtCore.QPointF(value.toPointF()

            snapped_x = round((new_pos.x() / scene.gridSizeWidth)) * scene.gridSizeWidth
            snapped_y = round((new_pos.y() / scene.gridSizeHeight)) * scene.gridSizeHeight
            
            if abs(new_pos.x() - snapped_x) < 5: new_pos.setX(snapped_x)
            if abs(new_pos.y() - snapped_y) < 5: new_pos.setY(snapped_y)
            
            # move node itsef
            self.node.setPosition((new_pos.x(), new_pos.y()))

            value = QtCore.QVariant(new_pos)

        return super(NodeItem, self).itemChange(change, value)

    def contextMenuEvent(self, event):
        logger.debug("Context menu")

    @QtCore.pyqtSlot()   
    def nodeMarkClean(self):
        '''Marks node as claen (cooking stated, remove all error signs)'''
        #self._display_flags = self._display_flags
        pass

    @QtCore.pyqtSlot()   
    def nodeMarkFailed(self):
        '''Marks node as failed (has some errors)'''
        #self._display_flags |= Display.FAILED
        pass