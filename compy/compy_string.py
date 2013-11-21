import string
import os

class CompyString(object):
	
	def __init__(self, engine, string_val, node = None):
		self.engine = engine
		self.node = node
		self.string_val = str(string_val)
	
	def unexpandedString(self):
		return self.string_val	

	def expandedString(self):
		string_template = string.Template( os.path.expandvars(self.string_val) )
		frame = self.engine.frame()
		string_expanded = string_template.substitute({
			'F': frame,
			'F2': '%02d' % frame,
			'F3': '%03d' % frame,
			'F4': '%04d' % frame,
			'F5': '%04d' % frame,
        })

		return string_expanded