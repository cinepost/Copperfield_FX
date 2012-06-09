import sys
import pyopencl as cl
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PyQt4 import QtGui

from viewer import *

class CLC_Engine():
	cpu_devices = []
	gpu_devices = []
	programs 	= {}
	viewer		= None	
	app 		= None
	def __init__(self, device_type="GPU"): # "cpu" or "gpu" here or "ALL"
		print "Initializing compositing engine..."
		for found_platform in cl.get_platforms():
			if found_platform.name in ['NVIDIA CUDA', 'ATI Stream', 'Apple']:
				my_platform = found_platform
			else:
				raise BaseException("Unable to found capable OpenCL GPU")
		
		for found_device in my_platform.get_devices():
			if cl.device_type.to_string(found_device.type) == "GPU":
				self.gpu_devices += [found_device]
			elif cl.device_type.to_string(found_device.type) == "CPU":    
				self.cpu_devices += [found_device]
	
		if self.cpu_devices != []:
			print "Found CPU devices: %s" % self.cpu_devices        
		else:
			print "No CPU devices found"
	
		if self.gpu_devices != []:
			print "Found GPU devices: %s" % self.gpu_devices
		else:
			print "No GPU devices found"
		
		if device_type in ["gpu","GPU","Gpu"]:
			print "Creating engine using GPU devices"
			self._ctx = cl.Context(devices = self.gpu_devices)
		elif device_type in ["cpu","CPU","Cpu"]:
			print "Creating engine using CPU devices"
			self._ctx = cl.Context(devices = self.cpu_devices)
		else:
			print "Creating engine using any type of device"
			self._ctx = cl.Context(devices = self.cpu_devices + self.gpu_devices)
		
		self._queue = cl.CommandQueue(self.ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)
		self._mf = cl.mem_flags
		print "Done."	
	
	def load_program(self, filename):
		of = open("cl/%s" % filename, 'r')
		return cl.Program(self.ctx, of.read()).build()
		
	def display(self, node = None):		
		if not self.app:
			app = QtGui.QApplication(['Compy Node Viewer'])
		
			if not self.viewer:
				# Create viewer instance here
				self.viewer = NodeViewer(node)
				self.viewer.setWindowTitle('View node: %s' % node)
				self.viewer.resize(node.width, node.height)
				self.viewer.show()
				app.exec_()
		
	@property
	def ctx(self):
		return self._ctx
		
	@property
	def queue(self):
		return self._queue	
		
	@property
	def mf(self):
		return self._mf
