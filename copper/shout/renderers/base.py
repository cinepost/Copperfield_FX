class Backet(object):
	def __init__(self):
		pass

class BaseRenderer(object):
	def __init__(self):
		self._output_driver = None

	@property
	def output_driver(self):
		return self._output_driver

	@output_driver.setter
	def output_driver(self, driver):
		self._output_driver = driver

	def renderBucket(self, time=None):
		raise NotImplementedError

	def render(self, time=None):
		raise NotImplementedError
