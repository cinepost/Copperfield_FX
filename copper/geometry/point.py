from copper.vmath import Vector3


class Point(Vector3):

	def setPosition(self, pos):
		self.comps = pos

	def position(self):
		return self.comps