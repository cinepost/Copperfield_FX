from copper.vmath import Vector3

class primType():
	class Polygon():
		@staticmethod
		def name():
			return "Polygon"

	class Mesh():
		@staticmethod
		def name():
			return "Mesh"

	class Sphere():
		@staticmethod
		def name():
			return "Sphere"		


class Point(object):

	def __init__(self, geometry, pt_index):
		self._geometry = geometry
		self._pt_index = pt_index

	def position(self):
		return self._geometry._data['P'][self._pt_index]

	def setPosition(self, pos):
		self._geometry._data['P'][self._pt_index] = pos[:3]

	def setPosition(self, x, y, z):
		self._geometry._data['P'][self._pt_index] = [x, y, z]

	def index(self):
		return self._pt_index


class Vertex(object):

	def __init__(self, pt_index, prim, number):
		self._pt_index = pt_index
		self._prim = prim
		self._number = number


	def number(self):
		return self._number


	def prim(self):
		return self._prim


	def geometry(self):
		return self._prim._geometry


	def pointIndex(self):
		return self._pt_index


	def point(self):
		raise Point(self._prim._geometry, self._pt_index)


	def raw_point(self):
		return self._prim._geometry._points[self._pt_index]


class Polygon(object):
	
	prim_type = primType.Polygon
	
	def __init__(self, geometry=None):
		self._geometry = geometry
		self._vertices = [] # this is actually just a list of point numbers, so index is vertex number and value is point number in geometry._points
		self._closed = False


	def numVertices(self):
		return len(self._vertices)


	def isClosed(self):
		return self._closed


	def setIsClosed(self, on_off=True):
		self._closed = on_off


	def close(self):
		self._closed = True


	def raw_vertices(self):
		return self._vertices


	def vertices(self):
		return [Vertex(self._vertices[i], self, i) for i in range(len(self._vertices))]


	def vertex(self, index):
		return Vertex(self._vertices[index])


	def normal(self):
		return Vector3()


