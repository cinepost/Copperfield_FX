import numpy
import pyopencl as cl
from PIL import Image
import base
import engines
			
class CLC_Source_Image(base.CLC_Base):
	
	def __init__(self, engine, width=0, height=0, imagefile = None):
		if imagefile:
			self.imagefile = imagefile
		
		super(CLC_Source_Image, self).__init__(engine, width, height)
		
	def compute(self):
		if self.imagefile:
			pic = Image.open(self.imagefile)
			if self.area > 0:
				 pic.thumbnail((self.width, self.height), Image.ANTIALIAS)
			self.width = pic.size[0]
			self.height = pic.size[1]
			temp_buff = numpy.array(pic.convert("RGB").getdata()).reshape(self.width, self.height, 3)
			host_buff = temp_buff.astype(numpy.float32)
			
			self.devOutBuffer = cl.Buffer(self.engine.ctx, self.engine.mf.READ_ONLY | self.engine.mf.COPY_HOST_PTR, hostbuf=host_buff)

			print "cl_buffer created !!!"
			#del temp_buff
			#del host_buff
		else:
			raise BaseException("No imagefile specified !!!")	


