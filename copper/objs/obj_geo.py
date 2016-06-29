from copper.op_manager import OP_Manager

class OBJ_Geo(OP_Manager):
	icon_name = 'icons/nodes/OBJ_geo.svg'

	def __init__(self, engine, parent):
		super(OBJ_Geo, self).__init__(engine, parent, mask=None)

	@classmethod
	def isNetwork(cls):
		return True

	@classmethod
	def type(cls):
		return "geo"

	@classmethod
	def isOp(cls):
		return True

	@classmethod
	def label(cls):
		return "Geometry"
