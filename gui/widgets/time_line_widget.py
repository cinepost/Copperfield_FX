from PyQt4 import QtGui, QtCore

class TimeLine(QtGui.QGraphicsScene):
    
    def __init__(self, parent=None):      
        super(TimeLine, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.cursor_moves = False 
        self.cursor_width = 10
        self.cursor_pos_x = 0
        self.cursor = QtGui.QGraphicsRectItem(self.cursor_pos_x, 0, self.cursor_width, 26)
        self.cursor.setX(self.cursor_pos_x)
        self.addItem(self.cursor)
   
    def mouseMoveEvent(self, event):
        if self.is_mouse_moves_cursor(event): 
            scene_pos = event.scenePos()
            self.cursor_pos_x = scene_pos.x() - self.cursor_width / 2
            self.cursor.setX( self.cursor_pos_x)

    def mousePressEvent(self, event):
        if self.is_mouse_hits_cursor(event): 
            self.cursor_moves = True

    def mouseReleaseEvent(self, event):
        self.cursor_moves = False                 

    def is_mouse_hits_cursor(self, event):    
        scene_pos_x = event.scenePos().x()
        if scene_pos_x > self.cursor_pos_x and scene_pos_x < self.cursor_pos_x + self.cursor_width:
            return True

    def is_mouse_moves_cursor(self, event):
        scene_pos_x = event.scenePos().x()
        if scene_pos_x > self.cursor_pos_x and scene_pos_x < self.cursor_pos_x + self.cursor_width or self.cursor_moves is True:
            return True

        return False            

class TimeLineWidget(QtGui.QWidget):
    in_frame = 0
    out_frame = 250
    cursor = 0.0

    def __init__(self, parent=None):      
        super(TimeLineWidget, self).__init__(parent)
        self.isPressed = False
        self.setStyleSheet("background-color: rgb(164, 164, 164); border:1px solid rgb(128, 128, 128); border-radius: 1px;")
        self.initUI()
        
    def initUI(self):
        self.setFixedHeight(30)
        
        # Left buttons
        buttons_box = QtGui.QHBoxLayout()
        buttons_box.setContentsMargins(0, 0, 0, 0)
        buttons_box.setSpacing(2)
        
        prev_key_btn = QtGui.QToolButton()
        prev_key_btn.setIcon(QtGui.QIcon('icons/glyphicons_170_step_backward.png'))
        prev_key_btn.setIconSize(QtCore.QSize(24,24))
        prev_key_btn.setStatusTip('Step back one frame')

        play_btn = QtGui.QToolButton()
        play_btn.setIcon(QtGui.QIcon('icons/glyphicons_173_play.png'))
        play_btn.setIconSize(QtCore.QSize(24,24))
        play_btn.setStatusTip('Play')

        next_key_btn = QtGui.QToolButton()
        next_key_btn.setIcon(QtGui.QIcon('icons/glyphicons_178_step_forward.png'))
        next_key_btn.setIconSize(QtCore.QSize(24,24))
        next_key_btn.setStatusTip('Step forward one frame')

        buttons_box.addWidget(prev_key_btn)
        buttons_box.addWidget(play_btn)
        buttons_box.addWidget(next_key_btn)

        # Time line
        timelinebox = QtGui.QHBoxLayout()
        timeline = TimeLine(self)
        timeline = QtGui.QGraphicsView(self)
        timeline.setScene(TimeLine(self))
        timelinebox.addWidget(timeline)

        # Set main layout
        hbox = QtGui.QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addLayout(buttons_box)
        hbox.addLayout(timelinebox)

        self.setLayout(hbox)       