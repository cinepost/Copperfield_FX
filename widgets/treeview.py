from PyQt4 import QtGui, QtCore

class TreeNodeViewerWidget(QtGui.QTreeWidget):
  
    def __init__(self, parent=None, engine=None, viewer=None):      
        super(TreeNodeViewerWidget, self).__init__(parent)
        self.engine = engine
        self.viewer = viewer
        self.current_node = None

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self, QtCore.SIGNAL("network_changed"), self.rebuild)
        self.connect(self, QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), self.menuContextTree)
        self.initUI()
        
    def initUI(self):
        header=QtGui.QTreeWidgetItem(["Type", "Name", "Path"])
        self.setHeaderItem(header) 

    def createNodeLevel(self, node, parent_widget):
        for node_name in node.children.keys():
            cur_node = node.children[node_name]
            item = QtGui.QTreeWidgetItem(parent_widget)
            item.setText(0, str(cur_node))
            item.setText(1, cur_node.name)
            item.setText(2, cur_node.path)
            if cur_node.children:
                self.createNodeLevel(cur_node, item)    

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
        node_path = str(item.text(2))
        name = item.text(0)  # The text of the node.

        # We build the menu.
        menu=QtGui.QMenu(self)
        action=menu.addAction(name)
        menu.addSeparator()

        action_1=menu.addAction("Show in viewer")
        action_1.triggered.connect(lambda: self.viewer.setNode(node_path))

        action_2=menu.addAction("Delete")

        menu.exec_(QtGui.QCursor.pos())  