from pyparsing import *

#http://pyparsing.wikispaces.com/HowToUsePyparsing
#https://habrahabr.ru/post/241670/
#https://pyparsing.wikispaces.com/file/view/SimpleCalc.py

exprStack = []
varStack  = []
variables = {}

def pushFirst( str, loc, toks ):
    exprStack.append( toks[0] )

def assignVar( str, loc, toks ):
    varStack.append( toks[0] )

class ParserBase(object):

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
		self._echo = False
		self._eof_or_quit = False # Set to True when parser finds special exit/quit/finish toket/command or EOF. In case of IFD it's 'ray_quit' command

	def setEchoInput(self, echo=True):
		self._echo = echo

	def parseFile(self, filename):
		# set up a generator to yield a line of text at a time
		linegenerator = open(filename)
		# line_buffer will accumulate lines until a fully parseable piece is found
		line_buffer = ""

		for line in linegenerator:
			line_buffer += line

			match = next(self.grammar.scanString(line_buffer), None)
			while match:
				tokens, start, end = match
				print tokens.asList()

				line_buffer = line_buffer[end:]
				match = next(self.grammar.scanString(line_buffer), None) 

	def isDone(self):
		"""Return True when parsing is done."""
		return self._eof_or_quit

	def finish(self):
		"""Call this from nested parser when exit/quit/finish token found."""
		self._eof_or_quit = True

	@property
	def grammar(self):
		raise NotImplementedError("Subclasses parser should implement this!")
