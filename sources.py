import numpy
import pyopencl as cl
import base
import engines

			
class CLC_Source_Image(base.CLC_Base):
	
	def __init__(self, engine, width=0, height=0, imagefile = None):
		self.engine = engine
		if imagefile:
			self.imagefile = imagefile
		
		self.program = self.engine.load_program("source_image.cl")	
		super(CLC_Source_Image, self).__init__(engine, width, height)
		
	def loadJPG(self, filename):
		from PIL import Image
		
		pic = Image.open(self.imagefile)
		self.source_width = pic.size[0]
		self.source_height = pic.size[1]
		temp_buff = numpy.array(pic.convert("RGBA").getdata()).reshape(self.source_width, self.source_height, 4)
		host_buff = temp_buff.astype(numpy.float32)
			
		self.devInBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, self.image_format, shape=(self.source_width, self.source_height,), pitches=(self.source_width * 16,), hostbuf=host_buff)

	def loadEXR(self, filename):
		import OpenEXR
		import Imath
		
		pt = Imath.PixelType(Imath.PixelType.HALF)
		image = OpenEXR.InputFile(filename)
		header = image.header()
		dw = header['dataWindow']
		channels = header['channels']
		size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
		self.source_width = size[0]
		self.source_height = size[1]
		
		redstr = image.channel('R', pt)
		host_buff_r = numpy.fromstring(redstr, dtype = numpy.float16)
		host_buff_r.shape = (size[1], size[0]) # Numpy arrays are (row, col)
		self.devInBufferR = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, cl.ImageFormat(cl.channel_order.INTENSITY, cl.channel_type.HALF_FLOAT), shape=(self.source_width, self.source_height,), pitches=(self.source_width * 2,), hostbuf=host_buff_r)
		
		greenstr = image.channel('G', pt)
		host_buff_g = numpy.fromstring(greenstr, dtype = numpy.float16)
		host_buff_g.shape = (size[1], size[0]) # Numpy arrays are (row, col)
		self.devInBufferG = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, cl.ImageFormat(cl.channel_order.INTENSITY, cl.channel_type.HALF_FLOAT), shape=(self.source_width, self.source_height,), pitches=(self.source_width * 2,), hostbuf=host_buff_g)
		
		bluestr = image.channel('B', pt)
		host_buff_b = numpy.fromstring(bluestr, dtype = numpy.float16)
		host_buff_b.shape = (size[1], size[0]) # Numpy arrays are (row, col)
		self.devInBufferB = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, cl.ImageFormat(cl.channel_order.INTENSITY, cl.channel_type.HALF_FLOAT), shape=(self.source_width, self.source_height,), pitches=(self.source_width * 2,), hostbuf=host_buff_b)
		
		if(channels.get('A') is not None):
			alphastr = image.channel('A', pt)
			host_buff_a = numpy.fromstring(alphastr, dtype = numpy.float16)
			host_buff_a.shape = (size[1], size[0]) # Numpy arrays are (row, col)
			self.devInBufferA = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, cl.ImageFormat(cl.channel_order.INTENSITY, cl.channel_type.HALF_FLOAT), shape=(self.source_width, self.source_height,), pitches=(self.source_width * 2,), hostbuf=host_buff_a)
		else:
			self.devInBufferA = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, cl.ImageFormat(cl.channel_order.INTENSITY, cl.channel_type.HALF_FLOAT), shape=(self.source_width, self.source_height,), pitches=(self.source_width * 2,), hostbuf=numpy.ones(self.source_width * self.source_height, dtype = numpy.float16))
		
			
	def compute(self):
		if self.imagefile:
			
			print "Cooking %s for size %sx%s" % (self, self.width, self.height)
			# Create sampler for sampling image object
			sampler = cl.Sampler(self.engine.ctx,
				True, #  Normalized coordinates
				cl.addressing_mode.CLAMP_TO_EDGE,
				cl.filter_mode.LINEAR)
				
			self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=(self.width, self.height))	
				
			ext = self.imagefile.split(".")[-1]
			if ext in ["jpg","JPEG","JPG","jpeg","png","PNG"]:
				self.loadJPG(self.imagefile)
				print "inBuffer size %s, outBuffer size %s" % (self.devInBuffer.size, self.devOutBuffer.size)
				exec_evt = self.program.run_jpg(self.engine.queue, self.size, None, 
					self.devInBuffer, 
					self.devOutBuffer, 
					sampler, 
					numpy.int32(self.source_width),
					numpy.int32(self.source_height),
					numpy.int32(self.width),
					numpy.int32(self.height),
				)
				exec_evt.wait()
			elif ext in ["exr", "EXR"]:
				self.loadEXR(self.imagefile)
				print "inBuffer size %s, outBuffer size %s" % (self.devInBufferR.size, self.devOutBuffer.size)
				exec_evt = self.program.run_exr(self.engine.queue, self.size, None, 
					self.devInBufferR, # red channel buffer
					self.devInBufferG, # green channel buffer
					self.devInBufferB, # blue channel buffer
					self.devInBufferA, # alpha channel buffer      
					self.devOutBuffer, 
					sampler, 
					numpy.int32(self.source_width),
					numpy.int32(self.source_height),
					numpy.int32(self.width),
					numpy.int32(self.height),
				)
				exec_evt.wait()
		else:
			raise BaseException("No imagefile specified !!!")	


