from copper.core.op.node_type import NodeTypeBase
from copper.core.op.node_type_category import SopNodeTypeCategory
from copper.core.op.op_data_socket import OP_DataSocket

from copper.core.parameter.parm_template import *
from copper.core.data.geometry_data import GeometryData

from copper.sop import SOP_Node, SOPCookException


class SOP_File(SOP_Node):

	class NodeType(NodeTypeBase):
		icon_name = 'SOP_file'
		type_name = 'file'
		category = SopNodeTypeCategory

	def __init__(self, engine, parent):
		super(SOP_File, self).__init__(engine, parent)
		self._input_sockets = (
			OP_DataSocket(self, "input1", GeometryData),
		)
		self._output_sockets = (
			OP_DataSocket(self, "output1", GeometryData),
		)
		
	def parmTemplates(self):
		templates = super(SOP_Node, self).parmTemplates()
		templates += [
			MenuParmTemplate(name='filemode', label='File Mode', menu_items=('auto', 'read', 'write', 'none'), menu_labels=('Automatic',
 				'Read Files', 'Write Files', 'No Operation'), default_value=1),
			StringParmTemplate(name="filename", label="File", default_value=("",), string_type=StringParmType.FileReference),
		]
		
		return templates

	@classmethod
	def label(cls):
		return "File"

	def cookMySop(self, lock, context):
		with lock:
			filename = self.parm("filename").evalAsString()
			mode = self.parm("filemode").evalAsString()
			if filename:
				if mode == 'read':
					try:
						self._geometry.loadFromFile(filename)
					except:
						self._errors.append("Unable to read geometry from file: %s" % filename)
						raise
				elif mode == 'write':
					self._geometry.saveToFile(filename)
				elif mode == 'auto':
					raise SOPCookException('Unimplemented file mode "auto" !') 
				else:
					pass





