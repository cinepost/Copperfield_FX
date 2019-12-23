import numpy
import sys

from ..base import GeoBaseIO
from copper.geometry import Polygon

class ObjIO(GeoBaseIO):

	@classmethod
	def registerMIMETypes(cls):
		return [
			['application/wobj', '.obj'],
		]

	@staticmethod 
	def readGeometry(filename, geometry, swapyz=False):
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
				#vertices.append(list(map(numpy.float32, values[1:4])))
				numpy.append(geometry._data['P'], values[1:4])
			elif values[0] == 'vn':
				# read vertex normal data
				if swapyz:
					values[1:4] = values[1], values[3], values[2]
				normals.append(map(numpy.float32, values[1:4]))
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
				face = []
				texcoords = []
				norms = []
				for v in values[1:]:
					w = v.split('/')
					face.append(int(w[0])-1) # .obj face uses vertex indices 1-n...
					if len(w) >= 2 and len(w[1]) > 0:
						texcoords.append(int(w[1]))
					else:
						texcoords.append(0)
					if len(w) >= 3 and len(w[2]) > 0:
						norms.append(int(w[2]))
					else:
						norms.append(0)
				faces.append((face, norms, texcoords, material))
				pass

		for face in faces:
			#print(face)
			poly = Polygon(geometry)
			poly._vertices = list(face[0])
			poly.setIsClosed()
			geometry._prims.append(poly)
			
	@staticmethod
	def saveGeometry(filename, geometry, swapyz=False):
		raise NotImplementedError

