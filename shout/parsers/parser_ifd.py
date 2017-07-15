from pyparsing import *
from parser_base import ParserBase

ifd_grammar = None

class ParserIFD(ParserBase):
	def __init__(self):
		super(ParserIFD, self).__init__()

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

			# IFD types

			# IFD commands
			setenv = Keyword('setnev')
			ray_version = Keyword('ray_version') + Word(alphas + nums + ".")
			
			ray_detail_1 = Optional(Keyword("-T")) + Word(alphanums + "/") + Word(alphanums + "/")
			ray_detail_2 = Optional(Keyword("-v") + floatnum3) | Optional(Keyword("-V") + floatnum3 + floatnum3) + Word(alphanums + "/") + Word(alphanums + "/")


			ray_declare_style = oneOf("object global light geometry plane")
			ray_declare_type = oneOf("float bool int vector2 vector3 vector4 matrix3 matrix4 string")
			ray_declare_array_size = Suppress(Keyword("-v")) + integer
			ray_declare = Keyword('ray_declare') + Group(Optional(ray_declare_array_size) + ray_declare_style + ray_declare_type)
			
			ray_start_object_type = oneOf('material geo light fog object instance plane segment')
			ray_start = Keyword('ray_start') + ray_start_object_type
			
			ray_end = Keyword('ray_start')
			ray_time = Keyword('ray_time') + floatnum
			ray_image = Keyword('ray_image')
			
			ray_procedural_bbox = Group(Suppress(Keyword("-m")) + floatnum3 + Suppress(Keyword("-M")) + floatnum3)
			ray_procedural = Keyword('ray_procedural') + Optional(ray_procedural_bbox)
			
			ray_property = Keyword('ray_property') + Group(oneOf('renderer image camera object light plane') + Word(alphanums) + Group(OneOrMore(integer | floatnum | Word(alphanums) | quotedString)))
			
			ray_transform = Keyword('ray_transform') + Group(OneOrMore(floatnum))
			ray_geometry = Keyword('ray_geometry')
			ray_raytrace = Keyword('ray_raytrace')
			ray_deviceoption = Keyword('ray_deviceoption')
			ray_reset = Keyword('ray_reset') + Group(OneOrMore(oneOf("-l -o -f")))
			ray_quit = Keyword('ray_raytrace').setParseAction(self.finish)


			ifd_grammar = (ray_time | ray_version | ray_end | ray_quit | ray_transform | ray_reset | ray_property | ray_procedural | ray_declare | Word(printables))# + StringEnd()
			ifd_grammar.ignore('#' + restOfLine) # ignore comments

			#ifd_grammar = Suppress('#' + restOfLine)

		return ifd_grammar