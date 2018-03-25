import logging

from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets

from gui.panels.base_panel import BasePanel

logger = logging.getLogger(__name__)


class HelpBrowserPanel(BasePanel):
    def __init__(self):      
        BasePanel.__init__(self)   

        self.browser_widget = QtWebEngineWidgets.QWebEngineView(self)
        self.addWidget(self.browser_widget)

        self.browser_widget.load(QtCore.QUrl('http://cinepost.github.io/Copperfield_FX/'))

    @classmethod
    def panelTypeName(cls):
        return "Help Browser"

    def closeEvent(self, event):
        logger.debug("Recieved closeEvent for HelpBroweserPanel")
