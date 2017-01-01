import math
import numpy

from .vector3 import Vector3

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
        M.m[3,:3] = vector3
        return M

    @staticmethod
    def eulerToMatrixDegrees(rx=0, ry=0, rz=0):
        ''' Return matrix for rotations around z, y and x axes '''
        return Matrix4.eulerToMatrixRadians(numpy.radians(rx), numpy.radians(ry), numpy.radians(rz))

    @staticmethod
    def eulerToMatrixRadians(rx=0, ry=0, rz=0):
        ''' Return matrix for rotations around z, y and x axes '''

        cosx = math.cos(rx)
        sinx = math.sin(rx)
        m1 = numpy.array(
                [[1, 0, 0, 0],
                 [0, cosx, -sinx, 0],
                 [0, sinx, cosx, 0],
                 [0, 0, 0, 1]])

        cosy = math.cos(ry)
        siny = math.sin(ry)
        m2 = numpy.array(
                [[cosy, 0, siny, 0],
                 [0, 1, 0, 0],
                 [-siny, 0, cosy, 0],
                 [0, 0, 0, 1]])

        cosz = math.cos(rz)
        sinz = math.sin(rz)
        m3 = numpy.array(
                [[cosz, -sinz, 0, 0],
                 [sinz, cosz, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])
        
        M = Matrix4()
        M.m = numpy.dot(numpy.dot(m1,m2),m3)
        return M

    @staticmethod
    def rotationMatrix( angleInRadians, axisVector, point=None):
		sina = math.sin(angleInRadians)
		cosa = math.cos(angleInRadians)
		direction = axisVector.normalized()
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
        M.m[:3,:3] = [x, y ,z]

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
            return Vector3(a.m[:3,:3].dot(b))
        else:
			raise BaseException("%s __mul__ %s not supported !!!" % (a.__class__, b.__class__))