from PyQt4 import Qt, QtGui, QtCore
from copper import parameter

from copper_widget import CopperWidget
from path_bar_widget import PathBarWidget

class CopperQTabWidget(QtGui.QTabWidget, CopperWidget):
    def __init__(self, parent):      
        QtGui.QFrame.__init__(self, parent)
        CopperWidget.__init__(self)

class TabbedPanelWidget(QtGui.QFrame, CopperWidget):
  
    def __init__(self, parent=None, engine=None):      
        QtGui.QFrame.__init__(self, parent)
        CopperWidget.__init__(self)
        self.engine = engine
        self.setObjectName("tabbedPanel")
        self.initUI()
        
    def initUI(self):
        layout = QtGui.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.tabs = CopperQTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

        self.tabButton = QtGui.QPushButton(self)
        self.tabButton.setObjectName("plusButton")
        #font = self.tabButton.font()
        #font.setBold(True)
        #self.tabButton.setFont(font)

        self.menu = QtGui.QMenu(self)
        self.tabButton.setMenu(self.menu)
        self.tabs.setCornerWidget(self.tabButton)

        layout.addWidget(self.tabs)
        self.setLayout(layout)


    def addPaneTab(self, widget, pane_title="Untitled"):
        tab = self.tabs.addTab(widget, pane_title)
        self.buildPlusButtonMenu()


    def addNewPaneTab(self):
        currentTabIndex = self.tabs.currentIndex()
        widget = self.tabs.widget(currentTabIndex)
        pane_title = self.tabs.tabText(currentTabIndex)
        self.tabs.addTab(widget.copy(), pane_title)
        self.buildPlusButtonMenu()

    def setActive(self, index):
        print "Setting active tab to: %s" % index
        self.tabs.setCurrentIndex(index)

    def buildPlusButtonMenu(self):
        if not self.menu.isEmpty():
            self.menu.clear()

        action_new_tab = self.menu.addAction("New Pane Tab")
        action_new_tab.triggered.connect(self.addNewPaneTab)

        action_new_tab_type = self.menu.addAction("New Pane Tab Type")
        #action_new_tab_type.triggered.connect(lambda: self.parent.renderNode(node_path))

        self.menu.addSeparator()
        currentTabIndex = self.tabs.currentIndex()
        for index in range(self.tabs.count()):
            action = self.menu.addAction(self.tabs.tabText(index))
            action.setCheckable(True)
            if index is currentTabIndex:
                action.setChecked(True)
            action.triggered[()].connect(lambda arg=index: self.setActive(arg))

