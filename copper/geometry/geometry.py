from copper.vmath import Vector3


class Geometry(object):
	def __init__(self, sop_node=None):
		self._sop_node = sop_node
		self._points = []
		self._prims = []


	def raw_points(self):
		return self._points

	def points(self):
		return [Vector3(pt) for pt in self._points]

	def prims(self):
		return self._prims

	def createPoint(self):
		self._points.append([0,0,0])
		return Vector3(self._points[-1])

	def sopNode(self):
		return self._sop_node