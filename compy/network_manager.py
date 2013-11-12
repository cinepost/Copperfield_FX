import re
lastNum = re.compile(r'(?:[^\d]*(\d+)[^\d]*)+')

class CLC_NetworkManager(object):
	"""
	This class implements all the network related methods to be used with Compy nodes. It handles child/parent relations, node creation, manipulation methods
	and tree traversal.

	"""
	def __init__(self, mask=None):
		# mask is a list with node type names that are allowed to be created by this NetworkManager instance e.d ["img","comp"] If mask is None than any node type can be used
		self.mask = mask
		self.__node_dict__ = {}
		self.parent = None
		self.__inputs__ = []
		self.__input_names__ = []

	def __increment__(self, s):
		""" look for the last sequence of number(s) in a string and increment """
		m = lastNum.search(s)
		if m:
			next = str(int(m.group(1))+1)
			start, end = m.span(1)
			s = s[:max(end-len(next), start)] + next + s[end:]
		return s	

	@property 
	def nodes(self):
		return self.__node_dict__

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

	def createNode(self, node_type=None):
		print "Creating node %s inside %s" % (node_type, self.__class__.__name__)

		if self.mask and node_type not in self.mask:
			print "Creating node of type %s not allowed by this manager." % node_type
			return None

		node = self.engine.filters[node_type](self.engine, self)
		self.__node_dict__[node.name()] = node
		if self.engine.network_cb:
			self.engine.network_cb()

		print "Created node %s childs is %s" % (node, node.children)	

		return node

	def name(self):
		return self.type_name	

	def path(self):
		if self.parent:
			return "%s/%s" % (self.parent.path(), self.name())

		return ""		

	# traverse nodes from this
	def traverse(self, path_list):
		print "Getting node: %s" % path_list
		node = self.nodes[path_list[0]]
		if len(path_list[1::]) > 0:
			# recursive traverse
			return node.traverse(path_list[1::])
		else:
			# return this node
			return node

	# return node object by it's path	
	def node(self, path):
		path_list = filter(lambda a: a != '', path.split("/"))
		
		if path[0] == "/":
			# traverse from root
			return self.root.traverse(path_list)
		else:	
			# traverse from this
			return self.traverse(path_list)

	# return root node
	@property
	def root(self):
		if self.parent:
			return self.parent.root
		else:
			return self				
