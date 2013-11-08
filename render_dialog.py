import sys, os, string
from PyQt4 import QtGui, QtCore

class RenderNodeDialog(QtGui.QDialog):
    def __init__(self, parent, node):
        super(RenderNodeDialog, self).__init__(parent)
        self.node = node
        layout = QtGui.QVBoxLayout(self)
        
        # frame range layout
        frm_layout = QtGui.QHBoxLayout()
        self.start_frame = QtGui.QSpinBox(self)
        self.start_frame.setRange(0, 10000)
        self.start_frame.setSingleStep(1)
        self.start_frame.setValue(0)

        self.end_frame = QtGui.QSpinBox(self)
        self.end_frame.setRange(0, 10000)
        self.end_frame.setSingleStep(1)
        self.end_frame.setValue(10)

        self.step_frame = QtGui.QSpinBox(self)
        self.step_frame.setRange(1, 1000)
        self.step_frame.setSingleStep(1)
        self.step_frame.setValue(1)

        frm_layout.addWidget(QtGui.QLabel("Frame range:"))
        frm_layout.addWidget(self.start_frame)
        frm_layout.addWidget(self.end_frame)
        frm_layout.addWidget(self.step_frame)
        frm_layout.addStretch(1)

        # file layout
        file_layout = QtGui.QHBoxLayout()

        self.filename = QtGui.QLineEdit("~/test/%s_$F4.jpg" % node.name())
        self.filename.setMinimumWidth(400)
        self.browser = QtGui.QPushButton("Browse", self)
        self.browser.clicked.connect(self.browse)

        file_layout.addWidget(self.filename)
        file_layout.addWidget(self.browser)

        # buttons layout
        btns_layout = QtGui.QHBoxLayout()   

        self.cancel = QtGui.QPushButton("Cancel", self)
        self.cancel.clicked.connect(self.reject)
        self.render = QtGui.QPushButton("Render", self)
        self.render.clicked.connect(self.renderNode)

        btns_layout.addStretch(1)
        btns_layout.addWidget(self.cancel) 
        btns_layout.addWidget(self.render)

        layout.addLayout(frm_layout)
        layout.addLayout(file_layout)
        layout.addLayout(btns_layout)
        layout.addStretch(1)

        self.setLayout(layout)
        self.setWindowTitle('Render Node Dialog')

    @QtCore.pyqtSlot()    
    def renderNode(self):
        start_frame = self.start_frame.value()
        end_frame = self.end_frame.value()
        step_frame = self.step_frame.value()
        for frame in range(start_frame, end_frame, step_frame):
            self.node.renderToFile(self.filename.text(), frame)

        self.close()    

    @QtCore.pyqtSlot()
    def browse(self):
        filename = str(self.filename.text()).rsplit("/")[-1]
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Browse Directory", self.filename.text(), QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks);    
        self.filename.setText("%s/%s" % (directory, filename))

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def render(parent, node):
        dialog = RenderNodeDialog(parent, node)
        result = dialog.exec_()
        #filename = dialog.dateFilename()
        return True
