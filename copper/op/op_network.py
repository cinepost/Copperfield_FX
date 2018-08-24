import re, collections
import logging 

#from gui.signals import signals
from copper.op.base import OpRegistry
from copper.op.op_node import OP_Node
from copper.parameter import CopperParameter

logger = logging.getLogger(__name__)


lastNum = re.compile(r'(?:[^\d]*(\d+)[^\d]*)+')

class OP_Network(OP_Node):
	"""
	This class implements all the network related methods to be used with Compy nodes. It handles child/parent relations, node creation, manipulation methods
	and tree traversal.

	"""
	__base__ = True

	def __init__(self, engine, parent):
		# mask is a list with node type names that are allowed to be created by this NetworkManager instance e.d ["img","comp"] If mask is None than any node type can be used
		super(OP_Network, self).__init__()
		self.__engine__ = engine
		self._name = None
		self.__node_dict__ = {}
		self.__parent__ = parent
		self.__network_label__ = None

	def asCode(self, brief=False, recurse=False, save_channels_only=False, save_creation_commands=True, save_keys_in_frames=False, save_outgoing_wires=False, 
		save_parm_values_only=False, save_spare_parms=True, function_name=None):
		'''
		Prints the Python code necessary to recreate a node.
		'''
		code = ""
		if self.parent() is None:
			# We are the root or base manager, so lets skip them
			pass

		elif self.parent() is self.engine:
			# We are base manager, so here it is
			code += '# Code for %s\n' % self.path()
			code += 'hou_node = hou.node(\"%s\")\n' % self.path()
		else:
			# We are node
			if recurse:
				code += self.parent().asCode()
				code += "hou_parent = hou_node\n"
			else:
				code += 'hou_parent = hou.node(\"%s\")\n' % self.parent().path()
			
			code += '# Code for %s\n' % self.path()
			code += 'hou_node = hou_parent.createNode(\"%s\", \"%s\")\n' % ( self.type().name(), self.name() )
		
		return code

	def children(self):
		'''
		Return a list of nodes that are children of this node. Using the file system analogy, a node's children are like the contents of a folder/directory.
		'''
		return tuple([self.__node_dict__[node_name] for node_name in self.__node_dict__])

	@classmethod
	def childTypeCategory(cls):
		'''
		Return the hou.NodeTypeCategory corresponding to the children of this node. For example, if this node is a geometry object, the children are SOPs. If it is an object subnet, the children are objects.
		'''
		raise NotImplementedError

	def createNode(self, node_type_name, node_name=None, run_init_scripts=True, load_contents=True, exact_type_name=False):
		'''
		Create a new node of type node_type_name as a child of this node.
		'''
		node = None
		if not self.isNetwork():
			raise BaseException("Unable to create node of type %s. %s is not a network manager !!!" % (node_type_name, self))

		if node_name:
			name = node_name
			if name in self.__node_dict__:
				name = self.getBase1Name(name)
		else:
			name = self.getBase1Name(node_type_name)

		node_type_name_with_category = '%s/%s' % (self.childTypeCategory().name(), node_type_name)
		logging.debug("Creating node %s inside %s" % (node_type_name_with_category, self.__class__.__name__))

		if node_type_name_with_category in OpRegistry._registry:
			node = OpRegistry[node_type_name_with_category](self.engine, self)	
			node.setName(name)
		else:
			raise BaseException("Invalid node type name \"%s\"" % node_type_name_with_category)	

		self.__node_dict__[name] = node

		if self.engine.gui_signals:
			self.engine.gui_signals.copperNodeCreated[str].emit(node.path())
		
		return node

	def createOutputNode(node_type_name, node_name=None, run_init_scripts=True, load_contents=True, exact_type_name=False):
		'''
		Create a new node and connect its first input to this node's (first) output. Return the new node.
		'''
		raise NotImplementedError

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

	def dumpLinks(self, recursive=False):
		links = []
		i = 0
		for input_node in self.inputs():		
			links += [(input_node.path(), self.path(), 0, i)]
			i += 1

		if recursive:
			for child_node in self.children():
				links += child_node.dumpLinks(recursive=True)	

		return links

	@property 
	def engine(self):
		return self.__engine__	

	def evalParm(self, parm_path):
		return self.parm(parm_path).eval()

	def errors(self):
		return

	def getBase1Name(self, base_name):
		""" look for the last sequence of number(s) in a string and increment """
		m = lastNum.search(base_name)
		if m:
			next = str(int(m.group(1))+1)
			start, end = m.span(1)
			name = base_name[:max(end-len(next), start)] + next + base_name[end:]
		else:
			name = "%s1" % base_name

		if name in self.__node_dict__:
			name = self.getBase1Name(name)

		return name

	@classmethod
	def isNetwork(cls):
		return True

	def isRoot(self):
		False

	def isSelected(self):
		return False

	@classmethod
	def label(cls):
		raise NotImplementedError

	def name(self):
		return self._name

	# return node object by it's path	
	def node(self, path):
		if not path:
			return None
			
		# check it path is string, if no then try to convert it
		if not isinstance(path, str):
			try:
				path = str(path)
			except:
				raise

		if path == "/":
			return self.root()

		path_list = [a for a in path.split("/") if a != '']
		if path[0] == "":
			# traverse from root
			return self.root().traverse(path_list)

		# traverse from this
		return self.traverse(path_list)		

	#def __str__(self):
	#	return self.__class__.__name__

	def parent(self):
		return self.__parent__	

	def path(self):
		"""returns path to this node as a string eg. /obj/geo1/file1"""
		if self.parent():
			if self.parent().parent():
				return "%s/%s" % (self.parent().path(), self.name())
			else:	
				return "/%s" % self.name()
		else:	
			return "/"

	def pathAsNodeList(self):
		"""returns path to this node as a list of nodes"""
		if not self.isRoot():
			path_list = self.parent().pathAsNodeList()
			path_list += [self]
		else:
			return []

		return path_list

	# return root node
	def root(self):
		return self.__engine__

	def setName(self, name):
		self._name = name

	def selectedChildren(self):
		return []

		# traverse nodes from this
	def traverse(self, path_list):
		node = self.__node_dict__.get(path_list[0])
		if not node: raise BaseException("Unable to get node %s in %s.traverse(self, path_list)" % (path_list[0], self))
		if len(path_list[1::]) > 0:
			# recursive traverse
			return node.traverse(path_list[1::])
		else:
			# return this node
			return node		

	def flush(self):
		self.__node_dict__ = {}

