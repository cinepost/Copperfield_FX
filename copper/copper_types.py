
class CopperFloat2(object):
	def __init__(self, x=0.0, y=0.0):
		self.x = float(x)
		self.y = float(y)

class CopperFloat3(CopperFloat2):
	def __init__(self, x=0.0, y=0.0, z=0.0):
		CopperFloat2.__init__(self, x, y)
		self.z = float(z)

class CopperFloat4(CopperFloat3):
	def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
		CopperFloat32.__init__(self, x, y, z)
		self.w = float(w)

class CopperInt2(object):
	def __init__(self, x=0.0, y=0.0):
		self.x = int(x)
		self.y = int(y)

class CopperInt3(CopperInt2):
	def __init__(self, x=0.0, y=0.0, z=0.0):
		CopperFloat2.__init__(self, x, y)
		self.z = int(z)

class CopperInt4(CopperInt3):
	def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
		CopperFloat32.__init__(self, x, y, z)
		self.w = int(w)