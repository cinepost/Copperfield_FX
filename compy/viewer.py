import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from PyQt4 import QtGui
from OpenGL.GL import *
from OpenGL.GLU import *
import pyopencl as cl

class ViewerWidget(QGLWidget):
	tex = None
    
	def __init__(self, parent, node=None):
		self.node = node
		QGLWidget.__init__(self, parent)
		self.setMinimumSize(node.width / 2, node.height / 2)

	def paintGL(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		
		glBindTexture(GL_TEXTURE_2D, self.tex)
		#glBindBuffer(GL_PIXEL_UNPACK_BUFFER, self.node.devOutBuffer)
		
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_TEXTURE_2D)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		
		glColor3f(1., 1., 1.) 
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0)
		glVertex2f(-1.0, -1.0)
		glTexCoord2f(1.0, 0.0)
		glVertex2f(1.0, -1.0)
		glTexCoord2f(1.0, 1.0)
		glVertex2f(1.0, 1.0)
		glTexCoord2f(0.0, 1.0)
		glVertex2f(-1.0, 1.0)
		glEnd() 
	
		glFlush()

	def resizeGL(self, w, h):
		glViewport(0, 0, w, h)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(0., 1., 0., 1., -w*h, w*h)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		#self.updateGL() 
    
	def initializeGL(self):
		self.tex = glGenTextures (1);
		glBindTexture (GL_TEXTURE_2D, self.tex);
		glTexImage2D (GL_TEXTURE_2D, 0, GL_RGBA, self.node.width, self.node.height, 0, GL_RGBA, GL_FLOAT, None);
		
		#cltex = cl.GLTexture(context, cl.mem_flags.READ_ONLY, GL_TEXTURE_2D, 0, self.tex, 2)
		gluBuild2DMipmaps( GL_TEXTURE_2D, 3, self.node.width, self.node.height, GL_RGBA, GL_FLOAT, self.node.devOutBuffer );
		
		glClearDepth(1.0)
		glClearColor(0.5, 0.5, 0.5, 1.0)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	
		glShadeModel(GL_FLAT)
		glDisable(GL_DITHER)
		glMatrixMode(GL_MODELVIEW)
		glDisable(GL_CULL_FACE)


class NodeViewer(QtGui.QMainWindow):
    
    def __init__(self, node=None):
        QtGui.QMainWindow.__init__(self)
        widget = ViewerWidget(self, node=node)    
        self.setCentralWidget(widget)
