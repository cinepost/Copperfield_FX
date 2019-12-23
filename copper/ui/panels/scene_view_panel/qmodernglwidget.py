import logging
from PyQt5 import QtWidgets, QtGui, QtCore, QtOpenGL, Qt
from OpenGL.GL import *
from OpenGL import GL
from OpenGL.GLU import *
import moderngl

logger = logging.getLogger(__name__)


class QModernGLWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, parent=None):
        super(QModernGLWidget, self).__init__(parent)
        fmt = QtGui.QSurfaceFormat()
        fmt.setVersion(3, 3)
        fmt.setProfile(QtGui.QSurfaceFormat.CoreProfile)
        fmt.setDepthBufferSize(24)
        fmt.setSwapInterval(0)
        fmt.setSamples(8)
        self.setFormat(fmt)

    def initializeGL(self):
        pass

    def resizeGL(self, width, height):
        pass

    def paintGL(self):
        self.ctx = moderngl.create_context()
        self.screen = self.ctx.detect_framebuffer(self.defaultFramebufferObject())
        self.init()

        self.resize(self.ctx.viewport[2],self.ctx.viewport[3])

        self.render()
        self.paintGL = self.render
        self.resizeGL = self.resize

    def init(self):
        pass

    def render(self):
        pass

    def resize(self, width, height):
        pass