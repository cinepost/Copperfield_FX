import pyopencl as cl
import numpy
import base
import engines

class CLC_Comp_Add(base.CLC_Base):
	'''
		This filter adds foreground over background using OpenCL
	'''
	def __init__(self, engine, width=0, height=0, background = None, foreground = None):
		self.engine = engine
		self.background = background
		self.foreground = foreground

		self.width = self.background.width
		self.height = self.background.height

		self.program = self.load_program("comp_add.cl")
		super(CLC_Comp_Add, self).__init__(engine, width, height) 
		
	def compute(self):
		if not self.foreground:
			raise BaseException("No foreground specified for %s" % this)
		if not self.background:
			raise BaseException("No background specified for %s" % this)	
		
		self.devOutBuffer = cl.Buffer(self.engine.ctx, self.engine.mf.WRITE_ONLY, self.background.volume * 4)
		
		cz = 1
		co = 1
		
		exec_evt = self.program.run(self.engine.queue, (self.width * 3 * self.height,), None, 
			self.background.get_out_buffer(), 
			self.foreground.get_out_buffer(), 
			self.devOutBuffer)
		exec_evt.wait()
