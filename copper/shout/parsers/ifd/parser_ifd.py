import logging

try:
	import cPyparsing as pp
except:
	import pyparsing as pp

from ..base import ParserBase
from .parser_bgeo import ParserBGEO

logger = logging.getLogger(__name__)

ifd_grammar = None

class ParserIFD(ParserBase):
	def __init__(self):
		self._bgeo_parser = None
		super(ParserIFD, self).__init__()

	@classmethod
	def registerMIMETypes(cls):
		return [
			['mantra/ifd', 'ifd'],
		]

	@property
	def bgeo_parser(self):
		if not self._bgeo_parser:
			self._bgeo_parser = ParserBGEO()

		return self._bgeo_parser

	def parseStream(self, input_stream):
			self.input_stream = input_stream
			command_buff = ""

			while True:
				word = self.readWord(input_stream)
				if not word:
					break
				
				if word.startswith("ray_") or word in ('setenv',):
					# we've encounted command so let's parse what we have so far
					self.parseIFDCommand(command_buff)
					command_buff = ""

				elif word == 'stdin':
					# parse stdin geometry
					command_buff += " stdin"
					self.parseIFDCommand(command_buff)
					command_buff = ""

				command_buff += word + " "

			#self.parseIFDCommand(command_buff)

				#print(word)

	def parseIFDCommand(self, command_str):
		try:
			self.grammar.parseString(command_str)
		except:
			raise #logger.error("Unable to parse string: %s" % command_str)


	@property
	def grammar(self):
		global ifd_grammar

		if ifd_grammar is None:

			# commons
			point = pp.Literal('.')
			e = pp.CaselessLiteral('E')
			pm_sign = pp.Optional(pp.Suppress("+") | pp.Literal("-"))
			number = pp.Word(pp.nums) 
			integer = pp.Combine( pp.Optional(pm_sign) + number + ~pp.FollowedBy(point)).setParseAction(lambda t: int(t[0]))
			floatnum = (integer | pp.Combine( pp.Optional(pm_sign) + pp.Optional(number) + pp.Optional(point) + number + pp.Optional( e + integer ))).setParseAction(lambda t: float(t[0]))
			floatnum3 = pp.Group(floatnum + floatnum + floatnum)
			string = pp.QuotedString('"', escChar=None, multiline=True, unquoteResults=True, endQuoteChar=None)

			# IFD types

			# IFD commands
			ray_version = pp.Keyword('ray_version') + pp.Word(pp.printables).setResultsName("version")
			ray_version.setParseAction(self.do_ray_version)
			
			ray_detail_name = pp.Word(pp.printables).setResultsName('name')
			ray_detail_filename = (string | pp.Word(pp.printables)).setResultsName('filename')
			ray_detail_temporary = pp.Optional(pp.Keyword("-T").setResultsName('temporary'))
			ray_detail_stdin = pp.Keyword('stdin').setResultsName('stdin').setParseAction(self.do_read_stdin_geo)
			ray_detail_1 = pp.Keyword("ray_detail") + ray_detail_temporary + ray_detail_name + (ray_detail_stdin | ray_detail_filename)
			ray_detail_1.setParseAction(self.do_ray_detail_1)

			ray_detail_sourcename = string | pp.Word(pp.printables)
			ray_detail_blur = pp.Suppress(pp.Keyword("-v")) + floatnum3.setResultsName('postblur') | pp.Suppress(pp.Keyword("-V")) + floatnum3.setResultsName('preblur') + floatnum3.setResultsName('postblur')
			ray_detail_2 = pp.Keyword("ray_detail") + pp.Optional(ray_detail_blur) + ray_detail_name + ray_detail_sourcename.setResultsName('sourcename')
			ray_detail_2.setParseAction(self.do_ray_detail_2)

			ray_declare_style = pp.oneOf("object global light geometry plane").setResultsName('style')
			ray_declare_type = pp.oneOf("float bool int vector2 vector3 vector4 matrix3 matrix4 string").setResultsName('type')
			ray_declare_array_size = pp.Suppress(pp.Keyword("-v") + integer.setResultsName('size'))
			ray_declare_name = pp.Word(pp.printables).setResultsName('name')
			ray_declare_value = (number | string | pp.Word(pp.alphanums)).setResultsName('value')
			ray_declare = pp.Keyword('ray_declare') + pp.Optional(ray_declare_array_size) + ray_declare_style + ray_declare_type + ray_declare_name + ray_declare_value
			ray_declare.setParseAction(self.do_ray_declare)

			# Begins definition of an object
			ray_start_object_type = pp.oneOf('material geo light fog object instance plane segment')
			ray_start = pp.Keyword('ray_start') + ray_start_object_type.setResultsName("object_type")
			ray_start.setParseAction(self.do_ray_start)
			
			# End declaration of an object
			ray_end = pp.Keyword('ray_end')
			ray_end.setParseAction(self.do_ray_end)

			ray_time = pp.Keyword('ray_time') + floatnum.setResultsName("time")
			ray_time.setParseAction(self.do_ray_time)

			ray_image_name = string
			ray_image = pp.Keyword('ray_image') + pp.Group(pp.Optional(ray_image_name) + pp.OneOrMore(string | pp.Word(pp.printables)))
			ray_image.setParseAction(self.do_ray_image)
			
			ray_procedural_bbox = pp.Group(pp.Suppress(pp.Keyword("-m")) + floatnum3 + pp.Suppress(pp.Keyword("-M")) + floatnum3)
			ray_procedural = pp.Keyword('ray_procedural') + pp.Optional(ray_procedural_bbox)
			
			ray_property_style = pp.oneOf('renderer image camera object light plane').setResultsName('style')
			ray_property_token = pp.Word(pp.printables).setResultsName('token')
			ray_property_value = pp.OneOrMore(integer | floatnum | string | pp.Word(pp.printables)).setResultsName('value')
			ray_property = pp.Keyword('ray_property') + ray_property_style + ray_property_token + ray_property_value
			ray_property.setParseAction(self.do_ray_property)
			
			ray_transform = pp.Keyword('ray_transform') + pp.Group(pp.OneOrMore(floatnum)).setResultsName("matrix")
			ray_transform.setParseAction(self.do_ray_transform)

			ray_geometry = pp.Keyword('ray_geometry')
			ray_raytrace = pp.Keyword('ray_raytrace')
			ray_deviceoption = pp.Keyword('ray_deviceoption')
			ray_reset = pp.Keyword('ray_reset') + pp.Group(pp.OneOrMore(pp.oneOf("-l -o -f")))
			ray_raytrace = pp.Keyword('ray_raytrace')
			ray_quit = pp.Keyword('ray_quit').setParseAction(self.finish)

			set_env = pp.Keyword('setenv') + pp.Word(pp.printables).setResultsName('key') + pp.Suppress(pp.Literal('=')) + string.setResultsName('value')
			set_env.setParseAction(self.do_set_env)

			otprefer = pp.Keyword('otprefer') + string + string

			ifd_grammar = pp.Optional(set_env | ray_time | ray_start | ray_end | ray_declare | ray_property | ray_detail_1 | ray_detail_1 | ray_version
				| ray_transform | ray_image)
			ifd_grammar.ignore('#' + pp.restOfLine) # ignore comments

		return ifd_grammar

	def do_set_env(self, tokens):
		import os
		logger.debug(tokens)
		os.environ[tokens['key']] = tokens['value']

	def do_ray_version(sefl, tokens):
		logger.debug(tokens)

	def do_ray_start(self, tokens):
		logger.debug(tokens)

	def do_ray_end(self, tokens):
		logger.debug(tokens)

	def do_ray_transform(self, tokens):
		logger.debug(tokens)

	def do_ray_time(self, tokens):
		logger.debug(tokens)

	def do_ray_image(self, tokens):
		logger.debug(tokens)

	def do_ray_declare(self, tokens):
		logger.debug(tokens)

	def do_ray_property(self, tokens):
		logger.debug(tokens)

	def do_ray_detail_1(self, tokens):
		print("ray_detail_1")
		logger.debug(tokens)

	def do_ray_detail_2(self, tokens):
		print("ray_detail_2")
		logger.debug(tokens)

	def do_read_stdin_geo(self, tokens):
		logger.debug(tokens)
		parser = ParserBGEO()
		parser.parseStream(self.input_stream)
		#self.bgeo_parser.parseBuffer(self.fp) #, echo=(args.V > 0), renderer=renderer)
		#while True:
		#	line = self.fp.readline()
		#	if not line:
		#		break
		#	print(line)

