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
		self.program = engine.load_program("comp_add.cl")
		self.__inputs__ = [None, None]
		self.__input_names__ = ["Input 1","Input 2"] 
		
	def compute(self):
		self.width, self.height = self.input(0).size
		self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=(self.width, self.height))
		
		sampler = cl.Sampler(self.engine.ctx,
				True, #  Normalized coordinates
				cl.addressing_mode.CLAMP_TO_EDGE,
				cl.filter_mode.LINEAR)
		
		exec_evt = self.program.run_add(self.engine.queue, self.size, None, 
			self.input(0).getOutDevBuffer(), 
			self.input(1).getOutDevBuffer(), 
			self.devOutBuffer,
			sampler,
			numpy.int32(self.width),
			numpy.int32(self.height),
		)
		exec_evt.wait()

class CLC_Comp_Blend(base.CLC_Base):
	'''
		This filter blends foreground over background using OpenCL
	'''
	type_name = "blend"
	category = "comps"
	def __init__(self, engine, parent):
		super(CLC_Comp_Blend, self).__init__(engine, parent)
		self.program = engine.load_program("comp_blend.cl")
		self.__inputs__ = [None, None]
		self.__input_names__ = ["Input 1","Input 2"]

		self.addParameter("factor", float, 0.5) 
		
	def compute(self):
		self.width, self.height = self.input(0).size
		self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=(self.width, self.height))
		
		sampler = cl.Sampler(self.engine.ctx,
				True, #  Normalized coordinates
				cl.addressing_mode.CLAMP_TO_EDGE,
				cl.filter_mode.LINEAR)
		print "Running blend program for node %s" % self.name()
		exec_evt = self.program.run_blend(self.engine.queue, self.size, None, 
			self.input(0).getOutDevBuffer(), 
			self.input(1).getOutDevBuffer(), 
			self.devOutBuffer,
			sampler,
			numpy.int32(self.width),
			numpy.int32(self.height),
			numpy.float32(self.parm("factor").evalAsFloat())
		)
		exec_evt.wait()
		print "Blend program for node %s completed." % self.name()

