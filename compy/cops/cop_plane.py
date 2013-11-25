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
