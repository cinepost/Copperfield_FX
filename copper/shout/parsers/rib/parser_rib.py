import logging
from pyparsing import *
from ..base import ParserBase

logger = logging.getLogger(__name__)

rib_grammar = None

class ParserRIB(ParserBase):
	def __init__(self):
		super(ParserRIB, self).__init__()

	@classmethod
	def registerMIMETypes(cls):
		return (
			('renderman/rib', 'rib'),
		)

	@property
	def keywords(self):
		return (
			'Format', 'Display', 'Sphere', 'Translate', 'Transform', 'Rotate', 'ConcatTransform', 'Opacity', 'Color', 'WorldBegin', 'WorldEnd',
			'AttributeBegin', 'AttributeEnd', 'Attribute'
		)

	@property
	def grammar(self):
		global rib_grammar

		if rib_grammar is None:
			# commons
			point = Literal('.')
			e = CaselessLiteral('e') + Optional(oneOf('+ -')) + Word(nums)
			pm_sign = Optional(Suppress("+") | Literal("-"))

			integer = Combine(Optional(pm_sign) + Word(nums) + ~FollowedBy(point)).setParseAction(lambda toks: int(toks[0]))
			floatnum = (integer | Combine(Optional(pm_sign) + Optional(Word(nums)) + Optional(point) + Word(nums) + Optional(e))).setParseAction(lambda toks: float(toks[0]))
			number = (floatnum | integer) # either integer or float
			floatnum3 = Optional(Suppress("[")) + Group(floatnum + floatnum + floatnum) + Optional(Suppress("]"))
			floatnum4 = Optional(Suppress("[")) + Group(floatnum + floatnum + floatnum + floatnum) + Optional(Suppress("]"))
			matrix3x3 = Optional(Suppress("[")) + Group(floatnum3 + floatnum3 + floatnum3) + Optional(Suppress("]"))
			matrix4x4 = Optional(Suppress("[")) + Group(floatnum4 + floatnum4 + floatnum4 + floatnum4) + Optional(Suppress("]"))
			string = QuotedString('"', escChar=None, multiline=True,unquoteResults=True, endQuoteChar=None)

			# RIB types

			# RIB commands
			rib_attribute_begin = Keyword('AttributeBegin')
			rib_attribute_begin.setParseAction(self._do_attribute_begin)
			
			rib_attribute_end = Keyword('AttributeEnd')
			rib_attribute_end.setParseAction(self._do_attribute_end)

			rib_format = Keyword('Format') + integer + floatnum + floatnum
			rib_format.setParseAction(self._do_format)

			rib_display = Keyword('Display') + string + string + string
			rib_display.setParseAction(self._do_display)

			rib_sphere = Keyword('Sphere') + floatnum3 + floatnum
			rib_sphere.setParseAction(self._do_sphere)

			rib_translate = Keyword('Translate') + floatnum3
			rib_translate.setParseAction(self._do_translate)

			rib_rotate = Keyword('Rotate') + (floatnum4 | floatnum3)
			rib_rotate.setParseAction(self._do_rotate)

			rib_transform = Keyword('Transform') + matrix4x4
			rib_transform.setParseAction(self._do_transform)

			rib_concat_transform = Keyword('ConcatTransform') + matrix4x4
			rib_concat_transform.setParseAction(self._do_concat_transform)

			rib_opacity = Keyword('Opacity') + floatnum3
			rib_opacity.setParseAction(self._do_opacity)

			rib_color = Keyword('Color') + (floatnum4 | floatnum3)
			rib_color.setParseAction(self._do_color)

			rib_world_begin = Keyword('WorldBegin')
			rib_world_begin.setParseAction(self._do_world_begin)

			rib_world_end = Keyword('WorldEnd')
			rib_world_end.setParseAction(self._do_world_end)

			rib_grammar = Optional(rib_format | rib_world_begin | rib_world_end | rib_translate | rib_transform | rib_concat_transform | rib_rotate | rib_color | rib_opacity |
				rib_sphere | rib_display | rib_attribute_begin | rib_attribute_end)
			rib_grammar.ignore('#' + restOfLine) # ignore comments
			rib_grammar.setDefaultWhitespaceChars(' \t\n')

		return rib_grammar

	def _do_attribute_begin(self, toks):
		logger.debug(toks)

	def _do_attribute_end(self, toks):
		logger.debug(toks)

	def _do_format(self, toks):
		logger.debug(toks)

	def _do_display(self, toks):
		logger.debug(toks)

	def _do_sphere(self, toks):
		logger.debug(toks)

	def _do_world_begin(self, toks):
		logger.debug(toks)

	def _do_world_end(self, toks):
		logger.debug(toks)

	def _do_transform(self, toks):
		logger.debug(toks)

	def _do_concat_transform(self, toks):
		logger.debug(toks)

	def _do_translate(self, toks):
		logger.debug(toks)

	def _do_rotate(self, toks):
		logger.debug(toks)

	def _do_color(self, toks):
		logger.debug(toks)

	def _do_opacity(self, toks):
		logger.debug(toks)
