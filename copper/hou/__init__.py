import logging
from copper import ui

from copper import settings
from copper.engine import Engine

logger = logging.getLogger(__name__)

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


node = _engine.node

fps =_engine.fps

time = _engine.time

frame = _engine.frame	

def setFps(fps):
	_engine.setFps(fps)	

def setTime(time):
	_engine.setTime(time)

def setFrame(frame):
	_engine.setFrame(frame)
