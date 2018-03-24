from PyQt5 import QtCore, QtGui, QtWidgets
from functools import wraps
import six
import inspect

from gui.widgets import PathBarWidget
import gui.signals
from .panel_registry import PanelRegistry

@six.add_metaclass(PanelRegistry)
class BasePanel(QtWidgets.QFrame):
    __base__ = True

    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.signals = gui.signals
        self.panel_layout = QtWidgets.QVBoxLayout()
        self.panel_layout.setSpacing(0)
        self.panel_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.panel_layout) 

    @classmethod
    def _signals(cls):
        return gui.signals

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


class NetworkPanel(BasePanel):
    __base__ = True

    def __init__(self, network_controls=False):
        BasePanel.__init__(self)
        self.signals = gui.signals.Signals() # copy of signals, because gui.signals.signals is a singleton
        self.path_bar_widget = PathBarWidget(self, self)
        self.panel_layout.addWidget(self.path_bar_widget)

        # connect global gui signals
        gui.signals.signals.copperNodeCreated.connect(self.copperNodeCreated)
        gui.signals.signals.copperNodeSelected.connect(self.copperNodeSelected)
        gui.signals.signals.copperSetCompositeViewNode.connect(self.copperSetCompositeViewNode)
        gui.signals.signals.copperNodeModified.connect(self.copperNodeModified)

    @classmethod
    def hasNetworkControls(cls):
        '''
        This method is used to determine particular panel type implements network navigation control aka path bar
        '''
        return True

    @classmethod
    def _signals(cls):
        '''
        This method returns signals for use in subclassed panels. It substitutes standard gui signals with it's own. They intercept signals coming from gui and forward
        them only when panel unpinned.
        '''
        return cls.signals

    def getNetworkControlsWidget(self):
        '''
        This method is used by UI to get control of network_controls_widget (whether it path bar or anything else) to hide and unhide it. Just mimiking dad's beheavior
        '''
        return self.path_bar_widget

    @QtCore.pyqtSlot(str)
    def copperNodeSelected(self, node_path = None):
        if not self.path_bar_widget.isPinned():
            self.signals.copperNodeSelected[str].emit(node_path)

    @QtCore.pyqtSlot(str)
    def copperNodeCreated(self, node_path = None):
        if not self.path_bar_widget.isPinned():
            self.signals.copperNodeCreated[str].emit(node_path)

    @QtCore.pyqtSlot(str)
    def copperSetCompositeViewNode(self, node_path = None):
        if not self.path_bar_widget.isPinned():
            self.signals.copperSetCompositeViewNode[str].emit(node_path)

    @QtCore.pyqtSlot(str)
    def copperNodeModified(self, node_path = None):
        if not self.path_bar_widget.isPinned():
            self.signals.copperNodeModified[str].emit(node_path)



