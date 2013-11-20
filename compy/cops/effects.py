from compy import base, parameter
import pyopencl as cl
import numpy

class CLC_Effect_FastBlur(base.CLC_Base):
	type_name = "fastblur"
	category = "effects"
	def __init__(self, engine, parent):
		super(CLC_Effect_FastBlur, self).__init__(engine, parent)
		self.program = engine.load_program("effects_blur.cl")
		self.__inputs__ = [None]
		self.__input_names__ = ["Input 1"]

		self.addParameter("blursize", float, 0.05)
		self.addParameter("blursizey", float, 0.05)
		self.addParameter("useindepy", bool, True)	
			
	def compute(self):	
		if self.has_inputs():
			self.devTmpBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=self.input(0).size)
			self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=self.input(0).size)	
			self.width = self.input(0).width
			self.height = self.input(0).height
			print "Blurring area: %s x %s" %(self.input(0).width, self.input(0).height)
			exec_evt = self.program.fast_blur_h(self.engine.queue, self.size, None, 
				self.input(0).getOutDevBuffer(),     
				self.devTmpBuffer, 
				numpy.float32(self.parm("blursize").eval()),
				numpy.float32(self.parm("blursizey").eval()),
				numpy.int32(self.input(0).width),
				numpy.int32(self.input(0).height),
				numpy.int32(self.parms("useindepy").eval()),
			)
			exec_evt.wait()
			
			exec_evt = self.program.fast_blur_v(self.engine.queue, self.size, None, 
				self.devTmpBuffer,     
				self.devOutBuffer, 
				numpy.float32(self.parm("blursize").eval()),
				numpy.float32(self.parm("blursizey").eval()),
				numpy.int32(self.input(0).width),
				numpy.int32(self.input(0).height),
				numpy.int32(self.parms("useindepy").eval()),
			)
			exec_evt.wait()
			del self.devTmpBuffer
		else:
			raise BaseException("No input specified !!!")	


class CLC_Effect_PressRaster(base.CLC_Base):
	type_name	= "press_raster"
	category = "effects"
	def __init__(self, engine, parent):
		super(CLC_Effect_PressRaster, self).__init__(engine, parent)
		self.program = engine.load_program("effects_press_raster.cl")
		self.__inputs__ = [None]
		self.__input_names__ = ["Input 1"]	

		self.addParameter("density", float, 100)
		self.addParameter("quality", int, 2)
			
	def compute(self):	
		if self.has_inputs():
			self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=self.inputs.get(0).size)	
			self.width = self.input(0).width
			self.height = self.input(0).height
			print "Raterizing area: %s x %s" %(self.input(0).width, self.input(0).height)
			exec_evt = self.program.raster(self.engine.queue, self.size, None, 
				self.input(0).getOutDevBuffer(),     
				self.devOutBuffer,
				numpy.int32(self.input(0).width),
				numpy.int32(self.input(0).height),
				numpy.float32(self.parm("density").eval()),
				numpy.int32(self.parm("quality").eval()),
			)
			exec_evt.wait()
		else:
			raise BaseException("No input specified !!!")
