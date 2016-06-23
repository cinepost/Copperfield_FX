from PyQt4 import QtGui, QtCore

from gui.widgets import PathBarWidget
from base_panel import BasePanel

class TreeViewPanel(BasePanel):
    def __init__(self, parent=None, engine=None, viewer=None, params=None):      
        BasePanel.__init__(self, parent)
        self.engine = engine
        self.initUI()

    def initUI(self):
        self.path_bar_widget = PathBarWidget(self, engine=self.engine)
        self.tree_view_widget = TreeViewWidget(self, engine=self.engine)

        self.setNetworkControlsWidget(self.path_bar_widget)
        self.addWidget(self.tree_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Tree View"

    @classmethod
    def hasNetworkControls(cls):
        return True

class TreeViewWidget(QtGui.QTreeWidget):
    def __init__(self, parent=None, engine=None, viewer=None, params=None):      
        QtGui.QTreeWidget.__init__(self, parent)

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