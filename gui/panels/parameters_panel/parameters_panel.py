from PyQt4 import Qt, QtGui, QtCore
from copper import parameter

from copper import engine
from gui.signals import signals
from gui.widgets import PathBarWidget
from gui.panels.base_panel import NetworkPanel
from parameters_widgets import *

from copper.parm_template import ParmLookScheme, ParmNamingScheme, ParmTemplateType, StringParmType

def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearLayout(child.layout())

class ParametersPanel(NetworkPanel):
    def __init__(self):      
        NetworkPanel.__init__(self)   

        self.parameters_widget = ParametersWidget(self, self)
        self.addWidget(self.parameters_widget)

    @classmethod
    def panelTypeName(cls):
        return "Parameters"


class ParametersWidget(QtGui.QWidget):
    def __init__(self, parent, panel):    
        QtGui.QWidget.__init__(self, parent) 
        self.panel = panel

        self.setMinimumWidth(320)
        self.setMinimumHeight(160)

        self.parm_box = QtGui.QVBoxLayout(self)
        self.parm_box.setSpacing(0)
        self.parm_box.setContentsMargins(0, 0, 0, 0)

        no_op_label = QtGui.QLabel("No Operator Selected")
        no_op_label.setObjectName("info")
        no_op_label.setSizePolicy( QtGui.QSizePolicy( QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum ))
        no_op_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.parm_box.addStretch(1)
        self.parm_box.addWidget(no_op_label)
        self.parm_box.addStretch(1)

        #Container Widget        
        self.widget = QtGui.QWidget(self)
        self.widget.setLayout(self.parm_box)
        self.widget.setObjectName("Parameters")

        self.scroll = QtGui.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.header_bar = QtGui.QHBoxLayout()
        self.header_bar.setSpacing(2)
        self.header_bar.setContentsMargins(0, 0, 0, 0)

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0, 0, 0, 0)

        self.vbox.addLayout(self.header_bar)
        self.vbox.addWidget(self.scroll)

        self.setLayout(self.vbox)
        self.setAcceptDrops(True)

        # connect panel signals
        self.panel.signals.copperNodeSelected.connect(self.nodeSelected)

    @QtCore.pyqtSlot(str)
    def nodeSelected(self, node_path=None):
        if node_path in [None, "/"]:
            return 

        node = engine.node(str(node_path))
        
        # remove old parms widgets
        clearLayout(self.header_bar)
        clearLayout(self.parm_box)

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
        for parm_template in node.parmGroups().keys():
            parm_template_type = parm_template.type()

            parms_layout = QtGui.QHBoxLayout()
            parms_layout.setSpacing(1)
            parms_layout.setContentsMargins(0, 0, 0, 0)
            for parm in node.parmGroups()[parm_template]:
                if parm_template_type is ParmTemplateType.Int:
                    # Int
                    widget = ParameterIntWidget(self, parm)

                elif parm_template_type is ParmTemplateType.Float:
                    # Float
                    widget = ParameterFloatWidget(self, parm)
                
                elif parm_template_type is ParmTemplateType.Button:
                    # Button
                    widget = ParameterButtonWidget(self, parm)

                elif parm_template_type is ParmTemplateType.Menu:
                    # Menu
                    widget = ParameterMenuWidget(self, parm)

                elif parm_template_type is ParmTemplateType.Toggle:
                    # Toggle
                    widget = ParameterToggleWidget(self, parm)

                elif parm_template_type is ParmTemplateType.String:
                    # String
                    widget = ParameterStringWidget(self, parm)

                parms_layout.addWidget(widget) 
                

            hbox = QtGui.QHBoxLayout()
            if parm_template_type not in [ParmTemplateType.Toggle, ParmTemplateType.Button]:
                label = QtGui.QLabel(parm_template.label())
                if parm_template.numComponents() == 1:
                    label.setToolTip("Parameter: %s" % parm.name())
                else:
                    label.setToolTip("Parameters: %s" % [parm.name() for parm in node.parmGroups()[parm_template]])

                label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                label.setStatusTip(parm.name())
                label.setFixedWidth(140)
                hbox.addWidget(label)
            else:
                hbox.addSpacing(143)

            hbox.addLayout(parms_layout)

            self.parm_box.addLayout(hbox)

            i+=1

        self.parm_box.addStretch(1)
