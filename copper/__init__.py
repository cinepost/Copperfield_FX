import os
import logging 
logger = logging.getLogger(__name__)

os.environ["PYOPENCL_COMPILER_OUTPUT"] = "1"
os.environ["PYOPENCL_NO_CACHE"] = "0"

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
from copper.engine import Engine
from .copper_object import CopperObject

def nodeTypeCategories():
    logger.debug(NodeTypeCategoryRegistry._registry_aliases)
