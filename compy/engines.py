import sys
import pyopencl as cl
import pickle
import compy.network_manager as network_manager

import re
lastNum = re.compile(r'(?:[^\d]*(\d+)[^\d]*)+')

def increment(s):
    """ look for the last sequence of number(s) in a string and increment """
    m = lastNum.search(s)
    if m:
        next = str(int(m.group(1))+1)
        start, end = m.span(1)
        s = s[:max(end-len(next), start)] + next + s[end:]
    return s

class CLC_Engine(network_manager.CLC_NetworkManager):
	cpu_devices = []
	gpu_devices = []
	programs 	= {}
	viewer		= None	
	app 		= None
	filters		= {}
	time		= 0
	network_cb  = None

	def __init__(self, device_type="GPU", filters={}, cl_path=""): # "cpu" or "gpu" here or "ALL"
		super(CLC_Engine, self).__init__(["comp"]) # only CLC_Composition class nodes allowed to be created at the root/engine level
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
	
	def set_network_change_callback(self, callback):
		self.network_cb = callback

	def call_network_changed_callback(self):
		if self.network_cb:
			print "Calling network change callback..."
			self.network_cb()	 	

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
	
	@property				
	def children(self):
		return self.nodes

	@property 
	def engine(self):
		return self	

	def save_project(self, filename):
		pickle.dump( self.comps, open( filename, "wb"))

	def open_project(self, filename):
		self.nodes = pickle.load( open( filename, "rb"))					