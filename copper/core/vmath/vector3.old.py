import math
import numpy

class Vector3:
	def __init__(self, comps=None):
		if comps == None:
			self.comps = numpy.empty(3, dtype=numpy.float64)
		else:
			self.comps = numpy.asarray(comps[:3], dtype=numpy.float64)

	def __repr__(self):
		return "%s %s" % (self.__class__, self.comps)

	def x(self):
		return self.comps[0]

	def y(self):
		return self.comps[1]

	def z(self):
		return self.comps[2]

	def __getitem__(self, key):
		return self.comps[key]

	def __setitem__(self, key, value):
		self.comps[key] = value

	def distanceTo(self, other):
		return numpy.linalg.norm(numpy.subtract(self.comps, other.comps))

	def __neg__(self):
		return Vector3(numpy.negative(self.comps))

	def __add__(self,other):
		return Vector3(numpy.add(self.comps, other.comps))
	
	def __sub__(self,other):
		return Vector3(numpy.subtract(self.comps, other.comps))

	def __xor__(self, other):   # cross product
		return Vector3(numpy.cross(self.comps, other.comps))

	def __mul__(self,other):
		if isinstance(other,Vector3):
		# dot product
			return Vector3(numpy.dot(self.comps, other.comps))
		
		# scalar product
		return Vector3(numpy.dot(self.comps, other))

	def __eq__(self,other):
		return numpy.array_equal(sefl.comps, other.comps)

	def __ne__(self,other):
		return not (self==other)

	def returnCopy(self):
		return Vector3(self.comps)

	def lengthSquared(self):
		return sum(numpy.square(self.comps))

	def length(self):
		return numpy.linalg.norm(self.comps)

	def normalized(self):
		norm = numpy.linalg.norm(self.comps)
		if norm==0:
			norm=numpy.finfo(v.dtype).eps
		return Vector3(self.comps/norm)