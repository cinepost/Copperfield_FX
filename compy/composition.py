from compy import base

class CLC_Composition(base.CLC_Node):
	engine 	= None
	nodes 	= {}
	
	def __init__(self, engine):
		self.engine = engine
		
	def createNode(self, node_type=None, node_name=None):
		if not node_type:
			raise BaseException("No node type specified")
		else:
			try:
				fx = self.engine.filters[node_type]
				print "Creating fx: %s " % fx
				node = fx(self.engine)
			except:
				raise
				return None	
			else:
				self.nodes[node.name] = node
				return node		
