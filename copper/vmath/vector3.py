import math
import numpy

class Vector3(numpy.ndarray):
	def __new__(cls, *args):
		nargs = len(args)
		if nargs == 0:
			# epmty vetor with undefined values
			buff = numpy.zeros(3, dtype=numpy.float64)
		elif nargs == 1:	
			if isinstance(args[0], Vector3):
				# return copy of input Vector3
				return args[0].copy()
			elif isinstance(args[0], list):
				buff = numpy.array(args[0][:3], dtype=numpy.float64)
			elif isinstance(args[0], numpy.ndarray):
				buff = args[0]
			else:
				raise TypeError('Vector3.__new__ unsupported argument type %s' % type(args[0]))
		elif nargs == 3:
			buff = numpy.array(data, dtype=numpy.float64, copy=True)

		return numpy.ndarray.__new__(cls, shape=(3,), buffer=buff)

	def __repr__(self):
		return "%s %s" % (self.__class__, repr(tuple(self)))

	def distanceTo(self, other):
		return numpy.linalg.norm(numpy.subtract(self, other))

	def __neg__(self):
		return Vector3(numpy.negative(self))

	def __add__(self,other):
		return Vector3(numpy.add(self, other))
	
	def __sub__(self,other):
		return Vector3(numpy.subtract(self, other))

	def __xor__(self, other):   # cross product
		return Vector3(numpy.cross(self, other))

	def __mul__(self,other):
		return Vector3(numpy.dot(self, other))

	def __eq__(self,other):
		return numpy.array_equal(self, other)

	def __ne__(self,other):
		return not (self==other)

	def lengthSquared(self):
		return sum(numpy.square(self))

	def length(self):
		return numpy.linalg.norm(self)

	def normalized(self):
		norm = numpy.linalg.norm(self)
		if norm==0:
			norm=numpy.finfo(v.dtype).eps
		return Vector3(self/norm)