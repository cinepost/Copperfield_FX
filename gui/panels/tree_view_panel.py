from PyQt4 import QtGui, QtCore

from copper import engine
from gui.signals import signals
from gui.widgets import PathBarWidget
from base_panel import BasePanel

class TreeViewPanel(BasePanel):
    def __init__(self):      
        BasePanel.__init__(self) 

        self.path_bar_widget = PathBarWidget()
        self.tree_view_widget = TreeViewWidget()

        self.setNetworkControlsWidget(self.path_bar_widget)
        self.addWidget(self.tree_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Tree View"

    @classmethod
    def hasNetworkControls(cls):
        return True


class TreeViewWidget(QtGui.QTreeWidget):
    def __init__(self, parent=None):      
        QtGui.QTreeWidget.__init__(self, parent)
        self.setObjectName("QTreeView")
        self.current_node = None
        self.setIconSize(QtCore.QSize(16,16))
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setDragEnabled(True)

        self.setAlternatingRowColors(True)
        vbox = QtGui.QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        
        self.header().close()
        self.createNodeTree(self, engine.node("/")) 

        ### Connect signals from UI
        self.connect(self, QtCore.SIGNAL("copperNetworkChanged"), self.rebuildNodeTree)

        ### Connect internal signals
        self.connect(self, QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), self.menuContextMenu)
        self.itemClicked.connect(self.handleItemClicked)

    def createNodeTree(self, parent, node=None):
        if node:
            for cur_node in node.children():
                item = QtGui.QTreeWidgetItem(parent)
                item.setExpanded(True)

                if cur_node.iconName():
                    item.setIcon(0, QtGui.QIcon(cur_node.iconName()))

                item.setText(0, cur_node.name())
                item.setText(1, cur_node.path())
                if cur_node.children():
                    self.createNodeTree(item, cur_node)  

    def handleItemClicked(self, item):
        selected_node_path = str(item.text(1))
        signals.copperNodeSelected[str].emit(selected_node_path)              

    def handleShowInViewer(self, node_path):
        signals.copperSetCompositeViewNode[str].emit(node_path)

    @QtCore.pyqtSlot()   
    def rebuildNodeTree(self):
        self.clear()
        self.createNodeTree(self.engine, self)

    @QtCore.pyqtSlot()   
    def menuContextMenu(self, point):
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
        action_1.triggered.connect(lambda: self.handleShowInViewer(node_path))

        action_2=menu.addAction("Render")
        #action_2.triggered.connect(lambda: self.workspace.copperRenderNode(node_path))

        action_3=menu.addAction("Delete")
        #action_3.triggered.connect(lambda: self.workspace.copperDeleteNode(node_path))

        menu.exec_(QtGui.QCursor.pos())  