from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import pyqtSignal

from copper import hou
from copper.core.engine import signals as engine_signals
from copper.core.op.op_node import OP_Node
from copper.ui.signals import signals
from copper.ui.widgets import PathBarWidget

from .base_panel import PathBasedPaneTab

class NodeMimeData(QtCore.QMimeData):
    def __init__(self, node):      
        QtCore.QMimeData.__init__(self)
        self._node_type = node.type()
        self._node_path = node.path()

    def nodeType(self):
        return self._node_type

    def nodePath(self):
        return self._node_path

    def hasFormat(self, fmt):
        if fmt in ["node/path", "node/type"]:
            return True

        return False

class TreeViewPanel(PathBasedPaneTab):
    def __init__(self):      
        PathBasedPaneTab.__init__(self) 

        self.tree_view_widget = TreeViewWidget(self, self)
        self.addWidget(self.tree_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Tree View"


class TreeViewWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent, panel):      
        QtWidgets.QTreeWidget.__init__(self, parent)
        self.panel = panel
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

        ### Connect signals from panel
        self._panel_signals = self.panel.signals
        self._panel_signals.copperNodeCreated.connect(self.rebuildNodeTree)
        self._panel_signals.copperNodeSelected[OP_Node].connect(self.nodeSelected)

        ### Connect internal signals
        #self.connect(self, QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), self.menuContextMenu)
        self.customContextMenuRequested.connect(self.menuContextMenu)
        self.itemClicked.connect(self.handleItemClicked)

    def createNodeTree(self, parent, node=None):
        """Builds node tree from node"""
        if not node:
            # create root node item
            root_node = hou.node("/")
            root_item = QtWidgets.QTreeWidgetItem(self)
            root_item.setExpanded(True)
            root_item.setIcon(0, QtGui.QIcon(root_node.iconName()))
            root_item.setText(0, "/")
            root_item.setText(1, "/")
            root_item.setData(2, Qt.Qt.UserRole, None)
            #self.nodes_map["/"] = root_item
            self.createNodeTree(root_item, root_node)
        else:
            if node:
                for child_node in node.children():
                    node_path = child_node.path()
                    item = QtWidgets.QTreeWidgetItem(parent)
                    item.setExpanded(True)

                    if child_node.iconName():
                        item.setIcon(0, QtGui.QIcon(child_node.iconName()))

                    item.setText(0, child_node.name())
                    item.setText(1, node_path)
                    item.setData(2, Qt.Qt.UserRole, child_node)
                    self.nodes_map[child_node.id()] = item

                    # connect signals
                    child_node.signals.opCookingStarted.connect(lambda node_path=node_path: self.nodeMarkClean(node_path))
                    child_node.signals.opCookingFailed.connect(lambda node_path=node_path: self.nodeMarkFailed(node_path))

                    if child_node.children():
                        self.createNodeTree(item, child_node)

        self.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def handleItemClicked(self, item):
        engine_signals.nodeSelected[OP_Node].emit(item.data(2, Qt.Qt.UserRole))              

    def handleShowInViewer(self, node):
        signals.copperSetCompositeViewNode[OP_Node].emit(node)

    @QtCore.pyqtSlot()   
    def nodeMarkClean(self, node_path):
        '''Marks node as claen (cooking stated, remove all error signs)'''
        pass

    @QtCore.pyqtSlot(OP_Node)   
    def nodeMarkFailed(self, node):
        '''Marks node as failed during cooking'''
        item = self.nodes_map[node.id()]
        if item:
            #self.itemWidget(item,2).setProperty("failed", True);
            pass

    @QtCore.pyqtSlot()   
    def rebuildNodeTree(self):
        '''Rebuilds node tree upon recieving signals like copperNodeCreated or copperNodeChanged'''
        self.clear()
        self.nodes_map = {}
        self.createNodeTree(self)

    @QtCore.pyqtSlot(OP_Node)   
    def nodeSelected(self, node):
        for item in self.selectedItems():
            item.setSelected(False)
        item = self.nodes_map[node.id()]
        item.setSelected(True)

    @QtCore.pyqtSlot()   
    def menuContextMenu(self, point):
        # Infos about the node selected.     
        index = self.indexAt(point)

        if not index.isValid():
            return

        item = self.itemAt(point)
        node = item.data(2, Qt.Qt.UserRole)
        name = item.text(0)  # The text of the node.

        # We build the menu.
        menu=QtGui.QMenu(self)
        action=menu.addAction(name)
        menu.addSeparator()

        action_1=menu.addAction("Show in viewer")
        action_1.triggered.connect(lambda: self.handleShowInViewer(node))

        action_2=menu.addAction("Render")
        #action_2.triggered.connect(lambda: self.workspace.copperRenderNode(node_path))

        action_3=menu.addAction("Delete")
        #action_3.triggered.connect(lambda: self.workspace.copperDeleteNode(node_path))

        menu.exec_(QtGui.QCursor.pos())

    def mimeData(self, items):
        node = items[0].data(2, Qt.Qt.UserRole)
        print("Mime node%s" % node)
        mime_data = NodeMimeData(node)
        return mime_data
