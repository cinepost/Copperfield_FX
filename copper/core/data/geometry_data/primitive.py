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

class ObjWithAttribs(object):

	def __init__(self, attribs_dict, index):
		self._attribs_dict = attribs_dict
		self._index = index

	def setAttribValue(self, name_or_attrib: str or Attrib, attrib_value):		
		attribs = self._attribs_dict[name_or_attrib]		
		attribs.data[self._index] = attrib_value

	def attribValue(self, name_or_attrib: str or Attrib):
		return self._attribs_dict[name_or_attrib][self._index]	

class Point(ObjWithAttribs):

	def __init__(self, geometry, pt_index):
		super(Point, self).__init__(geometry._point_attribs, pt_index)
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

	def index(self):
		return self._pt_index



class Vertex(ObjWithAttribs):

	def __init__(self, prim, pt_index, vt_index):
		super(Vertex, self).__init__(prim._geometry._vertex_attribs, vt_index)
		self._pt_index = pt_index
		self._prim = prim
		self._vt_index = vt_index

	def number(self):
		return self._vt_index

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


class Prim(ObjWithAttribs):
	def __init__(self, geometry, prim_index):
		super(Prim, self).__init__(geometry._prim_attribs, prim_index)
		self._geometry = geometry
		self._prim_index = prim_index
		self._vertices = [] # list of Vertex objects
	
	def numVertices(self):
		return len(self._vertices)

	def vertex(self, index):
		return self._vertices[index]

	def verticesRaw(self):
		return self._vertices

	def vertices(self) -> tuple:
		return tuple(self._vertices)

	def attribValue(self, name_or_attrib) -> int or float or str or tuple:
		pass

	def type(self):
		return self.__class__.prim_type

class Face(Prim):
	def __init__(self, geometry, prim_index):
		super(Face, self).__init__(geometry, prim_index)
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

	def addVertex(self, point) -> Vertex:
		'''
		Create a new vertex inside this face, adding it to the end of the vertex list.
		'''
		vt = self._geometry.createVertex(self, point)
		self._vertices.append(vt)
		return vt

	def normal(self):
		'''
		Return the vector that’s perpendicular to the face.
		'''
		return Vector3()

class Polygon(Face):
	
	prim_type = primType.Polygon
	
	def __init__(self, geometry, prim_index, is_closed=True):
		super(Polygon, self).__init__(geometry, prim_index)
		self._closed = is_closed



