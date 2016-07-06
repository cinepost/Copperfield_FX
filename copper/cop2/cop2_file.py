from PyQt4 import Qt, QtGui
import matplotlib.image
from PIL import Image 
import pyopencl as cl
import numpy
import os
	
from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import Cop2NodeTypeCategory
from copper.cop2.cop2_node import COP2_Node
from copper import parameter

class COP2_File(COP2_Node):
	
	class NodeType(NodeTypeBase):
		icon_name = 'COP2_file'
		type_name = 'file'
		category = Cop2NodeTypeCategory

	def __init__(self, engine, parent):
		super(COP2_File, self).__init__(engine, parent)
		self.program = self.engine.load_program("source_image.cl")

		self.addParameter("filename", parameter.CopperParmFile, None, label="File")
		self.addParameter("width", parameter.CopperParmInt, 0, label="Width")
		self.addParameter("height", parameter.CopperParmInt, 0, label="Height")
		self.addParameter("flipx", parameter.CopperParmBool, False)
		self.addParameter("flipy", parameter.CopperParmBool, False)
		self.addParameter("startframe", parameter.CopperParmInt, 0, label="Shift to Start Frame")
		self.addParameter("start", parameter.CopperParmInt, 0, label="File Range Start")
		self.addParameter("missingfr", parameter.CopperParmOrderedMenu, 3, label="Missing Frames", menu_items=[
			("closest", "Use Closest Frame"),
			("previous", "Use Previous Frame"),
			("next", "Use Next Frame"),
			("black", "Use Black Frame"),
			("error", "Report Error")
		])

	@classmethod
	def label(cls):
		return "File"

	def loadJPG(self, filename):
		img = matplotlib.image.imread(filename)
		
		self.source_width = img.shape[1]
		self.source_height = img.shape[0]
		
		if self.parm("width").eval() != 0:
			self.image_width = self.parm("width").eval()
		else:
			self.image_width = self.source_width
					
		if self.parm("height").eval() != 0:
			self.image_height = self.parm("height").eval() 
		else:
			self.image_height = self.source_height
			
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
		
		if self.parm("width").eval() != 0:
			self.width = self.parm("width").eval()
		else:
			self.width = self.source_width
					
		if self.parm("height").eval() != 0:
			self.height = self.parm("height").eval() 
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
	
	def getImageFileName(self):
		filename = self.parm("filename").eval()
		image_frame = self.engine.frame() + self.parm("start").evalAsInt() - self.parm("startframe").evalAsInt()
		return filename.expandedString(context={"frame": image_frame})
			
	def compute(self):
		self.log("Computing using CL.")
		imagefile = self.getImageFileName()
		print "READING IMAGE %s" % imagefile
		self.image_width = self.parm("width").eval()
		self.image_height = self.parm("height").eval()

		if os.path.isfile(imagefile):	 
			ext = imagefile.split(".")[-1]
			if ext in ["jpg","JPEG","JPG","jpeg","png","PNG"]:
				self.loadJPG(imagefile)
				self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=(self.image_width, self.image_height))
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
				self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE, self.image_format, shape=(self.image_width, self.image_height))
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
			if self.parm("missingfr").eval() is 4:
				raise BaseException("Image file %s does not exist !!!" % imagefile)
			else:
				# try to find sequence to get resolution frame resolution if
				file_name_pattern = self.parm("filename").eval()

				self.image_width = self.parm("width").eval()
				self.image_height = self.parm("height").eval()
				if 0 in [self.width, self.height]:
					raise BaseException("Image file %s does not exist !!!" % imagefile)

				self.log("Image file %s does not found !!! Using BLACK frame instead." % imagefile)	
				self.devOutBuffer = cl.Image(self.engine.ctx, self.engine.mf.READ_WRITE | self.engine.mf.COPY_HOST_PTR, self.image_format, shape=(self.image_width, self.image_height), hostbuf=numpy.zeros(self.image_width * self.image_height * 4, dtype = numpy.float32))
				

