from collections import OrderedDict

CompyLinear = 0
CompyBezier = 2

CompyParmInt = int
CompyParmBool = bool
CompyParmFloat = float 
CompyParmString = str
CompyParmOpPath = "oppath"
CompyParmFile = str
CompyParmButton = "button"
CompyParmOrderedMenu = "menu"

class CompyKeyframe(object):
	def __init__(self, engine, time=None, value=None):
		self.v = value
		self.f = None
		self.t = time
		self.in_type = CompyLinear
		self.out_type = CompyLinear

	def value(self):
		return self.v		

	def setValue(self, time, value):
		self.v = value

	def dump(self):
		return { "t": self.t, "v": self.v }

	def frame(self):
		return self.f

	def setFrame(self, frame):
		self.f = frame

	def setTime(self, time):
		self.t = time

	def __repr__(self):
		return "<CompyKeyframe: t:%s v:%s>"	% (self.t, self.v)				

		
class CompyParameter(object):
	def __init__(self, node, name, parm_type, label = None, callback = None, menu_items = []):
		self.__keyframes__ = []
		self.value = None
		self.__cb__ = callback
		self.__node__ = node
		self.__name__ = name
		self.__label__ = label
		self.__type__ = parm_type
		self.__menu_items__ = OrderedDict(menu_items)

	def log(self, text):
		print "%s parm at frame %s: %s" % (self.path(), self.node().engine.frame(), text)	

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
			return [key.dump() for key in self.__keyframes__]
		else:
			return self.value			

	def type(self):
		return self.__type__

	def animated(self):
		if self.__keyframes__:
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

	def evalAsInt(self):
		return int(self.eval())

	def evalAsFloat(self):
		return float(self.eval())	

	def evalAtTime(self, time):
		lesser_keys = sorted(k for k in self.__keyframes__ if k.t <= time)
		greter_keys = sorted(k for k in self.__keyframes__ if k.t >= time)

		if lesser_keys: 
			left_k = lesser_keys[-1]
		else: 
			left_k = None
		
		if greter_keys: 
			right_k = greter_keys[0] 
		else: 
			right_k = None

		if not left_k:
			# no interpolation
			self.log("No interpolation. Using closest right key at time %s" % right_k.t)
			return right_k.value()	

		if not right_k:
			# no interpolation
			self.log("No interpolation. Using closest left key at time %s" % left_k.t)
			return left_k.value()

		if right_k.t == left_k.t:
			return left_k.value()

		min_w = (time - left_k.t) / (right_k.t - left_k.t)
		max_w = (right_k.t - time) / (right_k.t - left_k.t)

		interp = min_w * right_k.value() + max_w * left_k.value()
		self.log("Interpolated value is %s" % interp)
		return interp
		#raise BaseException("Unimplemented evalAtTime(self, time) in %s" % self)

	def evalAtFrame(self, frame):
		raise BaseException("Unimplemented evalAtFrame(self, frame) in %s" % self)	

	def unexpandedString(self):
		raise BaseException("Unimplemented unexpandedString(self) in %s" % self)

	def set(self, value):
		if type(value) in [list, tuple]:
			# set up animated parameter
			for key in value:
				keyframe = CompyKeyframe(self.node().engine, time=key["t"], value=key["v"])
				self.setKeyframe(keyframe)
		else:
			# set up single parameter value	
			if self.__keyframes__:
				# Animated parameter
				raise BaseException("Unable to set parm that contains curve animation !!! Use addKeyFrame(time, key) instead !!!")
			else:
				# Constant parameter
				self.value = value
				
	def setKeyframe(self, keyframe):
		self.__keyframes__.append(keyframe)

	def setCallback(self, callback):
		self.__cb__ = callback

	def getCallback(self):
		return self.__cb__	

	def callback(self):
		self.__cb__()	

	#def __str__(self):
	#	return self.value			