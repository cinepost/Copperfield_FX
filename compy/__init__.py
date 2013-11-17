import inspect
import string
#import pyopencl as cl
#import numpy
from compy.engines import CLC_Engine as engine
import settings
import base

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
					print "FX filter %s loaded..." % obj
			elif hasattr(obj, "__mgr__"):
					ops[obj.type_name] = obj
					print "Network manager %s loaded..." % obj
								


def CreateEngine(device_type):
	return engine(device_type, ops, settings.cl_path)
