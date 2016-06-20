from PyQt4 import QtGui, QtCore
from path_bar_widget import PathBarWidget

class NodeTreeEditorWidget(QtGui.QFrame):
    def __init__(self, parent, engine=None, viewer=None, params=None):      
        super(NodeTreeEditorWidget, self).__init__(parent)
        self.engine = engine
        vbox = QtGui.QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        pathBar = PathBarWidget(self, engine=engine)
        nodeTreeEditor=NodeTreeEditor(self, engine=engine, viewer=viewer, params=params)
        vbox.addWidget(pathBar)
        vbox.addWidget(nodeTreeEditor)
        self.setLayout(vbox)

    def copy(self):
        return NodeTreeEditorWidget(None, engine=self.engine)

class NodeTreeEditor(QtGui.QTreeWidget):
  
    def __init__(self, parent, engine=None, viewer=None, params=None):      
        super(NodeTreeEditor, self).__init__(parent)
        self.parent = parent
        self.engine = engine
        self.viewer = viewer
        self.params = params
        self.current_node = None

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self, QtCore.SIGNAL("network_changed"), self.rebuild)
        self.connect(self, QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), self.menuContextTree)
        self.itemClicked.connect(self.handleItemClicked)
        self.setDragEnabled(True)
        self.initUI()
        
    def initUI(self):
        self.setAlternatingRowColors(True)
        vbox = QtGui.QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        
        #header=QtGui.QTreeWidgetItem(["Name", "Path","Type"])
        #self.setHeaderItem(header)
        self.header().close()
        self.createNodeLevel(self.engine, self) 

    def createNodeLevel(self, node, parent_widget):
        for cur_node in node.children():
            item = QtGui.QTreeWidgetItem(parent_widget)
            item.setExpanded(True)
            item.setText(0, cur_node.name())
            item.setText(1, cur_node.path())
            #item.setText(2, str(cur_node))
            if cur_node.children():
                self.createNodeLevel(cur_node, item)  

    def handleItemClicked(self, item, column):
        self.params.emit(QtCore.SIGNAL('node_selected'), str(item.text(1)))              

    @QtCore.pyqtSlot()   
    def rebuild(self):
        self.clear()
        self.createNodeLevel(self.engine, self)

    @QtCore.pyqtSlot()   
    def menuContextTree(self, point):
        # Infos about the node selected.     
        index = self.indexAt(point)

        if not index.isValid():
            return

        item = self.itemAt(point)
        node_path = str(item.text(1))
        name = item.text(0)  # The text of the node.

        # We build the menu.
        menu=QtGui.QMenu(self)
        action=menu.addAction(name)
        menu.addSeparator()

        action_1=menu.addAction("Show in viewer")
        action_1.triggered.connect(lambda: self.viewer.setNode(node_path))

        action_1=menu.addAction("Render")
        action_1.triggered.connect(lambda: self.parent.renderNode(node_path))

        action_3=menu.addAction("Delete")

        menu.exec_(QtGui.QCursor.pos())  