from PyQt4 import Qt, QtGui, QtCore
from copper import parameter

from copper_widget import CopperWidget

class PathBarWidget(QtGui.QFrame, CopperWidget):
  
    def __init__(self, parent, engine=None):      
        super(PathBarWidget, self).__init__(parent)
        self.engine = engine
        self.setObjectName("pathBar");
        self.initUI()
        
    def initUI(self):
        layout = QtGui.QHBoxLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(0, 4, 0, 4)

        btn_back = QtGui.QToolButton(self)
        btn_back.setObjectName("back")
        btn_frwd = QtGui.QToolButton(self)
        btn_frwd.setObjectName("fwd")

        self.path = QtGui.QHBoxLayout()
        self.path.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(btn_back)
        layout.addWidget(btn_frwd)
        layout.addLayout(self.path)

        self.setLayout(layout)
        self.setAcceptDrops(True)