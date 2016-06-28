import os
os.environ["PYOPENCL_COMPILER_OUTPUT"] = "1"
os.environ["PYOPENCL_NO_CACHE"] = "1"

if not os.environ.get("COPPER_HOME"):
	cwd = os.getcwd()
	print "Using current directory %s as $COPPER_HOME !!!" % cwd
	os.environ["COPPER_HOME"] = cwd

import inspect
from op_engine import Copper_Engine as engine
import settings

print "Loading operators..."

ops = {}

for module_name in settings.cop_modules + settings.out_modules:
	module = __import__(module_name, fromlist="*")
	for name in dir(module):
		obj = getattr(module, name)
		if inspect.isclass(obj):
			if hasattr(obj,"__op__"):
				if obj.type_name:
					ops[obj.type_name] = obj
					print "Operator %s loaded..." % obj
			elif hasattr(obj, "__mgr__"):
					ops[obj.type_name] = obj
					print "Network manager %s loaded..." % obj
								


def CreateEngine(device_type = None, device_index=None):
	print "Creating engine instance of type: %s" % device_type
	return engine(device_type = device_type, device_index=device_index, ops=ops, cl_path=settings.cl_path)
