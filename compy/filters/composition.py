from compy import base
import compy.network_manager as network_manager

class CLC_Composition(base.CLC_Node, network_manager.CLC_NetworkManager):
	__mgr__ = True # Indicates that this is a network manager node
	engine 	= None
	name 	= 'comp'

	def __init__(self, engine):
		self.engine = engine