import Image

class COP_Plane(object):
	def __init__(self, parent_cop, channel_names=[], dtype=float):
		self.parent_cop = parent_cop
		self.__channels__ = {}
		self.__dtype__ = dtype

		if len(channel_names) > 0:
			for name in channel_names:
				self.__channels__[name] = None
		else:
			self.__channels__[0] = None		

	def components(self):
		return self.__channels__.keys()

	def getChannel(self, component=None):
		if component:
			return self.__channels__[component]
		else:
			return self.__channels__[0]

	def setChannel(self, img, component=None):
		if component:
			self.__channels__[component] = img
		else:
			self.__channels__[0] = img	

	def setChannelFromString(self, size, img_string, component = None):
		if component:
			self.__channels__[component] = Image.fromstring("L", size, img_string)			
		else:
			self.__channels__[0] = Image.fromstring("L", size, img_string)	
