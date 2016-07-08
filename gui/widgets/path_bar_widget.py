from PyQt4 import Qt, QtGui, QtCore
from copper import parameter

class PathBarWidget(QtGui.QFrame):
    def __init__(self, parent=None): 
        QtGui.QFrame.__init__(self, parent)     
        self.pinned = False
        self.setObjectName("pathBar")
        
        layout = QtGui.QHBoxLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(0, 2, 0, 2)

        self.btn_back = QtGui.QToolButton(self)
        self.btn_back.setObjectName("back")
        
        self.btn_frwd = QtGui.QToolButton(self)
        self.btn_frwd.setObjectName("fwd")

        self.btn_pin = QtGui.QToolButton(self)
        self.btn_pin.setObjectName("pin")
        self.btn_pin.setCheckable(True)
        self.btn_pin.pressed.connect(self.pinPressed)

        self.path_layout = QtGui.QHBoxLayout()
        self.path_layout.setContentsMargins(0, 0, 0, 0)
        self.path_layout.addStretch(1)

        layout.addWidget(self.btn_back)
        layout.addWidget(self.btn_frwd)
        layout.addLayout(self.path_layout)
        layout.addWidget(self.btn_pin)

        self.setLayout(layout)
        self.setAcceptDrops(True)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)

        self.buildPathBar()

    def pinPressed(self):
        if self.pinned == False:
            self.pinned = True
        else:
            self.pinned = False

    def buildPathBar(self):
        btn = QtGui.QToolButton()
        btn.setText("file1")
        self.path_layout.addWidget(btn)

        btn = QtGui.QToolButton()
        btn.setText("file1")
        self.path_layout.addWidget(btn)

        btn = QtGui.QToolButton()
        btn.setText("file1")
        self.path_layout.addWidget(btn)

        btn = QtGui.QToolButton()
        btn.setText("file1")
        self.path_layout.addWidget(btn)
