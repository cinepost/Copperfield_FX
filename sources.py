import numpy
import pyopencl as cl
import base
import engines
import matplotlib.image

			
class CLC_Source_Image(base.CLC_Base):
	
	def __init__(self, engine):
		self.parms.update({
			"filename"	: None,		# image file name to read
			"width"		: 640, 		# downscale to this resolution. setting this to 0 uses sources resolution
			"height"	: 480,		# downscale to this resolution. setting this to 0 uses sources resolution
			"flipx"		: False,	# flip image horizontally
			"flipy"		: False,	# flip image vertically
		})
		self.engine = engine
		self.program = self.engine.load_program("source_image.cl")	
		super(CLC_Source_Image, self).__init__(engine)
		
	def loadJPG(self, filename):
		img = matplotlib.image.imread(filename)
		
		self.source_width = img.shape[1]
		self.source_height = img.shape[0]
		
		if self.parms.get("width") != 0:
			self.width = self.parms.get("width")
		else:
			self.width = self.source_width
					
		if self.parms.get("height") != 0:
			self.height = self.parms.get("height") 
		else:
			self.height = self.source_height
			
		r = numpy.array(img[:,:,0],dtype=numpy.int8)
		g = numpy.array(img[:,:,1],dtype=numpy.int8)
		b = numpy.array(img[:,:,2],dtype=numpy.int8)
		
		self.devInBufferR = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, cl.ImageFormat(cl.channel_order.INTENSITY, cl.channel_type.UNORM_INT8), shape=(self.source_width, self.source_height,), pitches=(self.source_width,), hostbuf=r)
		self.devInBufferG = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, cl.ImageFormat(cl.channel_order.INTENSITY, cl.channel_type.UNORM_INT8), shape=(self.source_width, self.source_height,), pitches=(self.source_width,), hostbuf=g)
		self.devInBufferB = cl.Image(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, cl.ImageFormat(cl.channel_order.INTENSITY, cl.channel_type.UNORM_INT8), shape=(self.source_width, self.source_height,), pitches=(self.source_width,), hostbuf=b)


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
		
		if self.parms.get("width") != 0:
			self.width = self.parms.get("width")
		else:
			self.width = self.source_width
					
		if self.parms.get("height") != 0:
			self.height = self.parms.get("height") 
		else:
			self.height = self.source_height
		
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
		imagefile = self.parms.get("imagefile")
		if imagefile:	 
			ext = imagefile.split(".")[-1]
			if ext in ["jpg","JPEG","JPG","jpeg","png","PNG"]:
				self.loadJPG(imagefile)
				self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=(self.width, self.height))
				print "inBuffer size %s, outBuffer size %s" % (self.devInBufferR.size, self.devOutBuffer.size)
				exec_evt = self.program.run_jpg(self.engine.queue, self.size, None, 
					self.devInBufferR, # red channel buffer
					self.devInBufferG, # green channel buffer
					self.devInBufferB, # blue channel buffer
					self.devOutBuffer, 
					numpy.int32(self.source_width),
					numpy.int32(self.source_height),
					numpy.int32(self.width),
					numpy.int32(self.height),
				)
				exec_evt.wait()
			elif ext in ["exr", "EXR"]:
				self.loadEXR(imagefile)
				self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=(self.width, self.height))
				print "inBuffer size %s, outBuffer size %s" % (self.devInBufferR.size, self.devOutBuffer.size)
				exec_evt = self.program.run_exr(self.engine.queue, self.size, None, 
					self.devInBufferR, # red channel buffer
					self.devInBufferG, # green channel buffer
					self.devInBufferB, # blue channel buffer
					self.devInBufferA, # alpha channel buffer      
					self.devOutBuffer, 
					numpy.int32(self.source_width),
					numpy.int32(self.source_height),
					numpy.int32(self.width),
					numpy.int32(self.height),
				)
				exec_evt.wait()
		else:
			raise BaseException("No imagefile specified !!!")	


