from PyQt4 import QtCore, QtGui


class BasePanel(QtGui.QFrame):
    def __init__(self, workspace=None, engine=None):
        QtGui.QFrame.__init__(self)
        self.engine = engine
        self.workspace = workspace
        self.network_controls_widget = None
        self.panel_layout = QtGui.QVBoxLayout()
        self.panel_layout.setSpacing(0)
        self.panel_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.panel_layout)

        ''' connect signals '''
        QtCore.QObject.connect(self, QtCore.SIGNAL('copperNodeSelected'), self.copperNodeSelected)  

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

    @classmethod
    def hasNetworkControls(cls):
        '''
        This method is used to determine particular panel type implements network navigation control aka path bar
        '''
        raise NotImplementedError

    def getNetworkControlsWidget(self):
        '''
        This method is used by UI to get control of network_controls_widget (whether it path bar or anything else) to hide and unhide it. Just mimiking dad's beheavior
        '''
        return self.network_controls_widget

    def setNetworkControlsWidget(self, widget):
        if not self.network_controls_widget:
            ### Add network controls widget
            self.network_controls_widget = widget
            self.panel_layout.insertWidget(0, self.network_controls_widget)
        else:
            raise BaseException("%s network controls widget already set !!!" % self.__class__)

    def addLayout(self, layout):
        self.panel_layout.addLayout(layout)

    def addWidget(self, widget):
        self.panel_layout.addWidget(widget)

    @QtCore.pyqtSlot()   
    def copperNodeSelected(self, node_path = None):
        print "copperNodeSelected not implemented in %s" % self.__class__

