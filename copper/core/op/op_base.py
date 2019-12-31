import sys, string
import Imath
from PIL import Image
import pyopencl as cl
import numpy
import logging
import threading
import logging
import copy

from .op_network import OP_Network

from copper.core.parameter import CopperParameter
from copper.core.parameter.parm_template import *

class OP_Base(OP_Network):
	__base__ = True
	
	def __init__(self, engine, parent):
		super(OP_Base, self).__init__(engine, parent)		

	def compute(self):
		logging.debug("Computing %s" % self.path())

	def cookData(self, lock):
		try:
			self.compute(lock, self.engine.openclContext(), self.engine.openclQueue())
		except Exception, e:
			logging.error(str(e))
			return False

		self._needs_to_cook = False
		return True

	def getCookedData(self):
		return self.getOutDevBuffer()

	def getOutDevBuffer(self):		
		return self.devOutBuffer

	def getOutHostBuffer(self):
		device_buffer = self.getOutDevBuffer()
		host_buffer = numpy.empty((self.xRes(), self.yRes(), 4), dtype = numpy.float16)
		self.engine.openclQueue().finish()
		
		quantized_buffer = cl.Image(self.engine.openclContext(), self.engine.mf.READ_WRITE, cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.HALF_FLOAT), shape=self.shape())	
		
		with self.engine.openclQueue() as queue:
			evt = self.common_program.quantize_show(queue, self.shape(), None, device_buffer, quantized_buffer )
			evt.wait()

		with self.engine.openclQueue() as queue:	
			evt = cl.enqueue_copy(queue, host_buffer, quantized_buffer, origin=(0,0), region=self.shape())
			evt.wait()

		return host_buffer

