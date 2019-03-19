import logging
from ..base import ParserBase

from . import binary_json as bson
from . import hgeo

logger = logging.getLogger(__name__)

bgeo_grammar = None

class Stack:
	def __init__(self):
		self.container = []  # You don't want to assign [] to self - when you do that, you're just assigning to a new local variable called `self`.  You want your stack to *have* a list, not *be* a list.

	def isEmpty(self):
		return self.size() == 0   # While there's nothing wrong with self.container == [], there is a builtin function for that purpose, so we may as well use it.  And while we're at it, it's often nice to use your own internal functions, so behavior is more consistent.

	def push(self, item):
		self.container.append(item)  # appending to the *container*, not the instance itself.

	def pop(self):
		return self.container.pop()  # pop from the container, this was fixed from the old version which was wrong

	def peek(self):
		if self.isEmpty():
			raise Exception("Stack empty!")
		return self.container[len(self.container)-1]  # View element at top of the stack

	def size(self):
		return len(self.container)  # length of the container

	def show(self):
		return self.container  # display the entire stack as list

from enum import Enum
import collections

class MHandle(bson.Handle):
	#cur_array = None

	class Mode(Enum):
		NONE = 0
		LIST = 1
		DICT = 2

	def __init__(self):
		self.list_stack = Stack()
		self.list_stack.push([]) # by default our json is a list itself

		self.dict_stack = Stack()

		self.mode = Stack()
		self.mode.push(self.Mode.LIST)

	def _pushValue(self, value):
		if self.mode.peek() == self.Mode.LIST:
			self.list_stack.peek().append(value)
		elif self.mode.peek() == self.Mode.DICT:
			self.dict_stack.peek()[list(self.dict_stack.peek().keys())[-1]] = value

	def jsonInt(self, parser, value):
		#print("jsonInt %s" % value)
		self._pushValue(value)
		return True

	def jsonBool(self, parser, value):
		#print("jsonBool %s" % value)
		self._pushValue(value)
		return True

	def jsonReal(self, parser, value):
		#print("jsonReal %s" % value)
		self._pushValue(value)
		return True
	
	def jsonString(self, parser, value):
		#print("jsonString %s" % value)
		self._pushValue(value)
		return True

	def jsonNull(self, parser):
		#print("jsonNull")
		self._pushValue(None)
		return True

	def jsonBeginArray(self, parser):
		#print("jsonBeginArray")
		self.mode.push(self.Mode.LIST)
		self.list_stack.push([])
		return True
	
	def jsonEndArray(self, parser):
		#print("jsonEndArray %s " % self.list_stack.peek())
		self.mode.pop()
		self._pushValue(self.list_stack.pop())
		return True

	def jsonBeginMap(self, parser):
		#print("jsonBeginMap")
		self.mode.push(self.Mode.DICT)
		self.dict_stack.push(collections.OrderedDict())
		return True
	
	def jsonEndMap(self, parser):
		#print("jsonEndMap %s" % self.dict_stack.peek())
		self.mode.pop()
		self._pushValue(self.dict_stack.pop())
		return True

	def jsonKey(self, parser, value):
		#print("jsonKey %s" % value)
		if type(value) == bytes:
			self.dict_stack.peek()[value.decode("UTF-8")] = None
		else:
			self.dict_stack.peek()[value] = None
		return True


class ParserBGEO(ParserBase):
	def __init__(self):
		super(ParserBGEO, self).__init__()

	@classmethod
	def registerMIMETypes(cls):
		return [
			['houdini/bgeo', 'bgeo'],
		]

	def parseStream(self, input_stream):
			self.input_stream = input_stream

			logger.debug("Parsing stdin geometry with binary_json.py")

			try:
				parser = bson.Parser()
				handle = MHandle()
				geo = parser.parse(input_stream, handle)
			except:
				raise

			if parser.Errors:
				logger.error("BGEO paser errors: \n%s" % parser.Errors)
				return False

			if geo:
				logger.debug("bgeo parsed ok!")
				jsn = handle.list_stack.pop()[0]
				print(jsn)

				logger.debug("check with hgeo")
				d = hgeo.Detail()
				d.loadJSON(jsn)
				print('%12d Points' % d.pointCount())
				print('%12d Vertices' % d.vertexCount())
				print('%12d Primitives' % d.primitiveCount())

			else:
				logger.error("error parsing bgeo!")

				logger.debug("done")

			return True

