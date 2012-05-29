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
			#if self.area > 0:
			#	 pic.thumbnail((self.width, self.height), Image.ANTIALIAS)
			self.width = pic.size[0]
			self.height = pic.size[1]
			temp_buff = numpy.array(pic.convert("RGBA").getdata()).reshape(self.width, self.height, 4)
			host_buff = temp_buff.astype(numpy.float32)
			del temp_buff
			
			#self.devInBuffer = cl.Buffer(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, hostbuf=host_buff)
			#self.devOutBuffer = cl.Buffer(self.engine.ctx, self.engine.mf.WRITE_ONLY, self.nbytes)
			
			self.devInBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, self.image_format, shape=(self.width, self.height,), pitches=(self.pitch,), hostbuf=host_buff)
			self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.WRITE_ONLY, self.image_format, shape=(self.width, self.height))
			
			print "Cooking %s for size %sx%s" % (self, self.width, self.height)
			print "inBuffer size %s, outBuffer size %s" % (self.devInBuffer.size, self.devOutBuffer.size)
			exec_evt = self.program.run(self.engine.queue, (self.volume,), None, 
				self.devInBuffer, 
				self.devOutBuffer, 
				numpy.int32(123),
				numpy.int32(123),
				numpy.int32(123),
				numpy.int32(123),
			)
			exec_evt.wait()
			
			#del host_buff
		else:
			raise BaseException("No imagefile specified !!!")	


