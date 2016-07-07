from PyQt4 import QtCore, QtGui

from gui.signals import signals

class ParameterBaseWidget(QtGui.QWidget):
	def __init__(self, parent, parm):
		QtGui.QWidget.__init__(self, parent)
		self.parm = parm 
		self.layout = QtGui.QHBoxLayout(self)
		self.layout.setSpacing(2)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.layout)

	def setParmValue(self):
		#self.parm.setValueFloat(float(self.line_edit.text()))
		pass

class ParameterFloatWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.line_edit = QtGui.QLineEdit(str(self.parm.evalAsFloat())) 
		self.line_edit.setMinimumWidth(60)
		self.line_edit.setMaximumWidth(140)

		self.slider = QtGui.QSlider(self)
		self.slider.setOrientation(QtCore.Qt.Horizontal)
		self.slider.setMinimum(0)
		self.slider.setMaximum(100)
		self.slider.setTracking(True)

		self.layout.addWidget(self.line_edit)
		self.layout.addWidget(self.slider)

		# connect signals
		self.line_edit.editingFinished.connect(self.setParmValue)


class ParameterIntWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.line_edit = QtGui.QLineEdit(str(self.parm.evalAsInt())) 
		self.line_edit.setMinimumWidth(60)
		self.line_edit.setMaximumWidth(140)

		self.slider = QtGui.QSlider(self)
		self.slider.setOrientation(QtCore.Qt.Horizontal)
		self.slider.setMinimum(0)
		self.slider.setMaximum(100)
		self.slider.setTracking(True)

		self.layout.addWidget(self.line_edit)
		self.layout.addWidget(self.slider)

		# connect signals
		self.line_edit.editingFinished.connect(self.setParmValue)


class ParameterBoolWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.checkbox = QtGui.QCheckBox(self)
		self.checkbox.setCheckState(self.parm.evalAsBool())

		self.label = QtGui.QLabel(parm.label())
		self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		self.label.setStatusTip(parm.name())

		self.layout.addWidget(self.checkbox)
		self.layout.addWidget(self.label)
		self.layout.addStretch(1)

		# connect signals
		self.checkbox.stateChanged.connect(self.setParmValue)


class ParameterChoiceWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		combobox = QtGui.QComboBox(self)
		for item_name in self.parm.__menu_items__:
			combobox.addItem(parm.__menu_items__[item_name])

		combobox.setCurrentIndex(parm.evalAsInt())

		self.layout.addWidget(combobox)
		self.layout.addStretch(1)


class ParameterButtonWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.button = QtGui.QPushButton(parm.label(), self)
		self.button.setMinimumWidth(60)
		self.button.setMaximumWidth(140)

		self.layout.addWidget(self.button)
		self.layout.addStretch(1)

		# connect signals
		self.button.clicked.connect(parm.getCallback())


class ParameterFilePathWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.file_path_widget = QtGui.QLineEdit(parm.evalAsStr()) 

		self.file_button = QtGui.QToolButton(self)
		self.file_button.setObjectName("file")
		
		self.layout.addWidget(self.file_path_widget)
		self.layout.addWidget(self.file_button)

		# connect signals
		self.file_path_widget.editingFinished.connect(self.setParmValue)
		self.file_button.clicked.connect(lambda: self.BrowseFile(self.file_path_widget))

	def BrowseFile(self, lineEdit):
		file_name = QtGui.QFileDialog.getOpenFileName()
		self.file_path_widget.setText(file_name)


class ParameterOpPathWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.op_path_widget = QtGui.QLineEdit(parm.evalAsStr())
		self.op_path_widget.setDragEnabled(True)
		self.op_path_widget.setAcceptDrops(True)
		self.op_path_widget.installEventFilter(self)
           

		self.op_jump_button = QtGui.QToolButton(self)
		self.op_jump_button.setObjectName("op_jump")

		self.op_path_button = QtGui.QToolButton(self)
		self.op_path_button.setObjectName("op_path")
		
		self.layout.addWidget(self.op_path_widget)
		self.layout.addWidget(self.op_jump_button)
		self.layout.addWidget(self.op_path_button)

		# connect signals
		self.op_path_widget.editingFinished.connect(self.setParmValue)
		self.op_path_button.clicked.connect(lambda: self.BrowseOp(self.op_path_widget))

	def BrowseOp(self, lineEdit):
		op_path = QtGui.QFileDialog.getOpenFileName()
		self.op_path_widget.setText(op_path)






