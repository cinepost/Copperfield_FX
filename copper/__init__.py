import os
import logging 
logger = logging.getLogger(__name__)

os.environ["PYOPENCL_COMPILER_OUTPUT"] = "1"
os.environ["PYOPENCL_NO_CACHE"] = "1"

if not os.environ.get("COPPER_HOME"):
    cwd = os.getcwd()
    logger.info("Using current directory %s as $COPPER_HOME" % cwd)
    os.environ["COPPER_HOME"] = cwd

from copper import settings

from .rop import *
from .obj import *
from .cop2 import *
from .sop import *

from copper.op.node_type_category import NodeTypeCategoryRegistry
from copper.op.op_engine import OP_Engine


def nodeTypeCategories():
    logger.debug(NodeTypeCategoryRegistry._registry_aliases)

hou = OP_Engine(device_type = settings.CL_DEVICE_TYPE, device_index=settings.CL_DEVICE_INDEX, cl_path=settings.CL_PROGRAMS_PATH)