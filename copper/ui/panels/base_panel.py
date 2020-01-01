import uuid
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from functools import wraps
import six
import inspect

from copper.core.op.op_node import OP_Node
from copper.core.engine import signals as engine_signals
from copper.ui.widgets import PathBarWidget
import copper.ui.signals as ui_signals
from copper.ui.signals import Signals
from .panel_registry import PanelRegistry

class Overlay(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.Qt.WA_TransparentForMouseEvents, True)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground, True)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self) #self.viewport()
        painter.fillRect(self.rect(), QtGui.QColor(80, 80, 255, 128));


class OverlayFilter(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self._overlay = None

    def eventFilter(self, view,  event):
        etype = event.type()
        if etype == QtCore.QEvent.DragEnter:
            if not self._overlay:
                self._overlay = Overlay()
                self._overlay.setParent(view)
                self._overlay.resize(view.size())
            
            self._overlay.show()

        elif etype in [QtCore.QEvent.DragLeave, QtCore.QEvent.Drop]:
            if self._overlay:
                self._overlay.hide()
        
        elif etype == QtCore.QEvent.Resize:
            if self._overlay and self._overlay.parent() == view:
                self._overlay.resize(view.size());

        return QtCore.QObject.eventFilter(self, view, event)


@six.add_metaclass(PanelRegistry)
class BasePanel(QtWidgets.QFrame):
    __base__ = True

    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self._signals = ui_signals
        self.panel_layout = QtWidgets.QVBoxLayout()
        self.panel_layout.setSpacing(0)
        self.panel_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.panel_layout)
        self.setObjectName("pane")

    @classmethod
    def signals(cls):
        return cls._signals

    def copyPanel(self):
        '''
        This method is used for copying panels and maintain all the setting and variables.
        Should be reimplemented by inhereted panel type
        '''
        return self.__class__()

    @classmethod
    def panelTypeName(cls):
        '''
        This method is used to get panel type name and display it as window title or tab title
        '''
        raise NotImplementedError

    @classmethod
    def hasNetworkControls(cls):
        '''
        This method is used to determine particular panel type implements network navigation control aka path bar
        '''
        return False

    def nodeSelected(self, node_path = None):
        raise NotImplementedError

    def addLayout(self, layout):
        self.panel_layout.addLayout(layout)

    def addWidget(self, widget):
        self.panel_layout.addWidget(widget)


class PathBasedPaneTabSignals(Signals):
    nodeDropped = QtCore.pyqtSignal(uuid.UUID)
    nodeDropped = QtCore.pyqtSignal(OP_Node)

    def __init__(self):  
        Signals.__init__(self)


class PathBasedPaneTab(BasePanel):
    __base__ = True

    def __init__(self, network_controls=False, accept_drops=False):
        BasePanel.__init__(self)
        if accept_drops:
            self._overlay_filter = OverlayFilter()
            self.setAcceptDrops(True)
            self.installEventFilter(self._overlay_filter)

        self.pinned = None
        self.node = None
        self._signals = PathBasedPaneTabSignals() # copy of signals, because gui.signals.signals is a singleton
        self.path_bar_widget = PathBarWidget(self, self)
        self.panel_layout.addWidget(self.path_bar_widget)

        # connect signals
        self.path_bar_widget.signals.pinPressed.connect(self.togglePin)

        # engine signals
        engine_signals.nodeSelected.connect(self.copperNodeSelected)
        engine_signals.nodeCreated.connect(self.copperNodeCreated)
        engine_signals.nodeModified.connect(self.copperNodeModified)

        # connect global gui signals
        ui_signals.signals.copperSetCompositeViewNode.connect(self.copperSetCompositeViewNode)

    @classmethod
    def hasNetworkControls(cls):
        '''
        This method is used to determine particular panel type implements network navigation control aka path bar
        '''
        return True

    @property
    def signals(self):
        '''
        This method returns signals for use in subclassed panels. It substitutes standard gui signals with it's own. They intercept signals coming from gui and forward
        them only when panel unpinned.
        '''
        return self._signals

    def getNetworkControlsWidget(self):
        '''
        This method is used by UI to get control of network_controls_widget (whether it path bar or anything else) to hide and unhide it. Just mimiking dad's beheavior
        '''
        return self.path_bar_widget


    def setPin(self, pin):
        self.pinned = pin

    def isPin(self):
        return self.pinned

    def currentNode(self):
        return self.node

    def setCurrentNode(self, node, pick_node = True):
        self.node = node
        if pick_node:
            # TODO: send signal to pick node
            pass

    @QtCore.pyqtSlot()
    def togglePin(self):
        self.pinned = not self.pinned

    @QtCore.pyqtSlot(OP_Node)
    def copperNodeSelected(self, node):
        if not self.isPin():
            self.signals.copperNodeSelected[OP_Node].emit(node)

    @QtCore.pyqtSlot(OP_Node)
    def copperNodeCreated(self, node):
        if not self.isPin():
            self.signals.copperNodeCreated[OP_Node].emit(node)

    @QtCore.pyqtSlot(OP_Node)
    def copperSetCompositeViewNode(self, node):
        if not self.isPin():
            self.signals.copperSetCompositeViewNode[OP_Node].emit(node)

    @QtCore.pyqtSlot(OP_Node)
    def copperNodeModified(self, node):
        if not self.isPin():
            self.signals.copperNodeModified[OP_Node].emit(node)

    def dragEnterEvent(self, event):
        from copper import hou
        if event.mimeData().hasFormat("node/type"):
            node_type = event.mimeData().nodeType()
            if node_type.category().name() == "Cop2":
                event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        pass

    def dropEvent(self, event):
        if event.mimeData().hasFormat("node/path"):
            if not self.isPin():
                from copper import hou
                node_path = event.mimeData().nodePath()
                node = hou.node(node_path)
                self.setCurrentNode(node, pick_node=False)
                self.signals.nodeDropped.emit(node)
            
            event.acceptProposedAction()
