#from .obj import ObjIO
import importlib
from copper import settings

for translator_path in settings.GEO_TRANSLATORS:
	importlib.import_module(translator_path)