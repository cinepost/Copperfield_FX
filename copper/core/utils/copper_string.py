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
		if "frame" in context:
			frame = context["frame"]
		else:
			frame = 0 # TODO: proper time and animation substituon needed
		
		expanded_string = os.path.expandvars(os.path.expanduser(self.__str__()))

		string_template = Template(expanded_string)
		string_subst = string_template.substitute({
			'F': frame,
			'F2': '%02d' % frame,
			'F3': '%03d' % frame,
			'F4': '%04d' % frame,
			'F5': '%05d' % frame,
        })

		return string_subst