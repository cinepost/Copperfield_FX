import logging

from PyQt5 import QtCore

from collections import OrderedDict
from .copper_string import CopperString

from copper.parm_template import ParmTemplate, ParmLookScheme, ParmNamingScheme, ParmTemplateType, StringParmType

logger = logging.getLogger(__name__)

CopperLinear = 0
CopperBezier = 2

#CopperParmInt = int
#CopperParmInt2 = CopperInt2
#CopperParmInt3 = CopperInt3
#CopperParmInt4 = CopperInt4
#CopperParmBool = bool
#CopperParmFloat = float 
#CopperParmFloat2 = CopperFloat2
#CopperParmFloat3 = CopperFloat3
#CopperParmFloat4 = CopperFloat4
#CopperParmString = CopperString
#CopperParmOpPath = "oppath"
#CopperParmFile = str
#CopperParmButton = "button"
#CopperParmOrderedMenu = "menu"

class CopperKeyframe(object):
	def __init__(self, engine, time=None, value=None):
		self.v = value
		self.f = None
		self.t = time
		self.in_type = CopperLinear
		self.out_type = CopperLinear

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
		return "<CopperKeyframe: t:%s v:%s>"	% (self.t, self.v)				


class ParmSignals(QtCore.QObject):
	parameterChanged = QtCore.pyqtSignal()
	setParameter = QtCore.pyqtSignal(object) # fired by GUI ParameterWidget... maybe not only by GUI... hmmm

	def __init__(self):  
		QtCore.QObject.__init__(self)

		
class CopperParameter(QtCore.QObject):
	def __init__(self, node, name, parm_template, default_value=None, callback = None, spare=True):
		QtCore.QObject.__init__(self)
		self.__keyframes__ = []
		self.value = default_value
		self._node = node
		self._name = name
		self._parm_template = parm_template
		self._spare = spare

		self.signals = ParmSignals()

		# connect signals
		self.signals.setParameter.connect(self._setParameter)

	def isSpare(self):
		return self._spare

	def parmTemplate(self) -> ParmTemplate:
		'''
		Returns the template for this parameter.
		'''
		return self._parm_template

	def node(self):
		return self._node	

	def name(self):
		return self._name

	def path(self):
		return "%s/%s" % (self.node().path(), self.name())

	def dump(self):
		if self.animated():
			return [key.dump() for key in self.__keyframes__]
		else:
			return self.value			

	def menuItems(self):
		if self.parmTemplate().type() is ParmTemplateType.Menu:
			return self.parmTemplate().menuItems()
		else:
			raise BaseException("Cannot get menu items for a non-menu parm")

	def menuLabels(self):
		if self.parmTemplate().type() is ParmTemplateType.Menu:
			return self.parmTemplate().menuLabels()
		else:
			raise BaseException("Cannot get menu values for a non-menu parm")

	def pressButton(self):
		if self.parmTemplate().type() is ParmTemplateType.Button:
			self.parmTemplate().callback()

	def invalidateNode(self):
		self.node.invalidate()
		# call this method to force recook node. e.g. parameter changed

	#def set(self, value):
	#	self.value = value
	#	self.invalidateNode()
	#	logger.debug("Parameter value set to: %s of type %s" % (self.value, type(self.value)))

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

	def evalAsBool(self):
		return bool(self.eval())

	def evalAsString(self):
		if self.parmTemplate().type() == ParmTemplateType.Menu:
			return self.menuItems()[self.eval()]

		return CopperString(self.eval()).expandedString()

	def evalAtTime(self, time):
		lesser_keys = sorted([k for k in self.__keyframes__ if k.t <= time], key=lambda x: x.t)
		greater_keys = sorted([k for k in self.__keyframes__ if k.t >= time], key=lambda x: x.t)

		#self.log("lesser_keys: %s" % ["t:%s, v:%s ; "%(key.t, key.value()) for key in lesser_keys])
		#self.log("greater_keys: %s" % ["t:%s, v:%s ; "%(key.t, key.value()) for key in greater_keys])

		if lesser_keys: 
			left_k = lesser_keys[-1]
		else: 
			left_k = None
		
		if greater_keys: 
			right_k = greater_keys[0] 
		else: 
			right_k = None

		if not left_k:
			# no interpolation
			self.log("No interpolation. Using closest right key at time %s with value %s" % (right_k.t, right_k.value()))
			#self.log(["t:%s,v:%s ; " % (key.t, key.value()) for key in self.__keyframes__])
			return right_k.value()	

		if not right_k:
			# no interpolation
			self.log("No interpolation. Using closest left key at time %s with value %s" % (left_k.t, left_k.value()))
			#self.log(["t:%s,v:%s ; " % (key.t, key.value()) for key in self.__keyframes__])
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
		raise NotImplementedError

	def evalAsStringAtFrame(self, frame):
		return self.evalAsString()

	def unexpandedString(self):
		return str(self.eval())

	@QtCore.pyqtSlot(object)
	def _setParameter(self, value):
		self.set(value)

	def set(self, value):
		if type(value) in [list, tuple]:
			# set up animated parameter
			for key in value:
				keyframe = CopperKeyframe(self.node().engine, time=key["t"], value=key["v"])
				self.setKeyframe(keyframe)
		else:
			# set up single parameter value	
			if self.__keyframes__:
				# Animated parameter
				raise BaseException("Unable to set parm that contains curve animation !!! Use addKeyFrame(time, key) instead !!!")
			else:
				# Constant parameter
				self.value = value

		self.signals.parameterChanged.emit() # emit signal to GUI
		self.node().setModified(True) # This is important ! We need to say node that it needs to recook itself when needed, because some parameter was changed
				
	def setKeyframe(self, keyframe):
		self.__keyframes__.append(keyframe)
	

	#def __str__(self):
	#	return self.value			