import pyopencl as cl
import numpy
import base
import engines

class CLC_Comp_Add(base.CLC_Base):
	'''
		This filter adds foreground over background using OpenCL
	'''
	def __init__(self, engine, width=0, height=0, background = None, foreground = None):
		self.background = background
		self.foreground = foreground

		self.width = self.background.width
		self.height = self.background.height

		self.program = engine.load_program("comp_add.cl")
		super(CLC_Comp_Add, self).__init__(engine, width, height) 
		
	def compute(self):
		if not self.foreground:
			raise BaseException("No foreground specified for %s" % this)
		if not self.background:
			raise BaseException("No background specified for %s" % this)	
		
		self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.WRITE_ONLY, self.image_format, shape=(self.width, self.height))
		
		sampler = cl.Sampler(self.engine.ctx,
				True, #  Normalized coordinates
				cl.addressing_mode.CLAMP_TO_EDGE,
				cl.filter_mode.LINEAR)
		
		
		self.Buffer1 = cl.Image(self.foreground.devOutBuffer)
		self.Buffer2 = cl.Image(self.foreground.devOutBuffer)
		
		exec_evt = self.program.run_add(self.engine.queue, self.size, None, 
			self.Buffer1, 
			self.Buffer2, 
			self.devOutBuffer,
			sampler,
			numpy.int32(self.width),
			numpy.int32(self.height),
		)
		exec_evt.wait()
