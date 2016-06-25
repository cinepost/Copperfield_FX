from PyQt4 import QtGui, QtCore

from gui.widgets import PathBarWidget
from base_panel import BasePanel

class TreeViewPanel(BasePanel):
    def __init__(self, workspace=None, engine=None):      
        BasePanel.__init__(self, workspace=workspace, engine=engine) 

        self.path_bar_widget = PathBarWidget(self, engine=self.engine)
        self.tree_view_widget = TreeViewWidget(self, engine=self.engine, workspace=self.workspace)

        self.setNetworkControlsWidget(self.path_bar_widget)
        self.addWidget(self.tree_view_widget)

    @classmethod
    def panelTypeName(cls):
        return "Tree View"

    @classmethod
    def hasNetworkControls(cls):
        return True


class TreeViewWidget(QtGui.QTreeWidget):
    def __init__(self, parent, engine=None, workspace=None):      
        QtGui.QTreeWidget.__init__(self, parent)

        self.engine = engine
        self.workspace = workspace

        self.current_node = None

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setDragEnabled(True)

        self.setAlternatingRowColors(True)
        vbox = QtGui.QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        
        self.header().close()
        self.createNodeTree(self, self.engine) 

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

                #if cur_node.icon:
                #    item.setIcon(0, cur_node.icon)

                item.setText(0, cur_node.name())
                item.setText(1, cur_node.path())
                if cur_node.children():
                    self.createNodeTree(item, cur_node)  

    def handleItemClicked(self, item, column):
        print "handleItemClicked"
        selected_node_path = str(item.text(1))
        self.workspace.emit(QtCore.SIGNAL('copperNodeSelected'), selected_node_path)              

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
        action_1.triggered.connect(lambda: self.viewer.setNode(node_path))

        action_2=menu.addAction("Render")
        action_2.triggered.connect(lambda: self.parent.renderNode(node_path))

        action_3=menu.addAction("Delete")

        menu.exec_(QtGui.QCursor.pos())  