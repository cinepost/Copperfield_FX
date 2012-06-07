import numpy
import pyopencl as cl
from PIL import Image
import base
import engines
			
class CLC_Source_Image(base.CLC_Base):
	
	def __init__(self, engine, width=0, height=0, imagefile = None):
		self.engine = engine
		if imagefile:
			self.imagefile = imagefile
		
		self.program = self.engine.load_program("source_image.cl")	
		super(CLC_Source_Image, self).__init__(engine, width, height)
		
	def compute(self):
		if self.imagefile:
			pic = Image.open(self.imagefile)
			source_width = pic.size[0]
			source_height = pic.size[1]
			temp_buff = numpy.array(pic.convert("RGBA").getdata()).reshape(source_width, source_height, 4)
			host_buff = temp_buff.astype(numpy.float32)
			del temp_buff
			
			self.devInBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, self.image_format, shape=(source_width, source_height,), pitches=(source_width * 16,), hostbuf=host_buff)
			self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.WRITE_ONLY, self.image_format, shape=(self.width, self.height))
			
			print "Cooking %s for size %sx%s" % (self, self.width, self.height)
			print "inBuffer size %s, outBuffer size %s" % (self.devInBuffer.size, self.devOutBuffer.size)
			
			# Create sampler for sampling image object
			sampler = cl.Sampler(self.engine.ctx,
				True, #  Normalized coordinates
				cl.addressing_mode.CLAMP_TO_EDGE,
				cl.filter_mode.LINEAR)

			
			exec_evt = self.program.run(self.engine.queue, self.size, None, 
				self.devInBuffer, 
				self.devOutBuffer, 
				sampler, 
				numpy.int32(source_width),
				numpy.int32(source_height),
				numpy.int32(self.width),
				numpy.int32(self.height),
			)
			exec_evt.wait()
			
			#del host_buff
		else:
			raise BaseException("No imagefile specified !!!")	


