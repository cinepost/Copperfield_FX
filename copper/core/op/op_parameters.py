from copper.core.parameter import CopperParameter
from copper.core.parameter.parm_template import ParmNamingScheme
import collections

class OP_Parameters(object):
	def __init__(self):
		self.__parms__ = collections.OrderedDict()
		self.__parm_groups__ = collections.OrderedDict() # Used to group parameters by parm templates
		for parm_template in self.parmTemplates():
			self.addParmTuple(parm_template=parm_template, folder_path=[])

	def addParmTuple(self, parm_template=None, folder_path=[], spare=False):
		callback = None
		self.__parm_groups__[parm_template] = []

		if parm_template.length() == 1:
			parm_name = parm_template.name()
			try:
				default_value = parm_template.defaultValue()[0]
			except:
				default_value = parm_template.defaultValue()

			self.__parms__[parm_name] = CopperParameter(self, name=parm_name, parm_template=parm_template, default_value=default_value, spare=spare, callback=callback)
			self.__parm_groups__[parm_template] = [self.__parms__[parm_name]]
			#print "Added parameter %s %s" % (parm_name, parm)
		else:
			for i in range(parm_template.length()):
				if parm_template.namingScheme() == ParmNamingScheme.XYZW:
					parm_name = "%s%s" % (parm_template.name(), ['x','y','z','w'][i])
				elif parm_template.namingScheme() == ParmNamingScheme.RGBA:
					parm_name = "%s%s" % (parm_template.name(), ['r','g','b','a'][i])
				else:
					parm_name = "%s%s" % (parm_template.name(), i+1)


				default_value = parm_template.defaultValue()[i]
				
				self.__parms__[parm_name] = CopperParameter(self, name=parm_name, parm_template=parm_template, default_value=parm_template.defaultValue()[i], spare=spare, callback=callback)
				self.__parm_groups__[parm_template] += [self.__parms__[parm_name]]
				#print "Added parameter %s %s" % (parm_name, parm)

	def addSpareParmFolder(folder_name, in_folder=[]):
		'''
		Adds a folder to the spare parameters. 
		'''
		pass

	def addSpareParmTuple(self, parm_template=None, folder_path = []):
		'''
		Add a spare parameter tuple to the end of the parameters on the node. If in_folder is not an empty sequence, this method adds the parameters 
		to the end of the parameters in a particular folder.
		'''
		self.addParmTuple(parm_template, folder_path, spare=True)

	def parm(self, parm_path):
		if parm_path[0] == "/":
			# get parameter by path
			node_path = parm_path.rsplit("/",1)[0]
			parm_name = parm_path.rsplit("/",1)[-1]
			node = self.node(node_path).parm(parm_name) 
		else:
			# get this node parameter by name 
			return self.__parms__.get(parm_path)

	def parms(self):
		return self.__parms__.values()

	def parmGroups(self):
		return self.__parm_groups__

	def parmTemplates(self):
		return []

	def setParms(self, parameters):
		self.cooked = False
		for parm_name in parameters:
			self.__parms__[parm_name].set(parameters[parm_name])

	def evalParm(self, parm_path):
		return self.parm(parm_path).eval()							
