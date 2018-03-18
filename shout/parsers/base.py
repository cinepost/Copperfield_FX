import sys
import six
import logging
import fileinput
import mimetypes
from pyparsing import *

#http://pyparsing.wikispaces.com/HowToUsePyparsing
#https://habrahabr.ru/post/241670/
#https://pyparsing.wikispaces.com/file/view/SimpleCalc.py

logger = logging.getLogger(__name__)

class RegistryMeta(type):
    def __getitem__(meta, key):
        return meta._registry[key]


@six.add_metaclass(RegistryMeta)
class ParsersRegistry(type):
	_registry = {}
	_registry_by_ext = {}
	_registry_by_mime = {}
	_registry_extensions = []

	def __new__(meta, name, bases, clsdict):
		cls = super(ParsersRegistry, meta).__new__(meta, name, bases, clsdict)
		if not clsdict.pop('__base__', False):
			meta._registry[name] = cls
			for mime_type in cls.registerMIMETypes():
				mimetypes.add_type(mime_type[0], mime_type[1], strict=True)
				meta._registry_by_mime[mime_type[0]] = cls # this is used to find a proper translator by mime type
				meta._registry_by_ext[mime_type[1]] = cls # this is used to find a proper translator by filename extension
				meta._registry_extensions += [mime_type[1]]

		return cls

	@classmethod
	def getParserByMIME(cls, mime_type):
		return cls._registry_by_mime[mime_type]

	@classmethod
	def getParserByExt(cls, ext):
		return cls._registry_by_ext[ext]()

	@classmethod
	def supportedTypes(cls):
		return cls._registry_extensions


exprStack = []
varStack  = []
variables = {}

def pushFirst( str, loc, toks ):
    exprStack.append( toks[0] )

def assignVar( str, loc, toks ):
    varStack.append( toks[0] )

@six.add_metaclass(ParsersRegistry)
class ParserBase(object):

	__base__ = True

	# define grammar
	point = Literal('.')
	e = CaselessLiteral('E')
	plusorminus = Literal('+') | Literal('-')
	number = Word(nums) 
	integer = Combine( Optional(plusorminus) + number )
	floatnumber = Combine( integer + Optional( point + Optional(number) ) + Optional( e + integer ))
	ident = Word(alphas,alphanums + '_') 
	plus = Literal( "+" )
	minus = Literal( "-" )
	mult = Literal( "*" )
	div = Literal( "/" )
	lpar = Literal( "(" ).suppress()
	rpar = Literal( ")" ).suppress()
	addop = plus | minus
	multop = mult | div
	expop = Literal( "^" )
	assign = Literal( "=" )

	expr = Forward()
	atom = ( ( e | floatnumber | integer | ident ).setParseAction(pushFirst) | ( lpar + expr.suppress() + rpar ))
	    
	factor = Forward()
	factor << atom + ZeroOrMore( ( expop + factor ).setParseAction( pushFirst ) )
	    
	term = factor + ZeroOrMore( ( multop + factor ).setParseAction( pushFirst ) )
	expr << term + ZeroOrMore( ( addop + term ).setParseAction( pushFirst ) )
	bnf = Optional((ident + assign).setParseAction(assignVar)) + expr

	pattern =  bnf + StringEnd()

	# map operator symbols to corresponding arithmetic operations
	opn = {
		"+" : ( lambda a,b: a + b ),
        "-" : ( lambda a,b: a - b ),
        "*" : ( lambda a,b: a * b ),
        "/" : ( lambda a,b: a / b ),
        "^" : ( lambda a,b: a ** b )
    }

	def __init__(self):
		self._renderer = None
		self._echo = False
		self._eof_or_quit = False # Set to True when parser finds special exit/quit/finish toket/command or EOF. In case of IFD it's 'ray_quit' command

	def setEchoInput(self, echo=True):
		self._echo = echo

	def parseFile(self, scene_filename, echo=False, renderer=None):
		self._renderer=renderer
		# line_buffer will accumulate lines until a fully parseable piece is found
		line_buffer = ""

		if scene_filename:
			# read from file
			file_input = open(scene_filename, "r")
		else:
			# read from stdin
			file_input = sys.stdin

		with file_input as f:
			for line in f:
				line_buffer += line
				#print("> %s" % line)
				result = self.grammar.parseString(line)
				#if result:
				#	print(": %s" % result.asDict())
				#match = next(self.grammar.parseString(line_buffer), None)
				#while match:
				#	tokens, start, end = match
				#	print(tokens.asDict())

				#	line_buffer = line_buffer[end:]
				#	match = next(self.grammar.scanString(line_buffer), None)

	def isDone(self):
		"""Return True when parsing is done."""
		return self._eof_or_quit

	def finish(self):
		"""Call this from nested parser when exit/quit/finish token found."""
		self._eof_or_quit = True

	@property
	def grammar(self):
		raise NotImplementedError("Subclasses parser should implement this!")

	@classmethod
	def registerMIMETypes(cls):
		raise NotImplementedError
