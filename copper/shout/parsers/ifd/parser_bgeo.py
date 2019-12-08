import logging
import numpy as np
from ..base import ParserBase

logger = logging.getLogger(__name__)

from copper.lib import bson

from . import hgeo
from copper.lib import ubjson

print("_ubjson %s" % ubjson.EXTENSION_ENABLED)

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

			geo = None

			try:
				parser = bson.Parser()
				#handle = MHandle()
				handle = bson.JSONHandle()
				parser.parse(input_stream, handle)

				#geo = ubjson.load(input_stream)
				#geo = handle.list_stack.pop()[0]
			except:
				raise

			if parser.Errors:
				logger.error("BGEO paser errors: \n%s" % parser.Errors)
				return False

			if geo:
				#jsn = handle.list_stack.pop()[0]
				logger.debug("bgeo json parsed ok!")

				#logger.debug("check with hgeo")
				d = hgeo.Detail()
				d.loadJSON(geo)
				print('%12d Points' % d.pointCount())
				print('%12d Vertices' % d.vertexCount())
				print('%12d Primitives' % d.primitiveCount())

			else:
				logger.error("error parsing bgeo!")

				logger.debug("done")

			return True

