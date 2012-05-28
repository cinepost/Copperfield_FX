from PIL import Image, ImageMath
import engines	
import sources
import comps

class CL_Comp_Add():
	'''
		This filter adds foreground over background using
	'''
	source_a = None	
	source_b = None
	result	 = None 
	
	dev_buffers = {}
	
	prg 	= None
	engine 	= None
	
	def __init__(self, engine, background = None, foreground = None):
		self.engine = engine
		if background:
			self.source_a = background.get_buffer()
		if foreground:
			self.source_b = foreground.get_buffer()
		
		self.result = numpy.empty_like(self.source_a)

		mf = cl.mem_flags
		self.dev_buffers[0] = cl.Buffer(engine.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.source_a)
		self.dev_buffers[1] = cl.Buffer(engine.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.source_b)
		self.dest_buf = cl.Buffer(engine.ctx, mf.WRITE_ONLY, self.result.nbytes)

		self.prg = cl.Program(self.engine.ctx,
		"""
			__kernel void sum(__global const float *a, __global const float *b, __global float *c)
			{
			int gid = get_global_id(0);
			c[gid] = a[gid] + b[gid];
			c[gid] = gid * 1;
			}
		"""
		).build()

	def connect_input(self, input_number, input_layer):
		self.dev_buffers[input_number] = input_layer.get_buffer()
		if input_number == 0:
			self.dev_dest_bufer = cl.Buffer(self.engine.ctx, mf.WRITE_ONLY, self.dev_buffers[0])

	def normalize(self, rgb):
		for i in range(4):
			rgb[...,i]*=255
		return rgb

	def getResult(self):
		return self.result
	
	def showResult(self):
		Image.frombuffer('RGB', self.result.shape[:-1], self.result.astype(numpy.uint8), 'raw', 'RGB', 0, 1).show()

	def cook(self):
		exec_evt = self.prg.sum(self.engine.queue, self.source_a.shape, None, self.dev_buffers[0], self.dev_buffers[1], self.dest_buf)
		exec_evt.wait()
		#cl.enqueue_copy(self.engine.queue, self.result, self.dest_buf)
		cl.enqueue_read_buffer(self.engine.queue, self.dest_buf, self.result).wait()
