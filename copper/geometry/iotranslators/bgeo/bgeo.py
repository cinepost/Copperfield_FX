import sys

from ..base import GeoBaseIO

class BgeoIO(GeoBaseIO):

	@classmethod
	def registerMIMETypes(cls):
		return [
			['application/houdini', '.geo'],
			['application/houdini', '.bgeo']
		]

	@staticmethod 
	def readGeometry(filename, geometry):
		""" Loads Houdini GEO/BGEO file. """
		with open(filename) as data_file:    
			data = json.load(data_file)

	@staticmethod
	def saveGeometry(filename, geometry):
		""" Saves Houdini GEO/BGEO file. """
		raise NotImplementedError

