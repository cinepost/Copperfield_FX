import logging
from pyparsing import *
from ..base import ParserBase

logger = logging.getLogger(__name__)

bgeo_grammar = None

class ParserBGEO(ParserBase):
	def __init__(self):
		super(ParserBGEO, self).__init__()

	@classmethod
	def registerMIMETypes(cls):
		return [
			['houdini/bgeo', 'bgeo'],
		]

	@property
	def grammar(self):
		global bgeo_grammar

		if bgeo_grammar is None:

			# commons
			point = Literal('.')
			e = CaselessLiteral('E')
			pm_sign = Optional(Suppress("+") | Literal("-"))
			number = Word(nums) 
			integer = Combine( Optional(pm_sign) + number + ~FollowedBy(point)).setParseAction(lambda t: int(t[0]))
			floatnum = (integer | Combine( Optional(pm_sign) + Optional(number) + Optional(point) + number + Optional( e + integer ))).setParseAction(lambda t: float(t[0]))
			floatnum3 = Group(floatnum + floatnum + floatnum)
			string = QuotedString('"', escChar=None, multiline=True,unquoteResults=True, endQuoteChar=None)

			bgeo_binary_magic_number = Keyword('NSJb').setParseAction(self.setBinaryMode)

			bgeo_grammar = Optional(bgeo_binary_magic_number)
			bgeo_grammar.ignore('#' + restOfLine) # ignore comments

		return bgeo_grammar

	def setBinaryMode(self, toks):
		print("B I N A R Y !!!!")
