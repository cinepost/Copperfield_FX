from PyQt4 import Qt, QtGui, QtCore
from copper import parameter

class PathBarWidget(QtGui.QFrame):
  
    def __init__(self, parent, engine=None):      
        super(PathBarWidget, self).__init__(parent)
        self.engine = engine
        self.setObjectName("pathBar");
        self.connect(self, QtCore.SIGNAL("node_selected"), self.setNode)
        self.initUI()
        
    def initUI(self):
        layout = QtGui.QHBoxLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(0, 4, 0, 4)

        btn_back = QtGui.QToolButton(self)
        btn_back.setObjectName("back")
        btn_frwd = QtGui.QToolButton(self)
        btn_frwd.setObjectName("fwd")
        str_path = QtGui.QLineEdit("/")

        layout.addWidget(btn_back)
        layout.addWidget(btn_frwd)
        layout.addWidget(str_path)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    @QtCore.pyqtSlot()   
    def setNode(self, node_path = None):
        node = self.engine.node(node_path)