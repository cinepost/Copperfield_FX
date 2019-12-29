from .singleton import SingletonOptmized

class Config(metaclass=SingletonOptmized):
	'''
	Class used for storing globlas variables
	'''
	def __init__(self):
		self._has_ui = False

	def hasUI(self):
		return self._has_ui