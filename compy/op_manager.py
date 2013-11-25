from compy.op_node import OP_Node
from compy.parameter import CompyParameter
import re, collections
lastNum = re.compile(r'(?:[^\d]*(\d+)[^\d]*)+')

class OP_Manager(OP_Node):
	"""
	This class implements all the network related methods to be used with Compy nodes. It handles child/parent relations, node creation, manipulation methods
	and tree traversal.

	"""
	def __init__(self, engine, parent, mask=None):
		# mask is a list with node type names that are allowed to be created by this NetworkManager instance e.d ["img","comp"] If mask is None than any node type can be used
		super(OP_Manager, self).__init__()
		self.__engine__ = engine
		self.__mask__ = mask
		self.__name__ = None
		self.__parms__ = collections.OrderedDict()
		self.__node_dict__ = {}
		self.__parent__ = parent
		self.__inputs__ = []
		self.__input_names__ = []

	def __increment__(self, s):
		""" look for the last sequence of number(s) in a string and increment """
		m = lastNum.search(s)
		if m:
			next = str(int(m.group(1))+1)
			start, end = m.span(1)
			s = s[:max(end-len(next), start)] + next + s[end:]
		else:
			return "%s1" % s	

	@property 
	def engine(self):
		return self.__engine__	

	def addParameter(self, name, parm_type, value=None, label=None, callback=None, menu_items=[]):
		parm = CompyParameter(self, name, parm_type, label=label, callback=callback, menu_items=menu_items)
		if value != None: parm.set(value)
		self.__parms__[name] = parm

	def parm(self, parm_path):
		return self.__parms__.get(parm_path)	

	def parms(self):
		return [self.__parms__[name] for name in self.__parms__]	

	def setParms(self, parameters):
		self.cooked = False
		for parm_name in parameters:
			self.__parms__[parm_name].set(parameters[parm_name])

	def type(self):
		return self.type_name

	@property 
	def nodes(self):
		return [self.__node_dict__[node_name] for node_name in self.__node_dict__]

	def parent(self):
		return self.__parent__	

	def children(self):
		if self.__node_dict__.keys() > 0:
			return [self.__node_dict__[name] for name in self.__node_dict__]	
		else:
			return []

	def inputs(self):
		return self.__inputs__

	def input(self, index):
		try:
			node = self.__inputs__[index]
		except:
			raise BaseException("Wrong input index %s specified for node %s !!!") % (index, self)

		return node			

	def inputNames(self):
		""" Returns dict of input names eg: ["Input 1", "Input 2"] """
		return [name for name in self.__input_names__]

	def setInput(self, input_index, node):
		try:
			self.__inputs__[input_index] = node					
		except:
			raise

	def has_inputs(self):
		if len(self.__inputs__) > 0:
			return True
		else:
			return False		

	def flush(self):
		self.__node_dict__ = {}
		

	def createNode(self, node_type_name, node_name=None):
		print "Creating node %s inside %s" % (node_type_name, self.__class__.__name__)

		if self.__mask__ and node_type_name not in self.__mask__:
			print "Creating node of type %s not allowed by this manager." % node_type_name
			return None

		if node_name:
			name = node_name
		else:
			name = node_type_name	

		if node_type_name in self.engine.ops:
			node = self.engine.ops[node_type_name](self.engine, self)	
			node.setName(name)
		else:
			raise BaseException("Unsupported node type \"%s\". Abort." % node_type_name)	

		self.__node_dict__[node.name()] = node
		if self.engine.network_cb:
			self.engine.network_cb()

		print "Created node %s childs is %s" % (node, node.children())	

		return node

	def setName(self, name):
		if name in self.parent().__node_dict__:
			# need to rename this node name by appending number to this node name
			new_name = self.__increment__(name)
			self.__name__ = new_name
		else:	
			self.__name__ = name	

	def name(self):
		return self.__name__	

	def path(self):
		if self.parent():
			if self.parent().parent():
				return "%s/%s" % (self.parent().path(), self.name())
			else:	
				return "/%s" % self.name()
		else:	
			return "/"		

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

	# traverse nodes from this
	def traverse(self, path_list):
		#print "Getting node: %s" % path_list
		node = self.__node_dict__.get(path_list[0])
		if not node: raise BaseException("Unable to get node %s in %s.traverse(self, path_list)" % (path_list[0], self))
		if len(path_list[1::]) > 0:
			# recursive traverse
			return node.traverse(path_list[1::])
		else:
			# return this node
			return node

	# return node object by it's path	
	def node(self, path):
		if path == "/":
			return self.root()

		path_list = filter(lambda a: a != '', path.split("/"))
		if path[0] == "/":
			# traverse from root
			return self.root().traverse(path_list)
		else:	
			# traverse from this
			return self.traverse(path_list)

	# return root node
	def root(self):
		if self.parent():
			return self.parent().root()
		else:
			return self	

	def dumpParms(self):
		dump = {}
		for parm in self.parms():
			dump[parm.name()] = parm.dump()

		return dump			

	def dump(self, recursive=False, dump_parms=False):
		desc = {
			"type":self.type(),
			"path":self.parent().path(),
			"name":self.name()
		}
		if dump_parms == True:
			desc["parms"] = self.dumpParms()

		if recursive == False:
			return desc
		else:
			desc_list = [desc]
			for node in self.children():
				desc_list += node.dump(recursive=True, dump_parms=dump_parms)

			return desc_list

	def __str__(self):
		return self.__class__.__name__				


