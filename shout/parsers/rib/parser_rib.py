from pyparsing import *
from ..base import ParserBase

rib_grammar = None

class ParserRIB(ParserBase):
	def __init__(self):
		super(ParserRIB, self).__init__()

	@classmethod
	def registerMIMETypes(cls):
		return [
			['renderman/rib', 'rib'],
		]

	@property
	def grammar(self):
		global rib_grammar

		if rib_grammar is None:

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
			setenv = Keyword('setnev')
			ray_version = Keyword('ray_version') + Word(alphas + nums + ".")
			
			ray_detail_name = Word(printables)
			ray_detail_filename = string | Word(printables)
			ray_detail_1 = Keyword("ray_detail") + Group(Optional(Keyword("-T")) + ray_detail_name + ray_detail_filename)
			ray_detail_1.setParseAction(self.do_ray_detail_1)

			ray_detail_sourcename = string | Word(printables)
			ray_detail_2 = Keyword("ray_detail") + Group(Optional(Keyword("-v") + floatnum3) | Optional(Keyword("-V") + floatnum3 + floatnum3) + ray_detail_name + ray_detail_sourcename)

			ray_declare_style = oneOf("object global light geometry plane")
			ray_declare_type = oneOf("float bool int vector2 vector3 vector4 matrix3 matrix4 string")
			ray_declare_array_size = Suppress(Keyword("-v")) + integer
			ray_declare_name = Word(printables)
			ray_declare_value = string | number | Word(alphanums)
			ray_declare = Keyword('ray_declare') + Group(Optional(ray_declare_array_size) + ray_declare_style + ray_declare_type + ray_declare_name + ray_declare_value)
			
			ray_start_object_type = oneOf('material geo light fog object instance plane segment')
			ray_start = Keyword('ray_start') + ray_start_object_type
			
			ray_end = Keyword('ray_end')
			ray_time = Keyword('ray_time') + floatnum

			ray_image_name = string
			ray_image = Group(Keyword('ray_image') + ray_image_name)
			
			ray_procedural_bbox = Group(Suppress(Keyword("-m")) + floatnum3 + Suppress(Keyword("-M")) + floatnum3)
			ray_procedural = Keyword('ray_procedural') + Optional(ray_procedural_bbox)
			
			ray_property_style = oneOf('renderer image camera object light plane')
			ray_property_token = Word(alphanums)
			ray_property_value = Group(OneOrMore(integer | floatnum | Word(alphanums + "_") | string))
			ray_property = Keyword('ray_property') + Group(ray_property_style + ray_property_token + ray_property_value)
			
			ray_transform = Keyword('ray_transform') + Group(OneOrMore(floatnum))
			ray_geometry = Keyword('ray_geometry')
			ray_raytrace = Keyword('ray_raytrace')
			ray_deviceoption = Keyword('ray_deviceoption')
			ray_reset = Keyword('ray_reset') + Group(OneOrMore(oneOf("-l -o -f")))
			ray_quit = Keyword('ray_raytrace').setParseAction(self.finish)

			set_env = Keyword('setenv') + Group(Word(alphanums) + Suppress(Literal('=')) + string)

			otprefer = Keyword('otprefer') + string + string

			rib_grammar = (world_begin | world_end | Word(printables))
			rib_grammar.ignore('#' + restOfLine) # ignore comments

		return rib_grammar
