import numpy

class Copper_Geometry(object):
	def __init__(self, engine, parent):
		super(Copper_Geometry, self).__init__()
		self._points = []
		self._primitives = []