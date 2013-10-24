from PyQt4 import QtGui, QtCore

class TreeNodeViewerWidget(QtGui.QTreeWidget):
  
    def __init__(self, parent=None, engine=None):      
        super(TreeNodeViewerWidget, self).__init__(parent)
        self.engine = engine
        
        self.connect(self, QtCore.SIGNAL("network_changed"), self.rebuild)

        self.initUI()
        
    def initUI(self):
        header=QtGui.QTreeWidgetItem(["Type","Name"])
        self.setHeaderItem(header) 
        #layout = QtGui.QVBoxLayout()
        #self.label = QtGui.QLabel('Test')
        #layout.addWidget(self.label)
        #self.setLayout(layout)

    def createNodeLevel(self, node, parent_widget):
        for node_name in node.children.keys():
            cur_node = node.children[node_name]
            item = QtGui.QTreeWidgetItem(parent_widget)
            item.setText(0, str(cur_node))
            item.setText(1, cur_node.name)
            if cur_node.children:
                self.createNodeLevel(cur_node, item)    

    @QtCore.pyqtSlot()   
    def rebuild(self):
        self.createNodeLevel(self.engine, self)
        
