from PyQt5 import QtWidgets, QtGui, QtCore, Qt

def clearLayout(layout, delete_widgets=False):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                if delete_widgets:
                    widget.deleteLater()
                else:
                    layout.removeWidget(widget)
                    widget.setParent(None)
            else:
                clearLayout(item.layout(), delete_widgets)
