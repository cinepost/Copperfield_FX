import copy

from copper.vmath import Vector3

from .primitive import Point, Polygon
from copper.geometry.iotranslators.base import GeoIORegistry

class Geometry(object):
	def __init__(self, sop_node=None):
		self._sop_node = sop_node
		self._points = []
		self._prims = []

		self._frozen = False


	def clear(self):
		self._points = []
		self._prims = []

	def raw_points(self):
		return self._points


	def points(self):
		return [Point(self, i) for i in range(len(self._points))]


	def prims(self):
		return self._prims


	def createPoint(self):
		self._points.append([0,0,0])
		return Point(self, len(self._points)-1)


	def sopNode(self):
		return self._sop_node


	def freeze(self):
		"""
		Return another Geometry object that is not linked to a particular SOP.
		"""
		if self._frozen:
			return self
		else:
			frozen_geo = Geometry()
			frozen_geo._points = copy.deepcopy(self._prims)
			frozen_geo._prims = copy.deepcopy(self._points)
			frozen_geo._frozen = True
			return frozen_geo


	def loadFromFile(self, filename):
		GeoIORegistry._registry_by_ext['.obj'].readGeometry(filename, self)


	def saveToFile(self, filename):
		GeoIORegistry._registry_by_ext['.obj'].saveGeometry(filename, self)