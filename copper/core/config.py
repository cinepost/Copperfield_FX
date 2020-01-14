from copper.core.utils.singleton import SingletonOptimized as Singleton
 
class Config(metaclass=Singleton):
	'''
	Class used for storing globlas variables
	'''
	def __init__(self):
		self._has_ui = False

	def hasUI(self):
		return self._has_ui