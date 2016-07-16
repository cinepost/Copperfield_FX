from PyQt4 import QtCore, QtWebKit

from gui.panels.base_panel import BasePanel

class HelpBrowserPanel(BasePanel):
    def __init__(self):      
        BasePanel.__init__(self)   

        self.browser_widget = QtWebKit.QWebView(self)
        self.addWidget(self.browser_widget)

        self.browser_widget.load(QtCore.QUrl('http://cinepost.github.io/Copperfield_FX/'))

    @classmethod
    def panelTypeName(cls):
        return "Help Browser"

    def closeEvent(self, event):
        print "Recieved closeEvent for HelpBroweserPanel"
