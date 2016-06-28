from PyQt4 import Qt, QtGui, QtCore
from copper import parameter

class PathBarWidget(QtGui.QFrame):
    def __init__(self, parent=None): 
        QtGui.QFrame.__init__(self, parent)     

        self.setObjectName("pathBar");
        
        layout = QtGui.QHBoxLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(0, 2, 0, 2)

        btn_back = QtGui.QToolButton(self)
        btn_back.setObjectName("back")
        btn_frwd = QtGui.QToolButton(self)
        btn_frwd.setObjectName("fwd")


        self.path = QtGui.QHBoxLayout()
        self.path.setContentsMargins(0, 0, 0, 0)
        self.path.addStretch(1)

        layout.addWidget(btn_back)
        layout.addWidget(btn_frwd)
        layout.addLayout(self.path)

        self.setLayout(layout)
        self.setAcceptDrops(True)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)