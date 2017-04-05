from PyQt4 import QtGui, QtCore

from ..collapsable_widget import CollapsableWidget
from time_line import TimeLineWidget

class PlayBarWidget(CollapsableWidget):
    def __init__(self, parent=None):
        CollapsableWidget.__init__(self, parent)
        self.initUI()
        
    def initUI(self):
        
        # Left buttons
        self.buttons_layout = QtGui.QHBoxLayout()
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_layout.setSpacing(0)
        
        self.prev_key_btn = QtGui.QPushButton()
        self.prev_key_btn.setCheckable(True)
        self.prev_key_btn.setIcon(QtGui.QIcon('icons/glyphicons_170_step_backward.png'))
        self.prev_key_btn.setStatusTip('Step back one frame')

        self.play_btn = QtGui.QPushButton()
        self.play_btn.setCheckable(True)
        self.play_btn.setIcon(QtGui.QIcon('icons/glyphicons_173_play.png'))
        self.play_btn.setStatusTip('Play')

        self.next_key_btn = QtGui.QPushButton()
        self.next_key_btn.setCheckable(True)
        self.next_key_btn.setIcon(QtGui.QIcon('icons/glyphicons_178_step_forward.png'))
        self.next_key_btn.setStatusTip('Step forward one frame')

        self.buttons_layout.addWidget(self.prev_key_btn)
        self.buttons_layout.addWidget(self.play_btn)
        self.buttons_layout.addWidget(self.next_key_btn)

        # Time line
        self.time_line = TimeLineWidget(self)


        self.addLayout(self.buttons_layout)
        self.addWidget(self.time_line)      