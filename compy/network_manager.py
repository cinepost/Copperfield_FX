
class CLC_NetworkManager(object):
	node_dict = {}
	mask = None

	def __init__(self, mask=None):
		# mask is a list with node type names that are allowed to be created by this NetworkManager instance e.d ["img","comp"] If mask is None than any node type can be used
		self.mask = mask

	@property 
	def nodes(self):
		return self.node_dict

	def createNode(self, node_type=None):
		print "AAA"
		if self.mask and node_type not in self.mask:
			print "Creating node of type %s not allowed by this manager." % node_type
			return None

		node = self.engine.filters[node_type](self.engine)
		self.node_dict[node.name] = node
		if self.engine.network_cb:
			self.engine.network_cb()
		return node

