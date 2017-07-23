from copper.sop import SOP_Node, SOPCookException
from copper.op.node_type import NodeTypeBase
from copper.op.node_type_category import SopNodeTypeCategory
from copper.op.op_connection import OP_Connection
from copper import parameter

from copper.parm_template import *
from copper.geometry import Geometry

class MyException(Exception):
    pass

raise MyException("My hovercraft is full of eels")

class SOP_File(SOP_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'SOP_file'
		type_name = 'file'
		category = SopNodeTypeCategory

	def __init__(self, engine, parent):
		super(SOP_File, self).__init__(engine, parent)
		self._inputs = (
			OP_Connection("input1"),
		)
		self._outputs = (
			OP_Connection("output1"),
		)
		
	def parmTemplates(self):
		templates = super(SOP_Node, self).parmTemplates()
		templates += [
			MenuParmTemplate(name='filemode', label='File Mode', menu_items=('auto', 'read', 'write', 'none'), menu_labels=('Automatic',
 				'Read Files', 'Write Files', 'No Operation'), default_value=1),
			StringParmTemplate(name="filename", label="File", default_value=("copper/media/obj/bunny.small.obj",), string_type=StringParmType.FileReference),
		]
		
		return templates

	@classmethod
	def label(cls):
		return "File"

	def cookMySop(self, lock):
		with lock:
			filename = self.parm("filename").evalAsString()
			mode = self.parm("filemode").evalAsString()
			if filename:
				if mode == 'read':
					self._geometry.loadFromFile(filename)
				elif mode == 'write':
					self._geometry.saveToFile(filename)
				elif mode == 'auto':
					raise 
				else:
					pass





