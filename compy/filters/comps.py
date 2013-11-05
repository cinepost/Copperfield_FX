from compy import base
import pyopencl as cl
import numpy

class CLC_Comp_Add(base.CLC_Base):
	'''
		This filter adds foreground over background using OpenCL
	'''
	type_name = "add"
	category = "comps"
	def __init__(self, engine, parent):
		super(CLC_Comp_Add, self).__init__(engine, parent)
		self.width = self.background.width
		self.height = self.background.height

		self.program = engine.load_program("comp_add.cl")
		self.__inputs__ = [None, None]
		self.__input_names__ = ["Input 1","Input 2"] 
		
	def compute(self):
		self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.WRITE_ONLY, self.image_format, shape=(self.width, self.height))
		
		sampler = cl.Sampler(self.engine.ctx,
				True, #  Normalized coordinates
				cl.addressing_mode.CLAMP_TO_EDGE,
				cl.filter_mode.LINEAR)
		
		exec_evt = self.program.run_add(self.engine.queue, self.size, None, 
			self.__inputs__[0].get_out_buffer(), 
			self.__inputs__[1].get_out_buffer(), 
			self.devOutBuffer,
			sampler,
			numpy.int32(self.width),
			numpy.int32(self.height),
		)
		exec_evt.wait()
