from PyQt4 import QtCore, QtGui

from gui.widgets import PathBarWidget
from gui.signals import signals

class BasePanel(QtGui.QFrame):
    def __init__(self, network_controls=False):
        QtGui.QFrame.__init__(self)
        self.network_controls = network_controls
        self.panel_layout = QtGui.QVBoxLayout()
        self.panel_layout.setSpacing(0)
        self.panel_layout.setContentsMargins(0, 0, 0, 0)

        if self.hasNetworkControls():
            self.path_bar_widget = PathBarWidget(self)
            self.panel_layout.addWidget(self.path_bar_widget)
        else:
            self.path_bar_widget = None

        self.setLayout(self.panel_layout)

        ''' connect signals '''
        signals.copperNodeSelected.connect(self.copperNodeSelected)  

    def copyPanel(self):
        '''
        This method is used for copying panels and maintain all the setting and variables.
        Should be reimplemented by inhereted panel type
        '''
        return self.__class__(None, engine=self.engine)

    @classmethod
    def panelTypeName(cls):
        '''
        This method is used to get panel type name and display it as window title or tab title
        '''
        raise NotImplementedError

    def hasNetworkControls(self):
        '''
        This method is used to determine particular panel type implements network navigation control aka path bar
        '''
        return self.network_controls

    def getNetworkControlsWidget(self):
        '''
        This method is used by UI to get control of network_controls_widget (whether it path bar or anything else) to hide and unhide it. Just mimiking dad's beheavior
        '''
        return self.path_bar_widget

    def nodeSelected(self, node_path = None):
        raise NotImplementedError

    def addLayout(self, layout):
        self.panel_layout.addLayout(layout)

    def addWidget(self, widget):
        self.panel_layout.addWidget(widget)

    @QtCore.pyqtSlot(str)   
    def copperNodeSelected(self, node_path = None):
        if self.hasNetworkControls():
            if not self.path_bar_widget.isPinned():
                self.path_bar_widget.nodeSelected(str(node_path))
                self.nodeSelected(str(node_path))
            else:
                print "pinned"

