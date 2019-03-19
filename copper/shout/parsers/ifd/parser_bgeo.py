import logging
import numpy as np
from ..base import ParserBase

logger = logging.getLogger(__name__)

try:
	from . import bson
	logger.debug("Using fast bson cython module !!!")
except:
	logger.warning("Using slow binary_json pure python module !!!")
	from . import binary_json as bson

from . import hgeo

bgeo_grammar = None


class ParserBGEO(ParserBase):
	def __init__(self):
		super(ParserBGEO, self).__init__()

	@classmethod
	def registerMIMETypes(cls):
		return [
			['houdini/bgeo', 'bgeo'],
		]

	def parseStream(self, input_stream):
			self.input_stream = input_stream

			logger.debug("Parsing stdin json geometry with binary_json.py")

			try:
				parser = bson.Parser()
				#handle = MHandle()
				handle = bson.MHandle()
				geo = parser.parse(input_stream, handle)
			except:
				raise

			if parser.Errors:
				logger.error("BGEO paser errors: \n%s" % parser.Errors)
				return False

			if geo:
				#jsn = handle.list_stack.pop()[0]
				logger.debug("bgeo json parsed ok!")

				#logger.debug("check with hgeo")
				#d = hgeo.Detail()
				#d.loadJSON(jsn)
				#print('%12d Points' % d.pointCount())
				#print('%12d Vertices' % d.vertexCount())
				#print('%12d Primitives' % d.primitiveCount())

			else:
				logger.error("error parsing bgeo!")

				logger.debug("done")

			return True

