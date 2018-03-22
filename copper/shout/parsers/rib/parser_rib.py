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
			world_begin = Keyword('WorldBegin')
			world_begin.setParseAction(self.do_world_begin)

			world_end = Keyword('WorldEnd')
			world_end.setParseAction(self.do_world_end)

			rib_grammar = Optional(world_begin | world_end)
			rib_grammar.ignore('#' + restOfLine) # ignore comments

		return rib_grammar

	def do_world_begin(self, tokens):
		logger.debug(tokens)

	def do_world_end(self, tokens):
		logger.debug(tokens)


