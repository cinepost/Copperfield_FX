PyQt_API_Impl = None
PyQt_API = None

try:
	import PyQt5 as PyQt_API
	PyQt_API_Impl = "PyQt5"
except ImportError:
	pass

try:
	import PySide2 as PyQt_API
	PyQt_API_Impl = "PySide2"
except ImportError:
	pass

if PyQt_API_Impl == None:
	raise Exception("No Qt for Python implementation found !!! PyQt5 or PySide2 required.")
