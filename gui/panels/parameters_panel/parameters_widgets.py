import os
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.signals import signals
from copper.parm_template import ParmLookScheme, ParmNamingScheme, ParmTemplateType, StringParmType

class ParameterBaseWidget(QtWidgets.QWidget):
	valueChanged = QtCore.pyqtSignal()
	def __init__(self, parent, parm):
		QtWidgets.QWidget.__init__(self, parent)
		self.parm = parm
		self.line_edit = None # Not all type of parm widget has line edit
		self.layout = QtWidgets.QHBoxLayout(self)
		self.layout.setSpacing(2)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.layout)

		self.valueChanged.connect(self.parmChanged)

	@QtCore.pyqtSlot()
	def parmChanged(self):
		parm_type = self.parm.parmTemplate().type()
		if parm_type is ParmTemplateType.Float:
			self.parm.set(float(self.line_edit.text()))
		elif parm_type is ParmTemplateType.Int:
			self.parm.set(int(self.line_edit.text()))
		elif parm_type is ParmTemplateType.String:
			self.parm.set(str(self.line_edit.text()))
		elif parm_type is ParmTemplateType.Menu:
			self.parm.set(int(self.combobox.currentIndex()))

	@QtCore.pyqtSlot()
	def setParmValueInt(self, value):
		self.parm.set(value)

	'''
	Handle drop event. Validate dropped data and set parameter.
	'''
	def eventFilter(self, source, event):
		if (event.type() == QtCore.QEvent.Drop and source is self.line_edit):
			if self.line_edit:
				self.line_edit.setText("")
				self.line_edit.dropEvent(event)
				if event.isAccepted():
					self.valueChanged.emit()
				return True
		return QtWidgets.QWidget.eventFilter(self, source, event) # propagate event


class ParameterFloatWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)
		self.resolution = 1000
		self.slider = None
		self.line_edit = QtWidgets.QLineEdit(str(self.parm.evalAsFloat())) 
		self.line_edit.setMinimumWidth(60)
		self.layout.addWidget(self.line_edit)

		if parm.parmTemplate().numComponents() == 1:
			self.line_edit.setMaximumWidth(140)
			self.slider = QtWidgets.QSlider(self)
			self.slider.setOrientation(QtCore.Qt.Horizontal)
			self.slider.setMinimum(self.parm.parmTemplate().min() * self.resolution)
			self.slider.setMaximum(self.parm.parmTemplate().max() * self.resolution)
			self.slider.setValue(self.parm.evalAsFloat() * self.resolution)
			self.slider.setSingleStep(1)
			self.slider.setTracking(True)
			self.slider.valueChanged.connect(self.processSlider)
			self.layout.addWidget(self.slider)

		# connect signals
		self.line_edit.editingFinished.connect(self.processLineEdit)

	def processSlider(self):
		value = self.slider.value()
		self.line_edit.setText(str(float(value)/self.resolution))
		self.valueChanged.emit()

	def processLineEdit(self):
		value = float(self.line_edit.text())
		if self.slider: self.slider.setValue(value)
		self.valueChanged.emit()

class ParameterIntWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)
		self.slider = None
		self.line_edit = QtWidgets.QLineEdit(str(self.parm.evalAsInt())) 
		self.line_edit.setMinimumWidth(60)
		self.layout.addWidget(self.line_edit)

		if parm.parmTemplate().numComponents() == 1:
			self.line_edit.setMaximumWidth(140)
			self.slider = QtWidgets.QSlider(self)
			self.slider.setOrientation(QtCore.Qt.Horizontal)
			self.slider.setMinimum(parm.parmTemplate().min())
			self.slider.setMaximum(parm.parmTemplate().max())
			self.slider.setValue(self.parm.evalAsInt())
			self.slider.setTracking(True)
			self.slider.setTickInterval(1)
			self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
			self.slider.valueChanged.connect(self.processSlider)
			self.layout.addWidget(self.slider)

		# connect signals
		self.line_edit.editingFinished.connect(self.processLineEdit)

	def processSlider(self):
		value = self.slider.value()
		self.line_edit.setText(str(value))
		self.valueChanged.emit()

	def processLineEdit(self):
		value = int(self.line_edit.text())
		if self.slider: self.slider.setValue(value)
		self.valueChanged.emit()


class ParameterToggleWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.checkbox = QtWidgets.QCheckBox(self)
		self.checkbox.setCheckState(self.parm.evalAsBool())

		self.label = QtWidgets.QLabel(parm.parmTemplate().label())
		self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		self.label.setStatusTip(parm.name())

		self.layout.addWidget(self.checkbox)
		self.layout.addWidget(self.label)
		self.layout.addStretch(1)

		# connect signals
		self.checkbox.stateChanged.connect(self.parmChanged)


class ParameterMenuWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.combobox = QtWidgets.QComboBox(self)
		for item_label in self.parm.menuLabels():
			self.combobox.addItem(item_label)

		self.combobox.setCurrentIndex(parm.evalAsInt())

		self.layout.addWidget(self.combobox)

		if parm.parmTemplate().numComponents() == 1:
			self.layout.addStretch(1)

		# connect signals
		self.combobox.currentIndexChanged.connect(self.parmChanged)


class ParameterButtonWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.button = QtWidgets.QPushButton(parm.parmTemplate().label(), self)
		self.button.setMinimumWidth(60)

		self.layout.addWidget(self.button)
		
		if parm.parmTemplate().numComponents() == 1:
			self.button.setMaximumWidth(140)
			self.layout.addStretch(1)

		# connect signals
		self.button.clicked.connect(parm.pressButton)


class ParameterStringWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.line_edit = QtWidgets.QLineEdit(parm.evalAsString())
		self.line_edit.setDragEnabled(True)
		self.line_edit.setAcceptDrops(True)
		self.line_edit.installEventFilter(self) # process drag'n'drop
		self.layout.addWidget(self.line_edit)

		if parm.parmTemplate().stringType() is StringParmType.FileReference:
			self.file_button = QtWidgets.QToolButton(self)
			self.file_button.setObjectName("file")
			self.file_button.clicked.connect(self.BrowseFile)
			self.layout.addWidget(self.file_button)
		elif parm.parmTemplate().stringType() is StringParmType.NodeReference:
			self.op_jump_button = QtWidgets.QToolButton(self)
			self.op_jump_button.setObjectName("op_jump")

			self.op_path_button = QtWidgets.QToolButton(self)
			self.op_path_button.setObjectName("op_path")
			self.op_path_button.clicked.connect(self.BrowseOp)

			self.layout.addWidget(self.op_jump_button)
			self.layout.addWidget(self.op_path_button)	

		# connect signals
		self.line_edit.editingFinished.connect(self.parmChanged)

	def BrowseFile(self, lineEdit):
		file_path, wildcard = QtWidgets.QFileDialog.getOpenFileName()
		self.line_edit.setText(file_path)
		self.valueChanged.emit()

	def BrowseOp(self, lineEdit):
		op_path = QtWidgets.QFileDialog.getOpenFileName()
		self.line_edit.setText(op_path)
		self.valueChanged.emit()








