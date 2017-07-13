import logging

from op.op_engine import Copper_Engine
from copper import settings

logger = logging.getLogger(__name__)

logger.debug("Creating engine instance of type: %s" % settings.CL_DEVICE_TYPE)
engine = Copper_Engine(device_type = settings.CL_DEVICE_TYPE, device_index = settings.CL_DEVICE_INDEX, cl_path = settings.CL_PROGRAMS_PATH)