from pyparsing import Word, alphas, nums

#http://pyparsing.wikispaces.com/HowToUsePyparsing

class ParserBase():

	exit_token = None
	integer = Word( nums )

	def __init__(self):
		self._echo = False
		self._eof_or_quit = False # Set to True when parser finds special exit/quit/finish toket/command or EOF. In case of IFD it's 'ray_quit' command

	def setEchoInput(self, echo=True):
		self._echo = echo

	def parseLine(self, line):
		if self._echo: sys.stdout.write(line)

	def isDone(self):
		return self._eof_or_quit

	def setDone(self):
		self._eof_or_quit = True


class ParserIFD(ParserBase):

	exit_token = 'ray_quit'
	command = 

	def __init__(self):

		super(ParserIFD, self).__init__()