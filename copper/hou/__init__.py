import logging
from copper import ui

from copper import settings
from copper.config import Config
from copper.engine import Engine

logger = logging.getLogger(__name__)

_config = Config()
_engine = Engine(device_type = settings.CL_DEVICE_TYPE, device_index=settings.CL_DEVICE_INDEX, cl_path=settings.CL_PROGRAMS_PATH)

# non-standard hou module stuff

def engine():
	return _engine

class OpenCL():

	@classmethod
	def have_gl(cls):
		return _engine.have_gl()

	@classmethod
	def context(cls, device_index=0):
		return _engine.openclContext(device_index)

	@classmethod
	def queue(cls):
		return _engine.openclQueue()		

# standard hou module stuff	

class hipFile():

	@classmethod
	def load(cls, filename): 
		if not filename:
			_engine.build_test_project()
		else:
			_engine.load(filename)


fps =_engine.fps

time = _engine.time

frame = _engine.frame	

def isUIAvailable():
	'''
	Return whether or not the .ui module is available.
	'''
	return True

import sys
from copper.parameter import CopperParameter

thismodule = sys.modules[__name__]

# variables section
#----------------------------------------------

setattr(thismodule, 'setFps', _engine.setFps)
setattr(thismodule, 'setTime', _engine.setTime)
setattr(thismodule, 'setFrame', _engine.setFrame)

# methods section
#----------------------------------------------

setattr(thismodule, 'isUIAvailable', _config.hasUI)

setattr(thismodule, 'node', _engine.node)
setattr(thismodule, 'setFps', _engine.setFps)
setattr(thismodule, 'setTime', _engine.setTime)
setattr(thismodule, 'setFrame', _engine.setFrame)

# classes section
#----------------------------------------------

setattr(thismodule, 'Parm', CopperParameter)


# Modules section
#----------------------------------------------

setattr(thismodule, 'ui', thismodule.ui)