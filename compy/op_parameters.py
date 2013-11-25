from compy.parameter import CompyParameter
import collections

class OP_Parameters(object):

	def __init__(self):
		self.__parms__ = collections.OrderedDict()

	def addParameter(self, name, parm_type, value=None, label=None, callback=None, menu_items=[]):
		parm = CompyParameter(self, name, parm_type, label=label, callback=callback, menu_items=menu_items)
		if value != None: parm.set(value)
		self.__parms__[name] = parm

	def parms(self):
		return [self.__parms__[name] for name in self.__parms__]	

	def setParms(self, parameters):
		self.cooked = False
		for parm_name in parameters:
			self.__parms__[parm_name].set(parameters[parm_name])
	
	def parm(self, parm_path):
		if parm_path[0] == "/":
			# get parameter by path
			node_path = parm_path.rsplit("/",1)[0]
			parm_name = parm_path.rsplit("/",1)[-1]
			node = self.node(node_path).parm(parm_name) 
		else:
			# get this node parameter by name 
			return self.__parms__.get(parm_path)

	def evalParm(self, parm_path):
		return self.parm(parm_path).eval()							
