import math
import numpy


class Vector3(list):
	def __init__(self, *args):
		nargs = len(args)
		if nargs == 0:
			list.__init__(self, [0,0,0])
		elif nargs == 1:
			if isinstance(args[0], Vector3):
				list.__init__(self, args[0])
			elif isinstance(args[0], list) or isinstance(args[0], numpy.ndarray):
				list.__init__(self, args[0][:3])
			else:
				raise TypeError('Vector3.__init__ unsupported argument type %s' % type(args[0]))
		elif nargs == 3:
			list.__init__(self, [args[0], args[1], args[2]])
		else:
			raise TypeError('Vector3.__init__ wrong number of arguments')

	def __repr__(self):
		return "%s %s" % (self.__class__, repr(tuple(self)))

	def distanceTo(self, other):
		d = self - other
		return math.sqrt(d[0]*d[0] + d[1]*d[1] + d[2]*d[2])

	def __neg__(self):
		return Vector3([-self[0], -self[1], -self[2]])

	def __add__(self,other):
		return Vector3([self[0]+other[0], self[1]+other[1], self[2]+other[2]])
	
	def __iadd__(self, other):
		return Vector3([self[0]+other[0], self[1]+other[1], self[2]+other[2]])

	def __sub__(self,other):
		return Vector3([self[0]-other[0], self[1]-other[1], self[2]-other[2]])

	def __xor__(self, other):   # cross product
		return Vector3([self[1]*other[2]-self[2]*other[1], self[2]*other[0]-self[0]*other[2], self[0]*other[1]-self[1]*other[0]])

	def __mul__(self, a):
		return Vector3([self[0]*a, self[1]*a, self[2]*a])

	def __eq__(self, other):
		return all([abs(self[0] - other[0]) < 1e-10, abs(self[1] - other[1]) < 1e-10, abs(self[2] - other[2]) < 1e-10])

	def __ne__(self, other):
		return not (self==other)

	def __truediv__(self, d):
		return Vector3([self[0] / d, self[1] / d, self[2] / d])

	def lengthSquared(self):
		return self[0]*self[0] + self[1]*self[1] + self[2]*self[2]

	def length(self):
		return math.sqrt(self[0]*self[0] + self[1]*self[1] + self[2]*self[2])

	def normalized(self):
		return Vector3(self/self.length())

	def setPosition(self, pos):
		self[0] = pos[0]; self[1] = pos[1]; self[2] = pos[2]

	def position(self):
		return self
