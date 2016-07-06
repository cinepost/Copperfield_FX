from PyQt4 import Qt, QtGui, QtCore
from copper import parameter

from copper import engine
from gui.signals import signals
from gui.widgets import PathBarWidget
from gui.panels.base_panel import BasePanel
from parameters_widgets import *

def clearParametersLayout(layout):
    pass
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearParametersLayout(child.layout())

class ParametersPanel(BasePanel):
    def __init__(self):      
        BasePanel.__init__(self)   

        self.path_bar_widget = PathBarWidget()
        self.parameters_widget = ParametersWidget()

        self.setNetworkControlsWidget(self.path_bar_widget)
        self.addWidget(self.parameters_widget)

    @classmethod
    def panelTypeName(cls):
        return "Parameters"

    @classmethod
    def hasNetworkControls(cls):
        return True


class ParametersWidget(QtGui.QWidget):
    def __init__(self, parent=None):    
        QtGui.QWidget.__init__(self, parent) 
        self.default_icon = QtGui.QIcon('icons/glyphicons_461_saw_blade.png')

        self.setMinimumWidth(320)
        self.setMinimumHeight(160)

        self.parm_box = QtGui.QVBoxLayout(self)
        self.parm_box.setSpacing(2)
        self.parm_box.setContentsMargins(0, 0, 0, 0)
        no_op_label = QtGui.QLabel("No Operator Selected")
        no_op_label.setObjectName("info")
        no_op_label.setSizePolicy( QtGui.QSizePolicy( QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum ))
        no_op_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.parm_box.addStretch(1)
        self.parm_box.addWidget(no_op_label)
        self.parm_box.addStretch(1)

        #Container Widget        
        widget = QtGui.QWidget(self)

        widget.setLayout(self.parm_box)
        widget.setObjectName("Parameters")

        scroll = QtGui.QScrollArea()
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        self.header_bar = QtGui.QHBoxLayout()

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)

        vbox.addLayout(self.header_bar)
        vbox.addWidget(scroll)

        self.setLayout(vbox)
        self.setAcceptDrops(True)

        ### Connect GUI signals
        signals.copperNodeSelected.connect(self.nodeSelected)


    @QtCore.pyqtSlot(str)   
    def nodeSelected(self, node_path = None):
        node = engine.node(str(node_path))
        
        # remove old parms widgets
        clearParametersLayout(self.header_bar)
        clearParametersLayout(self.parm_box)

        # build header
        if node.iconName():
            icon = QtGui.QIcon(node.iconName())
        else:
            icon = self.default_icon

        node_btn = QtGui.QToolButton()
        node_btn.setIcon(icon)
        node_btn.setIconSize(QtCore.QSize(24,24))

        node_type = QtGui.QLabel(node.label())
        node_type.setStyleSheet("font-weight: bold")
   
        node_name = QtGui.QLineEdit(node.name())

        self.header_bar.addWidget(node_btn)
        self.header_bar.addWidget(node_type)
        self.header_bar.addWidget(node_name)
        
        # build new parms widgets
        i = 1
        for parm in node.parms():
            value = parm.eval()
            parm_type = parm.type()

            if parm_type is bool:
                # check box
                widget = ParameterBoolWidget(self, parm)

            elif parm_type is parameter.CopperParmInt:
                # integer
                widget = ParameterIntWidget(self, parm)

            elif parm_type is parameter.CopperParmFloat:
                # float
                widget = ParameterFloatWidget(self, parm)
            
            elif parm_type is parameter.CopperParmButton:
                # button
                widget = ParameterButtonWidget(self, parm)

            elif parm_type is parameter.CopperParmOpPath:
                # op path
                widget = ParameterOpPathWidget(self, parm)

            elif parm_type is parameter.CopperParmOrderedMenu:
                # menu
                widget = ParameterChoiceWidget(self, parm)
 
            elif parm_type is parameter.CopperParmFile:
                # file path
                widget = ParameterFilePathWidget(self, parm)

            else:    
                # all other
                widget = QtGui.QLineEdit(str(value))
                widget.returnPressed.connect(parm.setValue)  
            
            # highlight animated parameter
            if parm.animated():
                widget.setStyleSheet("background-color: rgb(128,255,128)")    

            hbox = QtGui.QHBoxLayout()
            if parm_type is bool:    
                label = QtGui.QLabel("")
            else:
                label = QtGui.QLabel(parm.label())

            label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            label.setStatusTip(parm.name())
            label.setFixedWidth(140)
            hbox.addWidget(label)


            if isinstance(widget, QtGui.QLayout):
                hbox.addLayout(widget)
            else:
                hbox.addWidget(widget)

            self.parm_box.addLayout(hbox)

            i+=1

        self.parm_box.addStretch(1)
