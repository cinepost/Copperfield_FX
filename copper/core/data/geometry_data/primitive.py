from enum import Enum
from copper.core.vmath import Vector3

class primType(Enum):
	Unknown = 0
	Custom = 1
	Agent = 2
	AlembicRef = 3
	BezierCurve = 4
	BezierSurface = 5
	Circle = 6
	Mesh = 7
	Metaball = 8
	NURBSCurve = 9
	NURBSSurface = 10
	PackedFragment = 11
	PackedGeometry =12
	PackedPrim = 13
	ParticleSystem = 14
	PastedSurface = 15
	Polygon = 16
	PolySoup = 17
	Sphere = 18
	Tetrahedron = 19
	TriangleBezier = 20
	TriangleFan = 21
	TriangleStrip = 22
	Tube = 23
	VDB = 24
	Volume = 25

from .attribs import attribType, Attrib

class Point(object):

	def __init__(self, geometry=None, pt_index=None):
		self._geometry = geometry
		self._pt_index = pt_index

	def position(self):
		return self._geometry._point_attribs['P'][self._pt_index]

	def setPosition(self, pos):
		self._geometry._point_attribs['P'].data[self._pt_index] = pos[:3]

	def weight(self):
		return self._geometry._point_attribs['Pw'][self._pt_index]

	def setWeight(self, weight):
		self._geometry._point_attribs['Pw'][self._pt_index] = weight

	def attribValue(self, name_or_attrib: str or Attrib):
		if isinstance(name_or_attrib, Attrib):
			return self._geometry._point_attribs[name_or_attrib.name()][self._pt_index]

		return self._geometry._point_attribs[name_or_attrib][self._pt_index]

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

	def attribValue(self, name_or_attrib: str or Attrib):
		if isinstance(name_or_attrib, Attrib):
			return self._geometry._vertex_attribs[name_or_attrib.name()][self._pt_index]

		return self._geometry._vertex_attribs[name_or_attrib][self._pt_index]

class Prim():
	def __init__(self, geometry):
		self._geometry = geometry
		self._vertices = [] # this is actually just a list of point numbers, so index is vertex number and value is point number in geometry._points
	
	def numVertices(self):
		return len(self._vertices)

	def vertex(self, index):
		return Vertex(self._vertices[index])

	def verticesRaw(self):
		return self._vertices

	def vertices(self) -> tuple:
		return tuple([Vertex(self._vertices[i], self, i) for i in range(len(self._vertices))])

	def attribValue(self, name_or_attrib) -> int or float or str or tuple:
		pass

	def type(self):
		return self.__class__.prim_type

class Face(Prim):
	def __init__(self, geometry):
		super(Face, self).__init__(geometry)
		self._closed = False

	def isClosed(self) -> bool:
		'''
		Return whether the first and last vertex are connected.
		'''
		return self._closed

	def setIsClosed(self, on_off=True):
		'''
		Set whether the face is open or closed.
		'''
		self._closed = on_off

	def normal(self):
		'''
		Return the vector that’s perpendicular to the face.
		'''
		return Vector3()

class Polygon(Face):
	
	prim_type = primType.Polygon
	
	def __init__(self, geometry):
		super(Polygon, self).__init__(geometry)



