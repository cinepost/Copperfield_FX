from collections import OrderedDict


class CompyKey(object):
	in_type = "linear"
	out_type = "linear"

	def __init__(self, value, in_type=None, out_type=None):
		self.value = value

		if in_type:
			self.in_type = in_type

		if out_type:
			self.out_type = out_type	

	def set(self, value):
		self.value = value

	def get(self):
		return self.value		

		
class CompyParameter(object):
	def __init__(self, node, name, parm_type):
		self.keyframes = {}
		self.value = None
		self.__node__ = node
		self.__name__ = name
		self.__type__ = parm_type
		self.is_animated = False

	def node(self):
		return self.__node__	

	def name(self):
		return self.__name__

	def type(self):
		return self.__type__		

	def eval(self):
		if self.is_animated:
			# Animated parameter
			return self.evalAtTime(self.__node__.engine.time())
		else:
			# Constant parameter
			return self.value

	def evalAtTime(self, time):
		raise BaseException("Unimplemented evalAtTime(self, time) in %s" % self)

	def unexpandedString(self):
		raise BaseException("Unimplemented unexpandedString(self) in %s" % self)

	def set(self, value):
		if self.is_animated:
			# Animated parameter
			raise BaseException("Unable to set parm that contains curve animation !!! Use addKeyFrame(time, key) instead !!!")
		else:
			# Constant parameter
			if type(value) == self.__type__:
				self.value = value
			else:
				raise BaseException("Parameter type doesn't match !!! %s expected, but %s provided !" % (self.__type__, type(value)))	

	def setKeyFrame(self, keyframe):
		raise BaseException("Unimplemented setKeyFrame(self, keyframe) in %s" % self)

	def __str__(self):
		return self.value			