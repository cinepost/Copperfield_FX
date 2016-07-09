from string import Template
import os

class CopperString(object):
	
	def __init__(self, string_val):
		self.string_val = str(string_val)
	
	def __str__(self):
		return self.string_val

	def unexpandedString(self):
		return self.string_val	

	def expandedString(self, context = {}):
		string_template = Template( os.path.expandvars(self.string_val) )
		if "frame" in context:
			frame = context["frame"]
		else:
			pass	
			#frame = engine.frame()
		
		string_expanded = string_template.substitute({
			'F': frame,
			'F2': '%02d' % frame,
			'F3': '%03d' % frame,
			'F4': '%04d' % frame,
			'F5': '%04d' % frame,
        })

		return string_expanded