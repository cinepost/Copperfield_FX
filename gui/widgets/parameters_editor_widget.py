from PyQt4 import Qt, QtGui, QtCore
from copper import parameter
from path_bar_widget import PathBarWidget

def clearParametersLayout(layout):
    pass
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearParametersLayout(child.layout())


class OpPathWidget(QtGui.QLineEdit):
    def __init__(self, contents, parent=None):
        super(OpPathWidget, self).__init__(contents, parent)
        print "OpPathWidget"
        self.setAcceptDrops(True)

    def dropEvent(self, event):
        print "Drop!"

class ParametersEditorWidget(QtGui.QWidget):
    def __init__(self, parent=None, engine=None):     
        QtGui.QWidget.__init__(self, parent) 
        self.engine = engine
        self.connect(self, QtCore.SIGNAL("node_selected"), self.setNode)
        self.default_icon = QtGui.QIcon('icons/glyphicons_461_saw_blade.png')
        self.initUI()
        
    def initUI(self):
        self.setMinimumWidth(320)
        self.setMinimumHeight(160)

        self.parm_box = QtGui.QVBoxLayout(self)
        self.parm_box.setSpacing(2)
        self.parm_box.setContentsMargins(0, 0, 0, 0)


        #Container Widget        
        widget = QtGui.QWidget(self)
        #widget.setStyleSheet("QWidget {background-color: #0f0; border: none;}")

        widget.setLayout(self.parm_box)
        widget.setObjectName("Parameters")

        scroll = QtGui.QScrollArea()
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        scroll.setStyleSheet("QScrollArea {background-color: #f00; border: none;}")
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        self.path_bar = PathBarWidget(self)
        self.header_bar = QtGui.QHBoxLayout()

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)

        vbox.addWidget(self.path_bar)
        vbox.addLayout(self.header_bar)
        vbox.addWidget(scroll)

        self.setLayout(vbox)
        self.setAcceptDrops(True)

    @classmethod
    def panelTypeName(cls):
        return "Parameters"


    def copy(self):
        return ParametersEditorWidget(None, engine=self.engine)


    def BrowseFile(self, lineEdit):
        fname = QtGui.QFileDialog.getOpenFileName()
        lineEdit.setText(fname)


    @QtCore.pyqtSlot()   
    def setNode(self, node_path = None):
        node = self.engine.node(node_path)
        
        # remove old parms widgets
        clearParametersLayout(self.header_bar)
        clearParametersLayout(self.parm_box)

        # build header
        #icon = node.getIcon()
        icon = None
        if not icon:
            icon = self.default_icon

        node_btn = QtGui.QToolButton()
        node_btn.setIcon(icon)
        node_btn.setIconSize(QtCore.QSize(24,24))

        node_type = QtGui.QLabel(node.type_name)
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
                valueEdit = QtGui.QCheckBox()
                if value: valueEdit.setCheckState(QtCore.Qt.Checked)
                valueEdit.stateChanged.connect(parm.setValue)

            elif parm_type is parameter.CopperParmInt:
                # integer
                valueEdit = QtGui.QSpinBox()
                valueEdit.setMinimum(0)
                valueEdit.setMaximum(10000)  
                valueEdit.setValue(value)
                valueEdit.valueChanged.connect(parm.setValueInt)

            elif parm_type is parameter.CopperParmFloat:
                # float
                valueEdit = QtGui.QHBoxLayout()
                valueEditField = QtGui.QLineEdit(str(value)) 
                valueEditField.setMinimumWidth(60)
                valueEditField.setMaximumWidth(140)
                valueEditField.returnPressed.connect(parm.setValueFloat)
                
                valueSlider = QtGui.QSlider()
                valueSlider.setOrientation(QtCore.Qt.Horizontal)
                valueSlider.setTracking(True);

                valueEdit.addWidget(valueEditField)
                valueEdit.addWidget(valueSlider)
            
            elif parm_type is parameter.CopperParmButton:
                # button
                valueEdit = QtGui.QPushButton(parm.label(), self)
                valueEdit.setMinimumWidth(60)
                valueEdit.setMaximumWidth(140)
                valueEdit.clicked.connect(parm.getCallback())

            elif parm_type is parameter.CopperParmOpPath:
                # op path
                valueEdit = OpPathWidget(str(value))      
            
            elif parm_type is parameter.CopperParmOrderedMenu:
                # menu
                valueEdit = QtGui.QComboBox(self)
                for item_name in parm.__menu_items__:
                    valueEdit.addItem(parm.__menu_items__[item_name])
                valueEdit.setCurrentIndex(parm.evalAsInt())
 
            elif parm_type is parameter.CopperParmFile:
                # file path
                valueEdit = QtGui.QHBoxLayout()
                filePath = QtGui.QLineEdit(str(value))
                filePath.returnPressed.connect(parm.setValueStr)           
                fileDialog = QtGui.QPushButton("Choose", self)
                fileDialog.clicked.connect(lambda: self.BrowseFile(filePath))
                valueEdit.addWidget(filePath)
                valueEdit.addWidget(fileDialog)

            else:    
                # all other
                valueEdit = QtGui.QLineEdit(str(value))
                valueEdit.returnPressed.connect(parm.setValue)  
            
            # highlight animated parameter
            if parm.animated():
                valueEdit.setStyleSheet("background-color: rgb(128,255,128)")    

            hbox = QtGui.QHBoxLayout()
            label = QtGui.QLabel(parm.label())
            label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            label.setStatusTip(parm.name)
            label.setFixedWidth(140)
            hbox.addWidget(label)


            if isinstance(valueEdit, QtGui.QLayout):
                hbox.addLayout(valueEdit)
            else:
                hbox.addWidget(valueEdit)

            self.parm_box.addLayout(hbox)

            i+=1

        self.parm_box.addStretch(1)
