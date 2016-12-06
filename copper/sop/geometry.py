import numpy as np


class Point:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0

	def __init__(self, x):
		self.x = x
		self.y = x
		self.z = x

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z


class Geometry(object):
	def __init__(self, sop_node=None):
		self._sop_node = sop_node
		self._points = []
		self._prims = []

	def points(self):
		return self._points

	def prims(self):
		return self._prims

	def sopNode(self):
		return self._sop_node