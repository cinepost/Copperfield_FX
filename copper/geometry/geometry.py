from .point import Point


class Geometry(object):
	def __init__(self, sop_node=None):
		self._sop_node = sop_node
		self._points = []
		self._prims = []

	def points(self):
		return self._points

	def prims(self):
		return self._prims

	def createPoint(self):
		self._points.append(Point())
		return self._points[-1]

	def sopNode(self):
		return self._sop_node