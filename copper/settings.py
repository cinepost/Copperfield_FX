# Basic Copperfield FX settings

# OpenCl defaults
CL_DEVICE_TYPE = "GPU"
CL_DEVICE_INDEX = 0
CL_PROGRAMS_PATH = "$COPPER_HOME/copper/cl"


# Animation defaults
DEFAULT_FPS = 24.0

# Geometry translators modules
GEO_TRANSLATORS = [
	'copper.core.data.geometry_data.iotranslators.obj',
	'copper.core.data.geometry_data.iotranslators.bgeo',
]