import re
lastNum = re.compile(r'(?:[^\d]*(\d+)[^\d]*)+')

def increment(s):
    """ look for the last sequence of number(s) in a string and increment """
    m = lastNum.search(s)
    if m:
        next = str(int(m.group(1))+1)
        start, end = m.span(1)
        s = s[:max(end-len(next), start)] + next + s[end:]
    return s

class CLC_NetworkManager(object):
	
	def __init__(self, mask=None):
		# mask is a list with node type names that are allowed to be created by this NetworkManager instance e.d ["img","comp"] If mask is None than any node type can be used
		self.mask = mask
		self.node_dict = {}
		self.parent = None

	@property 
	def nodes(self):
		return self.node_dict

	@property
	def children(self):
		if self.node_dict != {}:
			return self.node_dict	
		else:
			return None	

	def createNode(self, node_type=None):
		print "Creating node %s inside %s" % (node_type, self.__class__.__name__)

		if self.mask and node_type not in self.mask:
			print "Creating node of type %s not allowed by this manager." % node_type
			return None

		node = self.engine.filters[node_type](self.engine, self)
		self.node_dict[node.name] = node
		if self.engine.network_cb:
			self.engine.network_cb()

		print "Created node %s childs is %s" % (node, node.children)	

		return node

	@property 	
	def path(self):
		if self.parent:
			return "%s/%s" % (self.parent.path, self.name)

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
