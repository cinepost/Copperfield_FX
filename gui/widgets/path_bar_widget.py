from PyQt4 import Qt, QtGui, QtCore

from gui.signals import signals
from copper import engine
from copper import parameter

class PathBarWidget(QtGui.QFrame):
    def __init__(self, parent=None): 
        QtGui.QFrame.__init__(self, parent)     
        self.pinned = False
        self.history = []
        self.history_index = -1
        self.setObjectName("pathBar")
        
        layout = QtGui.QHBoxLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(0, 2, 0, 2)

        self.btn_back = QtGui.QToolButton(self)
        self.btn_back.setIcon(QtGui.QIcon( "icons/main/go-previous.svg"))
        self.btn_back.setEnabled(False)
        self.btn_back.pressed.connect(self.historyGoBack)

        self.btn_frwd = QtGui.QToolButton(self)
        self.btn_frwd.setIcon(QtGui.QIcon("icons/main/go-next.svg"))
        self.btn_frwd.setEnabled(False)
        self.btn_frwd.pressed.connect(self.historyGoForward)

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

        self.buildPathBar(node_path="/obj")

    def historyGoBack(self):
        if self.history_index > 0:
            self.history_index -= 1
            print "History back to: %s with index %s" % (self.history[self.history_index], self.history_index)
            self.btn_frwd.setEnabled(True)
            if self.history_index == 0:
                self.btn_back.setEnabled(False)

            signals.copperNodeSelected.emit(self.history[self.history_index])

    def historyGoForward(self):
        if self.history_index < (len(self.history) - 1):
            self.history_index += 1
            print "History fwd to: %s with index %s" % (self.history[self.history_index], self.history_index)
            self.btn_back.setEnabled(True)
            if self.history_index == (len(self.history) - 1):
                self.btn_frwd.setEnabled(False)

            signals.copperNodeSelected.emit(self.history[self.history_index])

    def pinPressed(self):
        if self.pinned == False:
            self.pinned = True
        else:
            self.pinned = False

    def isPinned(self):
        return self.pinned

    def nodeSelected(self, node_path=None):
        if self.buildPathBar(node_path):
            if self.history:
                if self.history[-1] == node_path:
                    return

            self.history += [node_path]
            self.history_index += 1
            print "History added: %s at index %s" % (node_path, self.history_index)
            self.btn_back.setEnabled(True)

    def buildPathBar(self, node_path=None):
        node = engine.node(node_path).parent()
        if node.isRoot():
            node = engine.node(node_path)

        if not node:
            return False

        for i in reversed(range(self.path_layout.count())): 
            self.path_layout.itemAt(i).widget().deleteLater()

        btn = None

        path_nodes = node.pathAsNodeList()

        for node in path_nodes:
            btn = QtGui.QPushButton()
            btn.setIcon(QtGui.QIcon(node.iconName()))
            btn.setText(node.name())
            btn.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)

            menu = QtGui.QMenu()
            menu.addAction('This is Action 1')
            menu.addAction('This is Action 2')
            btn.setMenu(menu)

            self.path_layout.addWidget(btn)

        btn.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)

        return True


