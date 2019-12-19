from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal

from copper import hou
from copper.ui.signals import signals
from copper.ui.widgets import PathBarWidget

from .base_panel import PathBasedPaneTab

class TreeViewPanel(PathBasedPaneTab):
    def __init__(self):      
        PathBasedPaneTab.__init__(self) 

        self.tree_view_widget = TreeViewWidget()
        self.addWidget(self.tree_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Tree View"


class TreeViewWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):      
        QtWidgets.QTreeWidget.__init__(self, parent)
        self.nodes_map = {}
        self.setDragEnabled(True)
        self.setObjectName("QTreeView")
        self.current_node = None
        self.setIconSize(QtCore.QSize(16,16))
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.setAlternatingRowColors(True)
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        
        self.header().close()

        # build tree from root
        self.createNodeTree(self)

        ### Connect signals from UI
        signals.copperNodeCreated.connect(self.rebuildNodeTree)
        signals.copperNodeSelected[str].connect(self.nodeSelected)

        ### Connect internal signals
        #self.connect(self, QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), self.menuContextMenu)
        self.customContextMenuRequested.connect(self.menuContextMenu)
        self.itemClicked.connect(self.handleItemClicked)

    def createNodeTree(self, parent, node_path=None):
        """Builds node tree from node"""
        if not node_path:
            # create root node item
            root_item = QtWidgets.QTreeWidgetItem(self)
            root_item.setExpanded(True)
            root_item.setIcon(0, QtGui.QIcon(hou.node("/").iconName()))
            root_item.setText(0, "/")
            root_item.setText(1, "/")
            self.nodes_map["/"] = root_item
            self.createNodeTree(root_item, "/")
        else:
            node = hou.node(node_path)
            if node:
                for child_node in node.children():
                    node_path = child_node.path()
                    item = QtWidgets.QTreeWidgetItem(parent)
                    item.setExpanded(True)

                    if child_node.iconName():
                        item.setIcon(0, QtGui.QIcon(child_node.iconName()))

                    item.setText(0, child_node.name())
                    item.setText(1, node_path)
                    self.nodes_map[node_path] = item

                    # connect signals
                    child_node.signals.opCookingStarted.connect(lambda node_path=node_path: self.nodeMarkClean(node_path))
                    child_node.signals.opCookingFailed.connect(lambda node_path=node_path: self.nodeMarkFailed(node_path))

                    if child_node.children():
                        self.createNodeTree(item, child_node.path())

        self.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def handleItemClicked(self, item):
        selected_node_path = str(item.text(1))
        signals.copperNodeSelected[str].emit(selected_node_path)              

    def handleShowInViewer(self, node_path):
        signals.copperSetCompositeViewNode[str].emit(node_path)

    @QtCore.pyqtSlot()   
    def nodeMarkClean(self, node_path):
        '''Marks node as claen (cooking stated, remove all error signs)'''
        pass

    @QtCore.pyqtSlot()   
    def nodeMarkFailed(self, node_path):
        '''Marks node as failed during cooking'''
        item = self.nodes_map[node_path]
        if item:
            #self.itemWidget(item,2).setProperty("failed", True);
            pass

    @QtCore.pyqtSlot()   
    def rebuildNodeTree(self):
        '''Rebuilds node tree upon recieving signals like copperNodeCreated or copperNodeChanged'''
        self.clear()
        self.nodes_map = {}
        self.createNodeTree(self)

    @QtCore.pyqtSlot(str)   
    def nodeSelected(self, node_path):
        for item in self.selectedItems():
            item.setSelected(False)
        item = self.nodes_map[node_path]
        item.setSelected(True)

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

    def mimeData(self, items):
        mime_data = QtCore.QMimeData()
        mime_data.setText(items[0].text(1))
        return mime_data




