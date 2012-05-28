import pyopencl as cl
import numpy
import base
import engines

class CLC_Comp(base.CLC_Base):
	devInputBuffers = []
	
	def __init__(self, engine, width, height):
		super(CL_Comp, self).__init__() 


class CLC_Comp_Add(CLC_Comp):
	'''
		This filter adds foreground over background using OpenCL
	'''
	def __init__(self, engine, width=0, height=0, background = None, foreground = None):
		self.engine = engine
		self.background = background
		self.foreground = foreground

		self.prg = cl.Program(self.engine.ctx,
		"""
			__kernel void add(__global const float *a, __global const float *b, __global float *c)
			{
			int gid = get_global_id(0);
			c[gid] = a[gid] + b[gid];
			}
		"""
		).build()

	def compute(self):
		if not self.foreground:
			raise BaseException("No foreground specified for %s" % this)
		if not self.background:
			raise BaseException("No background specified for %s" % this)	
		
		self.width = self.background.width
		self.height = self.background.height
		
		#self.devInputBuffers += self.background.get_out_buffer()
		#self.devInputBuffers += self.foreground.get_out_buffer()
		self.devOutBuffer = cl.Buffer(self.engine.ctx, self.engine.mf.WRITE_ONLY, self.background.area * 3 * 8)
		
		exec_evt = self.prg.add(self.engine.queue, (128 * 3 * 8 * 16, 128), None, self.background.get_out_buffer(), self.foreground.get_out_buffer(), self.devOutBuffer)
		exec_evt.wait()
