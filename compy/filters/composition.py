from compy import base
import compy.network_manager as network_manager

class CLC_Composition(base.CLC_Node, network_manager.CLC_NetworkManager):
	__mgr__ 	= True # Indicates that this is a network manager node
	type_name 	= 'comp'

	def __init__(self, engine, parent):
		network_manager.CLC_NetworkManager.__init__(self)
		base.CLC_Node.__init__(self, parent)
		self.engine = engine
