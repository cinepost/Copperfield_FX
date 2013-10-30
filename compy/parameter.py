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


class CompyCurve(object):
	keys = []
	
	def insertKey(time, key):
		self.keys += (time, key,)


	def removeKey(time):
		pass	

		
class CompyParameter(object):
	is_animated 	= False
	curve			= {}

	def __init__(self, value=None):
		self.value = value

	def get(self, time=None):
		if not self.is_animated:
			# Constant parameter
			return self.value
		else:
			# Animated parameter
			pass

	def set(self, value):
		if not self.is_animated:
			# Constant parameter
			self.value = value
		else:
			# Animated parameter
			raise BaseException("Unable to set parm that contains curve animation !!! Use addKeyFrame(time, key) instead !!!")

	def addKeyFrame(self, time, key):
		self.is_animated = True
		curve[time] = key

	def __str__(self):
		return str(self.value)