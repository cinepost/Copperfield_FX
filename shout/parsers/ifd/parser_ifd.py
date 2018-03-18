import logging
from pyparsing import *
from ..base import ParserBase

logger = logging.getLogger(__name__)

ifd_grammar = None

class ParserIFD(ParserBase):
	def __init__(self):
		super(ParserIFD, self).__init__()

	@classmethod
	def registerMIMETypes(cls):
		return [
			['mantra/ifd', 'ifd'],
		]

	@property
	def grammar(self):
		global ifd_grammar

		if ifd_grammar is None:

			# commons
			point = Literal('.')
			e = CaselessLiteral('E')
			pm_sign = Optional(Suppress("+") | Literal("-"))
			number = Word(nums) 
			integer = Combine( Optional(pm_sign) + number + ~FollowedBy(point)).setParseAction(lambda t: int(t[0]))
			floatnum = (integer | Combine( Optional(pm_sign) + Optional(number) + Optional(point) + number + Optional( e + integer ))).setParseAction(lambda t: float(t[0]))
			floatnum3 = Group(floatnum + floatnum + floatnum)
			string = QuotedString('"', escChar=None, multiline=True,unquoteResults=True, endQuoteChar=None)

			# IFD types

			# IFD commands
			ray_version = Keyword('ray_version') + Word(printables).setResultsName("version")
			
			ray_detail_name = Word(printables)
			ray_detail_filename = string | Word(printables)
			ray_detail_1 = Keyword("ray_detail") + Group(Optional(Keyword("-T")) + ray_detail_name + ray_detail_filename)

			ray_detail_sourcename = string | Word(printables)
			ray_detail_2 = Keyword("ray_detail") + Group(Optional(Keyword("-v") + floatnum3) | Optional(Keyword("-V") + floatnum3 + floatnum3) + ray_detail_name + ray_detail_sourcename)

			ray_declare_style = oneOf("object global light geometry plane").setResultsName('style')
			ray_declare_type = oneOf("float bool int vector2 vector3 vector4 matrix3 matrix4 string").setResultsName('type')
			ray_declare_array_size = Suppress(Keyword("-v") + integer.setResultsName('size'))
			ray_declare_name = Word(printables).setResultsName('name')
			ray_declare_value = (number | string | Word(alphanums)).setResultsName('value')
			ray_declare = Keyword('ray_declare') + Optional(ray_declare_array_size) + ray_declare_style + ray_declare_type + ray_declare_name + ray_declare_value
			ray_declare.setParseAction(self.do_ray_declare)

			ray_start_object_type = oneOf('material geo light fog object instance plane segment')
			ray_start = Keyword('ray_start') + ray_start_object_type.setResultsName("type")
			ray_start.setParseAction(self.do_ray_start)
			
			ray_end = Keyword('ray_end')

			ray_time = Keyword('ray_time') + floatnum.setResultsName("time")
			ray_time.setParseAction(self.do_ray_time)

			ray_image_name = string
			ray_image = Keyword('ray_image') + Group(Optional(ray_image_name) + OneOrMore(string | Word(printables)))
			
			ray_procedural_bbox = Group(Suppress(Keyword("-m")) + floatnum3 + Suppress(Keyword("-M")) + floatnum3)
			ray_procedural = Keyword('ray_procedural') + Optional(ray_procedural_bbox)
			
			ray_property_style = oneOf('renderer image camera object light plane').setResultsName('style')
			ray_property_token = Word(printables).setResultsName('token')
			ray_property_value = OneOrMore(integer | floatnum | string | Word(printables)).setResultsName('value')
			ray_property = Keyword('ray_property') + ray_property_style + ray_property_token + ray_property_value
			ray_property.setParseAction(self.do_ray_property)
			
			ray_transform = Keyword('ray_transform') + Group(OneOrMore(floatnum))
			ray_geometry = Keyword('ray_geometry')
			ray_raytrace = Keyword('ray_raytrace')
			ray_deviceoption = Keyword('ray_deviceoption')
			ray_reset = Keyword('ray_reset') + Group(OneOrMore(oneOf("-l -o -f")))
			ray_raytrace = Keyword('ray_raytrace')
			ray_quit = Keyword('ray_quit').setParseAction(self.finish)

			set_env = Keyword('setenv') + Word(printables).setResultsName('key') + Suppress(Literal('=')) + string.setResultsName('value')
			set_env.setParseAction(self.do_set_env)

			otprefer = Keyword('otprefer') + string + string

			ifd_grammar = Optional(set_env | ray_time | ray_start | ray_declare | ray_property)
			ifd_grammar.ignore('#' + restOfLine) # ignore comments

		return ifd_grammar

	def do_set_env(self, tokens):
		print("do_set_env %s" % tokens.asDict())

	def do_ray_start(self, tokens):
		print("do_ray_start %s" % tokens.asDict())

	def do_ray_time(self, tokens):
		print("do_ray_time %s" % tokens.asDict())

	def do_ray_declare(self, tokens):
		print("do_ray_declare %s" % tokens.asDict())

	def do_ray_property(self, tokens):
		print("do_ray_property %s" % tokens.asDict())
