from compy import base
import pyopencl as cl
import numpy

class CLC_Effect(base.CLC_Base):
	
	def __init__(self, engine):
		self.parms.update({
			"maskinput"	: None,		# use this as operation mask
		})	
		super(CLC_Effect, self).__init__(engine)


class CLC_Effect_FastBlur(CLC_Effect):
	name = "fastblur"
	category = "Effects"
	def __init__(self, engine):
		self.parms.update({
			"blursize"	: 0.05,		# blur diameter for both X and Y in normalized coordinates
			"blursizey"	: 0.05, 	# blur diameter for Y in normalized coordinates
			"useindepy"	: False,	# use independent Y blur diameter
		})
		self.program = engine.load_program("effects_blur.cl")	
		super(CLC_Effect_FastBlur, self).__init__(engine)
			
	def compute(self):	
		if self.inputs.has_key(0):
			self.devTmpBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=self.inputs.get(0).size)
			self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=self.inputs.get(0).size)	
			self.width = self.inputs.get(0).width
			self.height = self.inputs.get(0).height
			print "Blurring area: %s x %s" %(self.inputs.get(0).width, self.inputs.get(0).height)
			exec_evt = self.program.fast_blur_h(self.engine.queue, self.size, None, 
				self.inputs.get(0).get_out_buffer(),     
				self.devTmpBuffer, 
				numpy.float32(self.parms.get("blursize")),
				numpy.float32(self.parms.get("blursizey")),
				numpy.int32(self.inputs.get(0).width),
				numpy.int32(self.inputs.get(0).height),
				numpy.int32(self.parms.get("useindepy")),
			)
			exec_evt.wait()
			
			exec_evt = self.program.fast_blur_v(self.engine.queue, self.size, None, 
				self.devTmpBuffer,     
				self.devOutBuffer, 
				numpy.float32(self.parms.get("blursize")),
				numpy.float32(self.parms.get("blursizey")),
				numpy.int32(self.inputs.get(0).width),
				numpy.int32(self.inputs.get(0).height),
				numpy.int32(self.parms.get("useindepy")),
			)
			exec_evt.wait()
			del self.devTmpBuffer
		else:
			raise BaseException("No input specified !!!")	


class CLC_Effect_PressRaster(CLC_Effect):
	name	= "raster"
	category = "Effects"
	def __init__(self, engine):
		self.parms.update({
			"density"	: 100,		# dots density
			"quality"	: 2,		# dots aa quality 2 is good, but 3 is better
		})
		self.program = engine.load_program("effects_press_raster.cl")	
		super(CLC_Effect_PressRaster, self).__init__(engine)
			
	def compute(self):	
		if self.inputs.has_key(0):
			self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=self.inputs.get(0).size)	
			self.width = self.inputs.get(0).width
			self.height = self.inputs.get(0).height
			print "Raterizing area: %s x %s" %(self.inputs.get(0).width, self.inputs.get(0).height)
			exec_evt = self.program.raster(self.engine.queue, self.size, None, 
				self.inputs.get(0).get_out_buffer(),     
				self.devOutBuffer,
				numpy.int32(self.inputs.get(0).width),
				numpy.int32(self.inputs.get(0).height),
				numpy.float32(self.parms.get("density")),
				numpy.int32(self.parms.get("quality")),
			)
			exec_evt.wait()
		else:
			raise BaseException("No input specified !!!")
