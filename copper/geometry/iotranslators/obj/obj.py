import numpy
import sys

from ..base import GeoBaseIO

class ObjIO(GeoBaseIO):

	@classmethod
	def registerMIMETypes(cls):
		return [
			['application/wobj', 'obj'],
		]

	@staticmethod 
	def readGeometry(geometry, filename, swapyz=False):
		""" Loads a Wavefront OBJ file. """
		vertices = []
		normals = []
		texcoords = []
		faces = []
 
		material = None
		for line in open(filename, "r"):
			if line.startswith('#'): continue
			values = line.split()
			if not values: continue
			if values[0] == 'v':
				# read vertex data
				geometry._points.append(map(float, values[1:4]))
			elif values[0] == 'vn':
				# read vertex normal data
				if swapyz:
					v = v[0], v[2], v[1]
				geometry._normals.append(map(float, v[1:4]))
			elif values[0] == 'vt':
				# read vertex texture coordinates
				texcoords.append(map(numpy.float64, values[1:3]))
			elif values[0] in ('usemtl', 'usemat'):
				# read material information
				#material = values[1]
				pass
			elif values[0] == 'mtllib':
				# read material definition
				#self.mtl = MTL(values[1])
				pass
			elif values[0] == 'f':
				# read face/primitive information
				#face = []
				#texcoords = []
				#norms = []
				#for v in values[1:]:
				#	w = v.split('/')
				#	face.append(int(w[0]))
				#	if len(w) >= 2 and len(w[1]) > 0:
				#		texcoords.append(int(w[1]))
				#	else:
				#		texcoords.append(0)
				#	if len(w) >= 3 and len(w[2]) > 0:
				#		norms.append(int(w[2]))
				#	else:
				#		norms.append(0)
				#faces.append((face, norms, texcoords, material))
 				pass

	@staticmethod
	def saveGeometry(geometry, filename, swapyz=False):
		raise NotImplementedError

