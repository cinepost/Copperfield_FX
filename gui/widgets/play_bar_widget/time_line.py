import logging
from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL

logger = logging.getLogger(__name__)


class CursorItem(QtWidgets.QGraphicsItem):
    def __init__(self, frame=0):      
        QtWidgets.QGraphicsItem.__init__(self)
        #self.setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        #self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)

        self.setX(frame)

    def paint(self, painter, option, widget=None):
        device_scale_factor = 1.0 / painter.deviceTransform().m11()
        
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

        # Draw  box itself
        painter.fillRect(self.boundingRect(), QtGui.QColor(16, 16, 16))

        #font = painter.font()
        #font.setPointSize(4)
        #painter.setFont(font)
        #painter.setPen(QtGui.QColor(192, 192, 192))
        #painter.drawText(self.size().width() / 2 + 1, 1, "0")

    def boundingRect(self):
        return QtCore.QRectF(-10, -10, 100, 100)

    def size(self):
        return QtCore.QSizeF(20, 20)

    def itemChange(self, change, value, direct=True):
        ''' direct argument shows us that shit node wa selected inside the items scene. Otherwise don't propagate copperNodeSelected signal.
            Just change item state.
        '''
        if change == QtWidgets.QGraphicsItem.ItemPositionChange:
            # snap to grid code here
            new_pos = value.toPointF()

            snapped_x = round(new_pos.x())
            
            new_pos.setX(snapped_x)
            
            value = QtCore.QVariant(new_pos)

        return super(CursorItem, self).itemChange(change, value)


class TimeLineScene(QtWidgets.QGraphicsScene):
    
    def __init__(self, parent=None):      
        super(TimeLineScene, self).__init__(parent)
        self.tick_height = 6
        self.start_frame = 1
        self.end_frame = 240
        self.fps = 25
        self.current_frame = 10.0
        self.initUI()

    def initUI(self):
        self.cursor_pos_x = 0
        self.cursor = CursorItem(self.cursor_pos_x)
        self.addItem(self.cursor)
        self.setSceneRect(0, 0, 240, 26)

    def drawBackground(self, painter, rect):
        painter.fillRect(rect, QtGui.QColor(42, 42, 42))

        # Draw frames grid
        left = rect.left() - (rect.left() % 10)
        top = rect.top() - (rect.top() % 10)
 
        lines = []
 
        # x ticks
        x = left
        tick_y1 = ((rect.bottom() - rect.top()) - self.tick_height) / 2
        tick_y2 = ((rect.bottom() - rect.top()) + self.tick_height) / 2
        while x < rect.right():
            lines.append( QtCore.QLineF(x, tick_y1, x, tick_y2) )
            x += 10

        # central line
        center_y = (rect.bottom() - rect.top()) / 2
        lines.append( QtCore.QLineF(rect.left(), center_y, rect.right(), center_y) )

        pen = QtGui.QPen(QtGui.QColor(160, 160, 160), 1)
        pen.setCosmetic(True)
        painter.setPen(pen)
        painter.drawLines(lines)


    #def mousePressEvent(self, event):
    #    self.cursor_moves = True

    #def mouseReleaseEvent(self, event):
    #    self.cursor_moves = False                 


class TimeLineWidget(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):      
        super(TimeLineWidget, self).__init__(parent)
        self.scene = TimeLineScene(self)

        self.initUI()

    def initUI(self):
        self.setObjectName("time_line_widget")

        self.setScene(self.scene)
        self.setFixedHeight(30)
        self.setMouseTracking(True)
        self.setInteractive(True)

        ## No need to see vertical scroll bars in time line view
        self.setHorizontalScrollBarPolicy ( QtCore.Qt.ScrollBarAlwaysOff )
        self.setVerticalScrollBarPolicy ( QtCore.Qt.ScrollBarAlwaysOff )

        format = QtOpenGL.QGLFormat.defaultFormat()
        format.setSampleBuffers(True)
        format.setSamples(16)
        self.setViewport( QtOpenGL.QGLWidget(format) ) # Force OpenGL rendering mode.
        self.setViewportUpdateMode( QtWidgets.QGraphicsView.FullViewportUpdate )

