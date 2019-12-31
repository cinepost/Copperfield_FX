import sys
import logging

from copper import settings
from copper.core.config import Config
from copper.core.engine import Engine

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

thismodule = sys.modules[__name__]

# variables section
#----------------------------------------------
setattr(thismodule, 'fps', _engine.fps)
setattr(thismodule, 'time', _engine.time)
setattr(thismodule, 'frame', _engine.frame)

setattr(thismodule, 'setFps', _engine.setFps)
setattr(thismodule, 'setTime', _engine.setTime)
setattr(thismodule, 'setFrame', _engine.setFrame)

# methods section
#----------------------------------------------

setattr(thismodule, 'isUIAvailable', _config.hasUI)

setattr(thismodule, 'root', lambda root=_engine.root: root)
setattr(thismodule, 'pwd', _engine.pwd)
setattr(thismodule, 'setPwd', _engine.setPwd)

setattr(thismodule, 'node', _engine.node)
setattr(thismodule, 'setFps', _engine.setFps)
setattr(thismodule, 'setTime', _engine.setTime)
setattr(thismodule, 'setFrame', _engine.setFrame)

# classes section
#----------------------------------------------
from copper.core.parameter import CopperParameter
from copper.core.data import GeometryData
from copper.core.data.geometry_data.primitive import Point, Vertex, Polygon

setattr(thismodule, 'Point', Point)
setattr(thismodule, 'Vertex', Vertex)
setattr(thismodule, 'Polygon', Polygon)
setattr(thismodule, 'Parm', CopperParameter)
setattr(thismodule, 'Geometry', GeometryData)


# Modules section
#----------------------------------------------
from copper.core.data.image_data import ImageDepth
from copper.core.parameter.parm_template import StringParmType

if _config.hasUI():
	from copper import ui
	setattr(thismodule, 'ui', thismodule.ui)

setattr(thismodule, 'imageDepth', ImageDepth)
setattr(thismodule, 'stringParmType', StringParmType)