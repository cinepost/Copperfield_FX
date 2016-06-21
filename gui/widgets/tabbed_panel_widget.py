from PyQt4 import Qt, QtGui, QtCore
from copper import parameter

from path_bar_widget import PathBarWidget

class TabbedPanelWidget(QtGui.QFrame):
  
    def __init__(self, parent=None, engine=None):      
        super(TabbedPanelWidget, self).__init__(parent)
        self.engine = engine
        self.allowedPanelTypesList = None
        self.setObjectName("tabbedPanel")
        self.initUI()
        
    def initUI(self):
        layout = QtGui.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.tabs = QtGui.QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

        self.tabButton = QtGui.QPushButton(self)
        self.tabButton.setObjectName("plusButton")

        self.plusButtonMenu = QtGui.QMenu(self)
        self.tabButton.setMenu(self.plusButtonMenu)
        self.tabs.setCornerWidget(self.tabButton)

        layout.addWidget(self.tabs)
        self.setLayout(layout)
        self.buildPlusButtonMenu() # Rebuild menu


    def setAllowedPanelTypes(self, typesList):
        self.allowedPanelTypesList = typesList
        self.buildPlusButtonMenu() # Rebuild menu


    def addPaneTab(self, widget, pane_title=None):
        if pane_title:
            panelTitle = pane_title
        else:
            panelTitle = widget.panelTypeName()

        tab_index = self.tabs.addTab(widget, panelTitle)
        self.tabs.tabBar().tabButton(tab_index, QtGui.QTabBar.RightSide).resize(12,12)
        self.buildPlusButtonMenu() # Rebuild menu


    def addNewPaneTab(self):
        currentTabIndex = self.tabs.currentIndex()
        widget = self.tabs.widget(currentTabIndex)
        pane_title = widget.panelTypeName()
        self.addPaneTab(widget.copy(), pane_title)


    def addNewPaneTabByType(self, panelType):
        panelWidget = panelType(self, engine=self.engine)
        self.addPaneTab(panelWidget, panelType.panelTypeName())


    def setActive(self, index):
        self.tabs.setCurrentIndex(index)


    def buildPlusButtonMenu(self):
        if not self.plusButtonMenu.isEmpty():
            self.plusButtonMenu.clear()

        action_new_tab = self.plusButtonMenu.addAction("New Pane Tab")
        action_new_tab.triggered.connect(self.addNewPaneTab)

        new_tab_type_submenu = self.plusButtonMenu.addMenu("New Pane Tab Type")
        if self.allowedPanelTypesList:
            for panel_type in self.allowedPanelTypesList:
                action = new_tab_type_submenu.addAction(panel_type.panelTypeName())
                action.triggered[()].connect(lambda arg=panel_type: self.addNewPaneTabByType(arg))

        self.plusButtonMenu.addSeparator()
        currentTabIndex = self.tabs.currentIndex()
        for index in range(self.tabs.count()):
            action = self.plusButtonMenu.addAction(self.tabs.tabText(index))
            action.setCheckable(True)
            if index is currentTabIndex:
                action.setChecked(True)
            action.triggered[()].connect(lambda arg=index: self.setActive(arg))


