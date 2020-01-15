import numpy
import sys

from ..base import GeoBaseIO
from copper.core.data.geometry_data.primitive import Polygon
from copper.core.data.geometry_data.attribs import attribType

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
		normals = [None] # .obj normal indices starts from 1 so we put None in zero index
		texcoords = [None] # .obj tex coords indices starts from 1 so we put None in zero index
		faces = []
		hou_points = [None] # .obj vertex indices starts from 1 so we put None in zero index

		material = None
		for line in open(filename, "r"):
			if line.startswith('#'): continue
			values = line.split()
			if not values: continue
			if values[0] == 'v':
				# read vertex data
				#pt = geometry.createPoint()
				#pt.setPosition(values[1:4])
				#hou_points.append(pt)
				pass
			elif values[0] == 'vn':
				# read vertex normal data
				if swapyz:
					values[1:4] = values[1], values[3], values[2]
				normals.append(values[1:4])
			elif values[0] == 'vt':
				# read vertex texture coordinates
				values.extend([0.0]) # in case we have only u and v components
				texcoords.append(values[1:4])
			elif values[0] in ('usemtl', 'usemat'):
				# read material information
				material = values[1]
			elif values[0] == 'mtllib':
				# read material definition
				#self.mtl = MTL(values[1])
				pass
			elif values[0] == 'f':
				# read face/primitive information
				pt_indices = []
				uvw_indices = []
				norm_indices = []
				for v in values[1:]:
					w = v.split('/')
					pt_indices.append(int(w[0]))
					if len(w) >= 2 and len(w[1]) > 0:
						uvw_indices.append(int(w[1]))
					else:
						uvw_indices.append(0)
					if len(w) >= 3 and len(w[2]) > 0:
						norm_indices.append(int(w[2]))
					else:
						norm_indices.append(0)
				faces.append((pt_indices, norm_indices, uvw_indices, material))
				pass

		use_normals = False
		if len(normals) > 1: # remember zero index element 
			#geometry.addAttrib(attribType.Vertex, 'N', (0.0, 0.0, 0.0))
			use_normals = True

		use_uvw = False
		if len(texcoords) > 1: # zero index element always present
			#geometry.addAttrib(attribType.Vertex, 'uv', (0.0, 0.0, 0.0))			
			use_uvw = True

		#for face in faces:
		#	poly = geometry.createPolygon()
		#	for i in range(len(face[0])):
		#		vt = poly.addVertex(hou_points[face[0][i]])
				
			#if use_normals:
			#	vt.setAttribValue('N', normals[face[1][i]])
			
			#if use_uvw:
			#	vt.setAttribValue('uv', texcoords[face[2][i]])

	@staticmethod
	def saveGeometry(filename, geometry, swapyz=False):
		raise NotImplementedError

