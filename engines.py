import pyopencl as cl

class CLC_Engine():

	def __init__(self, device_id=0):
		self._ctx = cl.create_some_context()
		self._queue = cl.CommandQueue(self._ctx)
		self._mf = cl.mem_flags
	@property
	def ctx(self):
		return self._ctx
		
	@property
	def queue(self):
		return self._queue	

	@property
	def mf(self):
		return self._mf
