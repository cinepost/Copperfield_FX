from PyQt4 import QtGui, QtCore, Qt
import compy

class NodeViewerWidget(QtGui.QWidget):

    def __init__(self, parent):
        super(NodeViewerWidget, self).__init__(parent=parent)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.makeScene()
        self.addBlock(10, 10, 'Block1', (70, 70, 170), {})


        ## First create engine
        engine = compy.CreateEngine("GPU")
        ## Create composition
        comp = engine.createNode("comp")
        ## Create source layer
        layer1 = comp.createNode("file")
        layer1.setPos(10, 10)
        layer1.setParms({"width": 1920, "height": 1200, "imagefile": "~/Pictures/ava_05.png"})

        self.makeBlockFromNode(layer1)


    def makeScene(self):

        self.scene = BlockScene(0, 0, self.minimumWidth(), self.minimumHeight(), self)
        self.view = QtGui.QGraphicsView(self.scene)
        self.view.setAlignment(QtCore.Qt.AlignAbsolute)
        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.view)
        self.setLayout(layout)

    def addBlock(self, x, y, title, color, params):

        self.scene.addBlock(x=x, y=y, text=title, color=color, params=params)

    def makeBlockFromNode(self, node):
        print node
        print node.__dict__
        self.addBlock(node.x_pos, node.y_pos, node.name, node.color, params=node.parms)


class BlockScene(QtGui.QGraphicsScene):

    def __init__(self, *args, **kwargs):
        super(BlockScene, self).__init__(*args)
        self.setBackgroundBrush(QtGui.QColor(0, 0, 0))
        self.selected_blocks = []
        self.move_mode = False

    def addBlock(self, x, y, text='', color=(70, 70, 70), params={}):
        Block(x=x, y=y, w=70, h=50, text=text, color=color, params=params, scene=self)

    def mouseReleaseEvent(self, event):
        for item in self.items():
            if isinstance(item, Connection):
                print item
        super(BlockScene, self).mouseReleaseEvent(event)


class Block(QtGui.QGraphicsItemGroup):

    def __init__(self, **kwargs):

        super(Block, self).__init__(scene=kwargs['scene'])

        self.setPos(kwargs['x'], kwargs['y'])
        self.setFlags(QtGui.QGraphicsItem.ItemIsMovable | QtGui.QGraphicsItem.ItemIsSelectable | QtGui.QGraphicsItem.ItemIsFocusable)
        self.w = kwargs['w']
        self.h = kwargs['h']
        self.properties = kwargs.get('params')
        self.text = kwargs['text']

        self.selected = False
        self.inputs = []
        self.outputs = []
        self.head_height = 20
        self.socket_number = 5
        self.arrows = {}
        self.sockets = {}
        print kwargs['color']
        self.head_color = QtGui.QColor(*kwargs['color']) if 'color' in kwargs else QtGui.QColor(70, 70, 70)
        self.head_selected_color = QtGui.QColor(70, 200, 70)
        self.body_color = QtGui.QColor(200, 0, 0)
        self.border_color = QtGui.QColor(100, 50, 20)
        self.text_font = QtGui.QFont('Decorative', 10)
        self.triangle_pen = QtGui.QPen(QtGui.QColor(70, 200, 70), 2)


        self.head = QtGui.QGraphicsRectItem(0, 0, self.w, self.head_height,  parent=self, scene=self.scene())
        self.head.setBrush(self.head_color)


        self.title = QtGui.QGraphicsSimpleTextItem(self.text, scene=self.scene(), parent=self)
        self.title.setFont(self.text_font)
        self.title.setPos(3, 5)

        self.property_text = '\n'.join(['%s: %s' % (k, str(v)) for k, v in self.properties.iteritems()]) if self.properties else ''

        self.body = QtGui.QGraphicsRectItem(0, self.head_height, self.w, self.h, parent=self, scene=self.scene())
        self.body.setBrush(self.body_color)

        self.pop_text = QtGui.QGraphicsSimpleTextItem(self.property_text, scene=self.scene(), parent=self)
        self.pop_text.setFont(self.text_font)
        self.pop_text.setPos(3, self.head_height+5)

        self.rect = QtGui.QGraphicsRectItem(0, 0, self.w, self.h+self.head_height, parent=self, scene=self.scene())
        self.rect.setPen(self.border_color)

        self.addToGroup(self.head)
        self.addToGroup(self.title)
        self.addToGroup(self.body)
        self.addToGroup(self.rect)

        self.generate_sockets()


    @property
    def connections(self):
        return self.inputs + self.outputs

    def find_connection(self, block):
        for conn in self.connections:
            if conn.output == block or conn.input == block:
                return True
        return False


    def generate_sockets(self):

        w = self.w
        h = self.h+self.head_height
        dw = w / (self.socket_number + 1)
        dh = h / (self.socket_number + 1)

        if not self.arrows:
            self.arrows['head'] = [None for i in xrange(1, self.socket_number+1)]
            self.arrows['bottom'] = [None for i in xrange(1, self.socket_number+1)]
            self.arrows['left'] = [None for i in xrange(1, self.socket_number+1)]
            self.arrows['right'] = [None for i in xrange(1, self.socket_number+1)]

        if not self.sockets:
            self.sockets['head'] = [{'coord': (self.x() + dw * i, self.y()-5), 'connections': 0} for i in xrange(1, self.socket_number+1)]
            self.sockets['bottom'] = [{'coord': (self.x() + dw * i, self.y()+h+5), 'connections': 0} for i in xrange(1, self.socket_number+1)]
            self.sockets['left'] = [{'coord': (self.x()-5, self.y() + dh * i), 'connections': 0} for i in xrange(1, self.socket_number+1)]
            self.sockets['right'] = [{'coord': (self.x()+w+5, self.y() + dh * i), 'connections': 0} for i in xrange(1, self.socket_number+1)]

        for side in self.sockets:
            for index in range(0, self.socket_number):
                self.remove_arrow(side, index)

    def rebind_sockets(self):
        w = self.w
        h = self.h+self.head_height
        dw = w / (self.socket_number + 1)
        dh = h / (self.socket_number + 1)


        self.sockets['head'] = [{'coord': (self.x() + dw * i, self.y()-5), 'connections': self.sockets['head'][i-1]['connections']} for i in xrange(1, self.socket_number+1)]
        self.sockets['bottom'] = [{'coord': (self.x() + dw * i, self.y()+h+5), 'connections': self.sockets['bottom'][i-1]['connections']} for i in xrange(1, self.socket_number+1)]
        self.sockets['left'] = [{'coord': (self.x()-5, self.y() + dh * i), 'connections': self.sockets['left'][i-1]['connections']} for i in xrange(1, self.socket_number+1)]
        self.sockets['right'] = [{'coord': (self.x()+w+5, self.y() + dh * i), 'connections': self.sockets['right'][i-1]['connections']} for i in xrange(1, self.socket_number+1)]

    def add_arrow(self, side, index):
        if side == 'left':
            p1 = Qt.QPointF(self.sockets[side][index]['coord'][0], self.sockets[side][index]['coord'][1]-4)
            p2 = Qt.QPointF(self.sockets[side][index]['coord'][0]+5, self.sockets[side][index]['coord'][1])
            p3 = Qt.QPointF(self.sockets[side][index]['coord'][0], self.sockets[side][index]['coord'][1]+4)
        elif side == 'right':
            p1 = Qt.QPointF(self.sockets[side][index]['coord'][0], self.sockets[side][index]['coord'][1]-4)
            p2 = Qt.QPointF(self.sockets[side][index]['coord'][0]-5, self.sockets[side][index]['coord'][1])
            p3 = Qt.QPointF(self.sockets[side][index]['coord'][0], self.sockets[side][index]['coord'][1]+4)
        elif side == 'head':
            p1 = Qt.QPointF(self.sockets[side][index]['coord'][0]-4, self.sockets[side][index]['coord'][1])
            p2 = Qt.QPointF(self.sockets[side][index]['coord'][0], self.sockets[side][index]['coord'][1]+5)
            p3 = Qt.QPointF(self.sockets[side][index]['coord'][0]+4, self.sockets[side][index]['coord'][1])
        elif side == 'bottom':
            p1 = Qt.QPointF(self.sockets[side][index]['coord'][0]-4, self.sockets[side][index]['coord'][1])
            p2 = Qt.QPointF(self.sockets[side][index]['coord'][0], self.sockets[side][index]['coord'][1]-5)
            p3 = Qt.QPointF(self.sockets[side][index]['coord'][0]+4, self.sockets[side][index]['coord'][1])

        triangle = QtGui.QGraphicsPolygonItem(QtGui.QPolygonF([p1, p2, p3, p1]),  scene=self.scene())
        triangle.setPen(self.triangle_pen)
        self.addToGroup(triangle)
        return triangle

    def remove_arrow(self, side, index):
        if self.arrows[side][index]:
            self.removeFromGroup(self.arrows[side][index])
            self.scene().removeItem(self.arrows[side][index])
            self.arrows[side][index] = None
            self.arrows[side][index] = None

    def decrease_socket_connection(self, side, index):

        self.sockets[side][index]['connections'] -= 1
        if self.sockets[side][index]['connections'] < 1:
            self.remove_arrow(side, index)

    def select_socket(self, side):

        self.rebind_sockets()

        min_connections = (None, 99999)
        index = -1
        min_index = 0
        for socket in self.sockets[side]:
            index += 1
            if socket['connections'] < min_connections[1]:
                min_connections = (socket['coord'], socket['connections'])
                min_index = index

        self.sockets[side][min_index]['connections'] += 1
        return min_connections[0], min_index



    def mouseReleaseEvent(self, event):

        scene = self.scene()

        if scene.move_mode:
            scene.move_mode = False
        else:
            self.select()
            if self not in scene.selected_blocks:
                scene.selected_blocks.append(self)
            else:
                scene.selected_blocks.remove(self)

            blocks = scene.selected_blocks

            if len(blocks) > 1:
                other_block = blocks[0] if blocks[0] != self else blocks[1]
                if not self.find_connection(other_block):
                    output = blocks[0]
                    input = blocks[1]
                    connection = Connection(output = output,
                                            input = input,
                                            scene=self.scene())
                    scene.addItem(connection)
                    scene.selected_blocks = []
                    output.connections.append(connection)

                    if other_block == input:
                        other_block.inputs.append(connection)
                        self.outputs.append(connection)
                    else:
                        other_block.outputs.append(connection)
                        self.inputs.append(connection)

                    output.select()
                    input.select()

        super(Block, self).mouseReleaseEvent(event)


    def unconnect(self, connection):
        if connection in self.inputs:
            self.inputs.remove(connection)
        elif connection in self.outputs:
            self.outputs.remove(connection)


    def mouseMoveEvent(self, event):
        scene = self.scene()
        scene.move_mode = True
        super(Block, self).mouseMoveEvent(event)
        self.selected = False
        self.head.setBrush(self.head_color)
        self.generate_sockets()

        for conn in self.connections:
            conn.setLine(conn.x1, conn.y1, conn.x2, conn.y2)

    def select(self):
        if not self.selected:
            self.selected = True
            self.setSelected(True)
            self.head.setBrush(self.head_selected_color)
        else:
            self.selected = False
            self.setSelected(False)
            self.head.setBrush(self.head_color)

    def keyReleaseEvent(self, event):
        if event.matches(Qt.QKeySequence.Delete) or event.matches(Qt.QKeySequence.Back):
            self.hide()
            for conn in self.connections:
                self.scene().removeItem(conn)
            self.scene().selected_blocks = []
            self.scene().removeItem(self)


class Connection(QtGui.QGraphicsLineItem):

    def __init__(self, output, input, parent=None, scene=None):
        self.output = output
        self.input = input
        self.index_input = None
        self.index_output = None
        self.x2 = None
        self.y2 = None
        self.side_input = None
        self.selected = False
        self.color = QtGui.QColor(70, 200, 70)
        self.selected_color = QtGui.QColor(150, 90, 70)

        self.calc_coordinates()
        super(Connection, self).__init__(self.x1, self.y1, self.x2, self.y2, parent=parent, scene=scene)
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable | QtGui.QGraphicsItem.ItemIsFocusable)
        self.setPen(QtGui.QPen(self.color, 2))


    def setLine(self, *__args):
        self.calc_coordinates()
        super(Connection, self).setLine(*__args)


    def calc_coordinates(self):

        side_input, side_output = None, None

        if self.output.x() > self.input.x() + self.input.w:
            side_input = 'right'
        elif self.output.x() > self.input.x() and self.output.x() <= self.input.x() + self.input.w:
            if self.output.y() + self.output.h + self.output.head_height < self.input.y():
                side_input = 'head'
            else:
                side_input = 'bottom'
        else:
            side_input = 'left'


        if self.output.x() > self.input.x() + self.input.w:
            side_output = 'left'
        elif self.output.x() > self.input.x() and self.output.x() <= self.input.x() + self.input.w:
            if self.output.y() + self.output.h + self.output.head_height < self.input.y():
                side_output = 'bottom'
            else:
                side_output = 'head'
        else:
            side_output = 'right'


        # inputs

        if self.index_input is not None and self.side_input is not None:

            if self.input.sockets[self.side_input][self.index_input]['connections'] > 0:
                self.input.decrease_socket_connection(self.side_input, self.index_input)

        coords, index_input = self.input.select_socket(side_input)

        if self.side_input and self.index_input is not None:
            if self.side_input != side_input or self.index_input != index_input:
                if self.input.sockets[self.side_input][self.index_input]['connections'] > 0:
                    self.input.decrease_socket_connection(self.side_input, self.index_input)


        self.x2 = coords[0]
        self.y2 = coords[1]
        self.side_input = side_input
        self.index_input = index_input

        if not self.input.arrows[self.side_input][self.index_input]:
            self.input.arrows[self.side_input][self.index_input] = self.input.add_arrow(self.side_input, self.index_input)

        # outputs

        if self.index_output is not None:
            if self.output.sockets[self.side_output][self.index_output]['connections'] > 0:
                self.output.decrease_socket_connection(self.side_output, self.index_output)

        coords, index_output = self.output.select_socket(side_output)
        self.x1 = coords[0]
        if side_output == 'right':
            self.x1 -= 4
        if side_output == 'left':
            self.x1 += 4
        self.y1 = coords[1]
        if side_output == 'head':
            self.y1 += 4
        if side_output == 'bottom':
            self.y1 -= 4
        self.side_output = side_output
        self.index_output = index_output

    def select(self):
        if not self.selected:
            self.selected = True
            self.setSelected(True)
            self.setPen(QtGui.QPen(self.selected_color, 2))
        else:
            self.selected = False
            self.setSelected(False)
            self.setPen(QtGui.QPen(self.color, 2))

    def mouseReleaseEvent(self, event):
        self.select()
        super(Connection, self).mouseReleaseEvent(event)

    def keyReleaseEvent(self, event):
        if event.matches(Qt.QKeySequence.Delete) or event.matches(Qt.QKeySequence.Back):
            self.input.decrease_socket_connection(self.side_input, self.index_input)
            self.output.decrease_socket_connection(self.side_output, self.index_output)
            self.output.unconnect(self)
            self.input.unconnect(self)
            self.scene().removeItem(self)