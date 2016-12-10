import numpy
import math


class Matrix4:
    def __init__(self, d=0):
        self.m = numpy.identity(4, dtype=numpy.float64) * d
    
    def __repr__(self):
        return self.m

    def __str__(self):
    	return str(self.m)
        
    def get(self):
        return self.m
    
    def returnCopy(self):
        M = Matrix4()
        M.m = numpy.array(self.m, copy=True) # copy the matrix array
        return M

    def setToZero(self):
    	self.m = numpy.zeros((4,4), dtype=numpy.float64)
    
    def setToIdentity(self):
        self.m = numpy.identity(4, dtype=numpy.float64)

    @staticmethod
    def translation( vector3 ):
        M = Matrix4(1) # identity matrix
        M.m[3,:3] = vector3.comps
        return M

    @staticmethod
    def rotationMatrix( angleInRadians, axisVector, point=None):
		sina = math.sin(angleInRadians)
		cosa = math.cos(angleInRadians)
		direction = axisVector.normalized().comps
		# rotation matrix around unit vector
		R = numpy.diag([cosa, cosa, cosa])		
		R += numpy.outer(direction, direction) * (1.0 - cosa)
		direction *= sina
		R += numpy.array([[ 0.0, -direction[2], direction[1]],
			 [ direction[2], 0.0, -direction[0]],
			 [-direction[1], direction[0],  0.0]])
		M = Matrix4(1) # identity matrix
		M.m[:3, :3] = R
		if point is not None:
			# rotation not around origin
			point = numpy.array(point[:3], dtype=numpy.float64, copy=False)
			M.m[:3, 3] = point - numpy.dot(R, point)

		return M

    @staticmethod
    def rotation( angleInRadians, axisVector, originPoint ):
        v = originPoint.asVector3()
        return Matrix4.translation(v) * Matrix4.rotationMatrix(angleInRadians,axisVector) * Matrix4.translation(- v)

    @staticmethod
    def uniformScaleAroundOrigin(scaleFactor):
        M = Matrix4(1) # identity matrix
        M.m[:3,:3] *= scaleFactor
        return M

    @staticmethod
    def uniformScale( scaleFactor, originPoint ):
        v = originPoint.asVector3()
        return Matrix4.translation(v) * Matrix4.uniformScaleAroundOrigin(scaleFactor) * Matrix4.translation(- v)

    @staticmethod
    def lookAt( eyePoint, targetPoint, upVector, isInverted ):
        # step one: generate a rotation matrix

        z = (eyePoint-targetPoint).normalized()
        y = upVector
        x = (y ^ z).normalized()   # cross product
        y = (z ^ x).normalized()   # cross product

        M = Matrix4(1) # identity matrix

        # the rotation matrix
        M.m[:3,:3] = [x.comps, y.comps ,z.comps]

        # step two: postmultiply by a translation matrix
        if isInverted :
            return M * Matrix4.translation( eyePoint )
        else:
            M.m = numpy.transpose(M.m)
            return Matrix4.translation( - eyePoint ) * M

    def __mul__(a,b):   # note: a is really self
        if isinstance(b,Matrix4):
            M = Matrix4()
            M.m = numpy.dot(a.m,b.m)
            return M
        elif isinstance(b,Vector3):
            # We treat the vector as if its (homogeneous) 4th component were zero.
            return Vector3(a.m[:3,:3].dot(b.comps))
        else:
        	raise BaseException("%s __mul__ %s not supported !!!" % (a.__class__, b.__class__))

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


class Point(Vector3):

	def setPosition(self, pos):
		self.comps = pos

	def position(self):
		return self.comps


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