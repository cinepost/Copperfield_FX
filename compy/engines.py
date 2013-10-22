import sys
import pyopencl as cl
import pickle
import compy.composition as composition

class CLC_Engine(object):
	cpu_devices = []
	gpu_devices = []
	programs 	= {}
	viewer		= None	
	app 		= None
	filters		= {}
	comps		= {}
	time		= 0

	def __init__(self, device_type="GPU", filters={}, cl_path=""): # "cpu" or "gpu" here or "ALL"
		print "Initializing compositing engine..."
		for found_platform in cl.get_platforms():
			if found_platform.name in ['NVIDIA CUDA', 'ATI Stream', 'Apple']:
				my_platform = found_platform
			else:
				raise BaseException("Unable to found capable OpenCL device!")
		
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
		
		self._queue 	= cl.CommandQueue(self.ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)
		self._mf 		= cl.mem_flags
		self.filters 	= filters
		self.cl_path 	= cl_path
		print "Bundled with filters: %s \n Done." % self.filters	
	
	def load_program(self, filename):
		of = open("%s/%s" % (self.cl_path, filename), 'r')
		return cl.Program(self.ctx, of.read()).build()
		
	@property
	def ctx(self):
		return self._ctx
		
	@property
	def queue(self):
		return self._queue	
		
	@property
	def mf(self):
		return self._mf

	def setTime(self, time):
		self.time = time	
		
	def createNode(self, node_type):
		if node_type in ["comp", "img"]:
			comp = composition.CLC_Composition(self)
			self.comps[node_type] = comp
			return comp
		else:
			print "Invalid node type specified!!!"
			return None
					
	def children(self):
		return self.comps

	def save_project(self, filename):
		pickle.dump( self.comps, open( filename, "wb"))

	def open_project(self, filename):
		self.comps = pickle.load( open( filename, "rb"))					