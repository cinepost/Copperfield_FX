from copper.ui import PyQt_API
from PyQt5 import QtWidgets, QtGui, QtCore
from copper import parameter

from .panels.panel_registry import PanelRegistry

class Pane(QtWidgets.QFrame):
    def __init__(self, parent=None):      
        super().__init__(parent)
        self.setObjectName("tabbedPanel")

        self.maximized = False

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.tabs = QtWidgets.QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

        ### Corner widget
        self.corner_widget = QtWidgets.QWidget(self)
        self.corner_widget_layout = QtWidgets.QHBoxLayout()
        self.corner_widget_layout.setSpacing(0)
        self.corner_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.corner_widget.setLayout(self.corner_widget_layout) 

        self.plus_button = QtWidgets.QPushButton(self)
        self.plus_button.setIcon(QtGui.QIcon("gui/icons/main/pane-plus.svg"))

        self.plus_button_menu = QtWidgets.QMenu(self)
        self.plus_button.setMenu(self.plus_button_menu)

        self.maximize_button = QtWidgets.QPushButton(self)
        self.maximize_button.setCheckable(True)
        self.maximize_button.setIcon(QtGui.QIcon("gui/icons/main/pane-maximize.svg"))
        self.maximize_button.setStatusTip('Maximize pane')

        self.arrow_button = QtWidgets.QPushButton(self)
        self.arrow_button.setIcon(QtGui.QIcon("gui/icons/main/pane-arrow.svg"))

        self.corner_widget_layout.addWidget(self.plus_button)
        self.corner_widget_layout.addStretch(100)
        self.corner_widget_layout.addWidget(self.maximize_button)
        self.corner_widget_layout.addWidget(self.arrow_button)

        self.corner_widget.setSizePolicy( QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred ))

        self.tabs.setCornerWidget(self.corner_widget)

        ###
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        self.buildPlusButtonMenu() # Rebuild menu

    def _addPanel(self, panel, pane_title=None):
        if pane_title:
            panelTitle = pane_title
        else:
            panelTitle = panel.panelTypeName()

        tab_index = self.tabs.addTab(panel, panelTitle)
        
        try:
            self.tabs.tabBar().tabButton(tab_index, QtWidgets.QTabBar.RightSide).resize(12,12)
        except:
            pass
        
        self.buildPlusButtonMenu() # Rebuild menu
        return tab_index

    @QtCore.pyqtSlot()
    def addNewPaneTab(self):
        currentTabIndex = self.tabs.currentIndex()
        panel = self.tabs.widget(currentTabIndex)
        pane_title = panel.panelTypeName()
        self._addPanel(panel.copyPanel(), pane_title)

    @QtCore.pyqtSlot()
    def addNewPaneTabByType(self, panel_type_name):
        panelWidgetClass = PanelRegistry[panel_type_name]
        
        if panelWidgetClass:
            panelWidget = panelWidgetClass()
            tab_index = self._addPanel(panelWidget, panelWidget.panelTypeName())
            self.tabs.tabBar().setCurrentIndex(tab_index)

    def setActive(self, index):
        self.tabs.setCurrentIndex(index)


    def buildPlusButtonMenu(self):
        from .panels.panel_registry import PanelRegistry

        if not self.plus_button_menu.isEmpty():
            self.plus_button_menu.clear()

        action_new_tab = self.plus_button_menu.addAction("New Pane Tab")
        action_new_tab.triggered.connect(self.addNewPaneTab)

        new_tab_type_submenu = self.plus_button_menu.addMenu("New Pane Tab Type")

        for panel_type_name in PanelRegistry._registry:
            action = new_tab_type_submenu.addAction(PanelRegistry._registry[panel_type_name].panelTypeName())
            action.setCheckable(False)
            action.triggered.connect(lambda checked, arg=panel_type_name: self.addNewPaneTabByType(arg))

        self.plus_button_menu.addSeparator()
        currentTabIndex = self.tabs.currentIndex()
        for index in range(self.tabs.count()):
            action = self.plus_button_menu.addAction(self.tabs.tabText(index))
            action.setCheckable(True)
            if index is currentTabIndex:
                action.setChecked(True)
            action.triggered.connect(lambda checked, arg=index: self.setActive(arg))

    # standard hou stuff

    #def tabs(self):
    #    '''
    #    Return the pane tabs in this pane.
    #    '''
    #    return [self.tabs.widget(index) for index in range(self.tabs.count())]