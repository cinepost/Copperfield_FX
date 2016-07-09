class ParmNamingScheme:
	Base1 = 1
	XYZW = 2
	RGBA = 3

class ParmLookScheme:
	Regular = 1

class ParmTemplateType:
	Button = 1
	Float = 2
	Folder = 3
	Int = 4
	Label = 5
	String = 6
	Toggle = 7
	Menu = 8

class StringParmType:
	Regular = 1
	FileReference = 2
	NodeReference = 3

class ParmTemplate(object):
	def __init__(self, name='parm', label='Label', length=1, default_value=(0,), min=0, max=10, min_is_strict=False, max_is_strict=False,
			naming_scheme=ParmNamingScheme.XYZW, look=ParmLookScheme.Regular):

		self._name = name
		self._label = label
		self._length = length
		self._default_vlaue = default_value
		self._min = min
		self._max = max
		self._min_is_strict = min_is_strict
		self._max_is_strict = max_is_strict
		self._naming_scheme = naming_scheme
		self._look = look

	def name(self):
		return self._name

	def label(self):
		return self._label

	def length(self):
		return self._length

	def numComponents(self):
		return self._length

	def defaultValue(self):
		return self._default_vlaue

	def min(self):
		return self._min

	def max(self):
		return self._max

	def minIsStrict(self):
		return self._min_is_strict

	def maxIsStrict(self):
		return self._max_is_strict

	def namingScheme(self):
		return self._naming_scheme

	def look(self):
		return self._look

	def joinWithNext(self):
		return False

	@classmethod
	def type(cls):
		return cls._type


class FloatParmTemplate(ParmTemplate):
	_type = ParmTemplateType.Float


class IntParmTemplate(ParmTemplate):
	_type = ParmTemplateType.Int 


class ButtonParmTemplate(ParmTemplate):
	_type = ParmTemplateType.Button


class ToggleParmTemplate(ParmTemplate):
	_type = ParmTemplateType.Toggle 
	def __init__(self, name="parm", label="Label", length=1, default_value=False):
		super(ToggleParmTemplate, self).__init__(name=name, label=label, length=length, default_value=default_value)


class MenuParmTemplate(ParmTemplate):
	_type = ParmTemplateType.Menu 
	def __init__(self, name="parm", label="Label", length=1, menu_items=('',), menu_labels=('',), default_value=0):
		super(MenuParmTemplate, self).__init__(name=name, label=label, length=length, default_value=default_value)
		self._menu_items = menu_items
		self._menu_labels = menu_labels

	def menuItems(self):
		return self._menu_items

	def menuLabels(self):
		return self._menu_labels


class StringParmTemplate(ParmTemplate):
	_type = ParmTemplateType.String
	def __init__(self,  name="parm", label="Label", length=1, default_value = ('',), string_type = StringParmType.NodeReference):
		super(StringParmTemplate, self).__init__(name=name, label=label, length=length, default_value=default_value)
		self._string_type = string_type

	def stringType(self):
		return self._string_type



		