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

	def node(self, path):
		return None
