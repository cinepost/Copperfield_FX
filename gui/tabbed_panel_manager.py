from PyQt4 import Qt, QtGui, QtCore
from copper import parameter

class TabbedPanelManager(QtGui.QFrame):
    def __init__(self, parent=None):      
        QtGui.QFrame.__init__(self, parent)
        self.allowedPanelTypesList = None
        self.setObjectName("tabbedPanel")

        self.layout = QtGui.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.tabs = QtGui.QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

        ### Corner widget

        self.corner_widget = QtGui.QWidget(self)
        self.corner_widget_layout = QtGui.QHBoxLayout()
        self.corner_widget_layout.setSpacing(0)
        self.corner_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.corner_widget.setLayout(self.corner_widget_layout) 

        self.plus_button = QtGui.QPushButton(self)
        self.plus_button.setObjectName("plusButton")

        self.plus_button_menu = QtGui.QMenu(self)
        self.plus_button.setMenu(self.plus_button_menu)

        self.arrow_button = QtGui.QPushButton(self)
        self.arrow_button.setObjectName("arrowButton")

        self.corner_widget_layout.addWidget(self.plus_button)
        self.corner_widget_layout.addStretch(100)
        self.corner_widget_layout.addWidget(self.arrow_button)

        self.corner_widget.setSizePolicy( QtGui.QSizePolicy( QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred ))

        self.tabs.setCornerWidget(self.corner_widget)

        ###

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        self.buildPlusButtonMenu() # Rebuild menu


    def setAllowedPanelTypes(self, typesList):
        self.allowedPanelTypesList = typesList
        self.buildPlusButtonMenu() # Rebuild menu


    def _addPanel(self, panel, pane_title=None):
        if pane_title:
            panelTitle = pane_title
        else:
            panelTitle = panel.panelTypeName()

        tab_index = self.tabs.addTab(panel, panelTitle)
        self.tabs.tabBar().tabButton(tab_index, QtGui.QTabBar.RightSide).resize(12,12)
        self.buildPlusButtonMenu() # Rebuild menu
        return tab_index

    def panels(self):
        panels = []
        for index in range(self.tabs.count()):
            panels += [self.tabs.widget(index)]

        return panels

    @QtCore.pyqtSlot()
    def addNewPaneTab(self):
        currentTabIndex = self.tabs.currentIndex()
        panel = self.tabs.widget(currentTabIndex)
        pane_title = panel.panelTypeName()
        self._addPanel(panel.copy(), pane_title)

    @QtCore.pyqtSlot()
    def addNewPaneTabByType(self, panelType):
        panelWidget = panelType()
        tab_index = self._addPanel(panelWidget, panelType.panelTypeName())
        self.tabs.tabBar().setCurrentIndex(tab_index)


    def setActive(self, index):
        self.tabs.setCurrentIndex(index)


    def buildPlusButtonMenu(self):
        if not self.plus_button_menu.isEmpty():
            self.plus_button_menu.clear()

        action_new_tab = self.plus_button_menu.addAction("New Pane Tab")
        action_new_tab.triggered.connect(self.addNewPaneTab)

        new_tab_type_submenu = self.plus_button_menu.addMenu("New Pane Tab Type")
        if self.allowedPanelTypesList:
            for panel_type in self.allowedPanelTypesList:
                action = new_tab_type_submenu.addAction(panel_type.panelTypeName())
                action.triggered[()].connect(lambda arg=panel_type: self.addNewPaneTabByType(arg))

        self.plus_button_menu.addSeparator()
        currentTabIndex = self.tabs.currentIndex()
        for index in range(self.tabs.count()):
            action = self.plus_button_menu.addAction(self.tabs.tabText(index))
            action.setCheckable(True)
            if index is currentTabIndex:
                action.setChecked(True)
            action.triggered[()].connect(lambda arg=index: self.setActive(arg))


