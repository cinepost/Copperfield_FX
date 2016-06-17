from PyQt4 import Qt, QtGui, QtCore
from compy import parameter

def clearParametersLayout(layout):
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

class ParamsWidget(QtGui.QWidget):
  
    def __init__(self, parent=None, engine=None):      
        super(ParamsWidget, self).__init__(parent)
        self.engine = engine
        self.connect(self, QtCore.SIGNAL("node_selected"), self.setNode)
        self.default_icon = QtGui.QIcon('icons/glyphicons_461_saw_blade.png')
        self.initUI()
        
    def initUI(self):
        self.setMinimumWidth(320)

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)

        self.header = QtGui.QHBoxLayout()

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(self.header)
        vbox.addLayout(self.grid)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.setAcceptDrops(True)

    def BrowseFile(self, lineEdit):
        fname = QtGui.QFileDialog.getOpenFileName()
        lineEdit.setText(fname)

    @QtCore.pyqtSlot()   
    def setNode(self, node_path = None):
        node = self.engine.node(node_path)
        
        # remove old parms widgets
        clearParametersLayout(self.header)
        clearParametersLayout(self.grid)

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

        self.header.addWidget(node_btn)
        self.header.addWidget(node_type)
        self.header.addWidget(node_name)
        
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

            elif parm_type is parameter.CompyParmInt:
                # integer
                valueEdit = QtGui.QSpinBox()
                valueEdit.setMinimum(0)
                valueEdit.setMaximum(10000)  
                valueEdit.setValue(value)
                valueEdit.valueChanged.connect(parm.setValueInt)

            elif parm_type is parameter.CompyParmFloat:
                # float
                valueEdit = QtGui.QLineEdit(str(value)) 
                valueEdit.textChanged.connect(parm.setValueFloat)
            
            elif parm_type is parameter.CompyParmButton:
                # button
                valueEdit = QtGui.QPushButton(parm.label(), self)
                valueEdit.clicked.connect(parm.getCallback())

            elif parm_type is parameter.CompyParmOpPath:
                # op path
                valueEdit = OpPathWidget(str(value))      
            
            elif parm_type is parameter.CompyParmOrderedMenu:
                # menu
                valueEdit = QtGui.QComboBox(self)
                for item_name in parm.__menu_items__:
                    valueEdit.addItem(parm.__menu_items__[item_name])
                valueEdit.setCurrentIndex(parm.evalAsInt())
 
            elif parm_type is parameter.CompyParmFile:
                # file path
                valueEdit = QtGui.QHBoxLayout()
                filePath = QtGui.QLineEdit(str(value))
                filePath.textChanged.connect(parm.setValueStr)           
                fileDialog = QtGui.QPushButton("Choose", self)
                fileDialog.clicked.connect(lambda: self.BrowseFile(filePath))
                valueEdit.addWidget(filePath)
                valueEdit.addWidget(fileDialog)

            else:    
                # all other
                valueEdit = QtGui.QLineEdit(str(value))
                valueEdit.textChanged.connect(parm.setValue)  
            
            # highlight animated parameter
            if parm.animated():
                valueEdit.setStyleSheet("background-color: rgb(128,255,128)")    

            label = QtGui.QLabel(parm.label())
            label.setStatusTip(parm.name)

            self.grid.addWidget(label, i, 0)

            if isinstance(valueEdit, QtGui.QLayout):
                self.grid.addLayout(valueEdit, i, 1)
            else:
                self.grid.addWidget(valueEdit, i, 1)

            i+=1

        print "Total widgets: %s" % self.grid.count()