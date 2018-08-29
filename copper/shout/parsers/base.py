import sys
import six
import logging
import fileinput
import mimetypes
from pyparsing import *

ParserElement.setDefaultWhitespaceChars(' \t\n')

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

	def __init__(self):
		self._renderer = None
		self._echo = False
		self._eof_or_quit = False # Set to True when parser finds special exit/quit/finish toket/command or EOF. In case of IFD it's 'ray_quit' command

	def setRenderer(self, renderer):
		self._renderer = renderer

	def setEchoInput(self, echo=True):
		self._echo = echo

	def parseBuffer(self, buff):
		line = buff.readline()
		while line:
			result = self.grammar.parseString(line)
			line = buff.readline()

	def parseFile(self, scene_filename, echo=False):
		from functools import partial

		# line_buff will accumulate lines until a fully parseable piece is found
		line_buff = ""

		if scene_filename:
			# read from file
			file_input = open(scene_filename, "r")
		else:
			# read from stdin
			file_input = sys.stdin

		# read text file 
		with file_input as openfileobject:
			for line in openfileobject:
				if line.lstrip().startswith(self.keywords):
					result = self.grammar.parseString(line_buff)
					line_buff = line
				else:
					line_buff += line

		# snippet to read binary read binary
		#with open('somefile', 'rb') as openfileobject:
		#	for chunk in iter(partial(openfileobject.read, 1024), ''):
		#		pass


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
