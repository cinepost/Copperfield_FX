import os
os.environ["PYOPENCL_COMPILER_OUTPUT"] = "1"
os.environ["PYOPENCL_NO_CACHE"] = "1"

if not os.environ.get("COPPER_HOME"):
	cwd = os.getcwd()
	print "Using current directory %s as $COPPER_HOME" % cwd
	os.environ["COPPER_HOME"] = cwd

import inspect
from op.op_engine import Copper_Engine
import settings

from rop import *
from obj import *
from cop2 import *
from sop import *

from copper.op.node_type_category import NodeTypeCategoryRegistry

def nodeTypeCategories():
	print NodeTypeCategoryRegistry._registry_aliases

def CreateEngine(device_type = None, device_index=None):
	print "Creating engine instance of type: %s" % device_type
	return Copper_Engine(device_type = device_type, device_index=device_index, cl_path=settings.cl_path)

engine = CreateEngine("GPU",0)
