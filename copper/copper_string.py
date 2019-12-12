from string import Template
import os


class CopperString(str):
	def __new__(cls, *args, **kw):
		return str.__new__(cls, *args, **kw)

	def __str__(self):
		return str.__str__(self)

	def unexpandedString(self):
		return self.__str__()	

	def expandedString(self, context = {}):
		string_template = Template( self.__str__() )
		if "frame" in context:
			frame = context["frame"]
		else:
			pass
		
		string_subs = string_template.substitute({
			'F': frame,
			'F2': '%02d' % frame,
			'F3': '%03d' % frame,
			'F4': '%04d' % frame,
			'F5': '%05d' % frame,
        })

		return os.path.expandvars(os.path.expanduser(string_subs))