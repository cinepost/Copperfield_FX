import os
import copy
import numpy as np

from copper.vmath import Vector3

from .primitive import Point, Polygon
from copper.geometry.iotranslators.base import GeoIORegistry


class FrozenGeometryMedifyExcpetion(Exception):
	def __init__(self):
		Exception.__init__(self, "Cannot modify frozen geometry !") 

def check_frozen(f):
	def wrapper(*args):
		if args[0]._frozen:
			raise FrozenGeometryMedifyExcpetion()
		
		return f(*args)
	
	return wrapper

class Geometry(object):
	def __init__(self, sop_node=None):
		self._sop_node = sop_node
		self.clear()

		self._frozen = False


	def clear(self):
		self._data = np.empty(shape=0, dtype={'names':['P', 'N'], 'formats':['3f4','3f4']})
		self._points = self._data['P'].view()
		self._prims = []

	def raw_points(self):
		return self._points

	def isEmpty(self):
		if self._data.size > 0:
			return False

		return True

	def points(self):
		return [Point(self, i) for i in range(len(self._points))]


	def prims(self):
		return self._prims


	def createPoint(self):
		self._points.append([0,0,0])
		return Point(self, len(self._points)-1)

	def appendPoint(self, x, y, z):
		self._points.append([x, y, z])


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
			frozen_geo._data = copy.deepcopy(self._data)
			frozen_geo._prims = copy.deepcopy(self._prims)
			frozen_geo._frozen = True
			return frozen_geo

	@check_frozen
	def loadFromFile(self, file_name):
		name, extension = os.path.splitext(file_name)
		self.clear()
		GeoIORegistry.getIOTranslatorByExt(extension).readGeometry(file_name, self)


	def saveToFile(self, file_name):
		name, extension = os.path.splitext(file_name)
		GeoIORegistry.getIOTranslatorByExt(extension).saveGeometry(file_name, self)