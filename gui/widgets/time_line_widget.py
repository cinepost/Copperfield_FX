from PyQt4 import QtGui, QtCore

from collapsable_widget import CollapsableWidget

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
        self.setSceneRect(-1000, -1, 2000, 2)
   
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

class TimeLineWidget(CollapsableWidget):
    def __init__(self, parent=None):
        CollapsableWidget.__init__(self, parent)
        
        self.start_frame = 0
        self.end_frame = 250
        self.current_frame = 0.0

        self.isPressed = False
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
        self.time_line = QtGui.QGraphicsView(self)
        self.time_line.setFixedHeight(30)
        self.time_line.setScene(TimeLine(self))


        self.addLayout(self.buttons_layout)
        self.addWidget(self.time_line)      