import itertools
import uuid

class CopperObject():
	id_iter = itertools.count()

	def __init__(self):
		self._id = next(self.id_iter)
		self._uuid = uuid.uuid4()

	def id(self):
		return self._id

	def uuid(self):
		return self._uuid