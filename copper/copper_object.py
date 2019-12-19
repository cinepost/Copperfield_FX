import uuid

class CopperObject():
	def __init__(self):
		self.__uuid__ = uuid.uuid4()

	def uuid(self):
		return self.__uuid__