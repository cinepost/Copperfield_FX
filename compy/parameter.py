from collections import OrderedDict

CompyLinear = 0
CompyBezier = 2

CompyInt = int 
CompyFloat = float 
CompyString = str 
CompyButton = "button"

class CompyKeyframe(object):
	def __init__(self, engine):
		self.v = value
		self.f = None
		self.t = None
		self.in_type = CompyLinear
		self.out_type = CompyLinear

		if in_type:
			self.in_type = in_type

		if out_type:
			self.out_type = out_type	

	def value(self):
		return self.v		

	def setValue(self, time, value):
		self.v = value

	def dump(self):
		return { "t": self.t, "v": self.value }

	def frame(self):
		return self.f

	def setFrame(self, frame):
		self.f = frame

	def setTime(self, time):
		self.t = time				

		
class CompyParameter(object):
	def __init__(self, node, name, parm_type, label = None):
		self.keyframes = []
		self.value = None
		self.__node__ = node
		self.__name__ = name
		self.__label__ = label
		self.__type__ = parm_type

	def label(self):
		if self.__label__:
			return self.__label__
		else:
			return self.name()		

	def node(self):
		return self.__node__	

	def name(self):
		return self.__name__

	def path(self):
		return "%s/%s" % (self.node().path(), self.name())

	def dump(self):
		if self.animated():
			return [key.dump() for key in self.keyframes]
		else:
			return self.value			

	def type(self):
		return self.__type__

	def animated(self):
		if self.keyframes:
			return True
		else:
			return False

	def eval(self):
		if self.animated():
			# Animated parameter
			return self.evalAtTime(self.__node__.engine.time())
		else:
			# Constant parameter
			return self.value

	def evalAtTime(self, time):
		raise BaseException("Unimplemented evalAtTime(self, time) in %s" % self)

	def evalAtFrame(self, frame):
		raise BaseException("Unimplemented evalAtFrame(self, frame) in %s" % self)	

	def unexpandedString(self):
		raise BaseException("Unimplemented unexpandedString(self) in %s" % self)

	def set(self, value):
		if type(value) in [list, tuple]:
			# set up animated parameter
			pass
		else:
			# set up single parameter value	
			if self.keyframes:
				# Animated parameter
				raise BaseException("Unable to set parm that contains curve animation !!! Use addKeyFrame(time, key) instead !!!")
			else:
				# Constant parameter
				if type(value) == self.__type__:
					self.value = value
				else:
					raise BaseException("Parameter type doesn't match !!! %s expected, but %s provided !" % (self.__type__, type(value)))	

	def setKeyframe(self, keyframe):
		self.keframes.append(keyframe)

	def __str__(self):
		return self.value			