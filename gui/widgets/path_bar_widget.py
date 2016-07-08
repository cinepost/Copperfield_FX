from PyQt4 import Qt, QtGui, QtCore

from copper import engine
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
        self.path_layout.setSpacing(0)
        self.path_layout.setContentsMargins(0, 0, 0, 0)

        self.path_bar = QtGui.QFrame()
        self.path_bar.setObjectName("bar")
        self.path_bar.setLayout(self.path_layout)

        layout.addWidget(self.btn_back)
        layout.addWidget(self.btn_frwd)
        layout.addWidget(self.path_bar)
        layout.addWidget(self.btn_pin)

        self.setLayout(layout)
        self.setAcceptDrops(True)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)

        self.buildPathBar(node_path="/obj/geo1")

    def pinPressed(self):
        if self.pinned == False:
            self.pinned = True
        else:
            self.pinned = False

    def isPinned(self):
        return self.pinned

    def nodeSelected(self, node_path=None):
        self.buildPathBar(node_path)

    def buildPathBar(self, node_path=None):
        node = engine.node(node_path)

        if not node:
            return

        for i in reversed(range(self.path_layout.count())): 
            self.path_layout.itemAt(i).widget().deleteLater()

        parent = node.parent()
        while parent:
            if parent is not engine:
                btn = QtGui.QPushButton()
                btn.setText(parent.name())
                self.path_layout.addWidget(btn)
            
            parent = parent.parent()

        btn.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        #self.path_layout.setStretchFactor (btn, 1)
