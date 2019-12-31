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
	def readGeometry(file_name):
		""" Loads Houdini GEO/BGEO file. """
		with open(filename) as data_file:    
			data = json.load(data_file)

	@staticmethod
	def saveGeometry(file_name):
		""" Saves Houdini GEO/BGEO file. """
		raise NotImplementedError

