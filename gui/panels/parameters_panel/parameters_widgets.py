import os
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.signals import signals
from copper.parm_template import ParmLookScheme, ParmNamingScheme, ParmTemplateType, StringParmType

class ParmSignals(QtCore.QObject):
	valueChanged = QtCore.pyqtSignal(object)

	def __init__(self, parent=None):  
		QtCore.QObject.__init__(self, parent)

class ParameterBaseWidget(QtWidgets.QWidget):
	def __init__(self, parent, parm):
		QtWidgets.QWidget.__init__(self, parent)
		self.signals = ParmSignals()
		self.parm = parm
		self.line_edit = None # Not all type of parm widget has line edit
		self._line_edit_changed = False

		self.layout = QtWidgets.QHBoxLayout(self)
		self.layout.setSpacing(2)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.layout)

		# connect signals
		self.signals.valueChanged.connect(self.parmChanged)
		self.parm.signals.parameterChanged.connect(self.updateWidget) # sent by CopperParameter

	def updateWidget(self):
		pass # TODO: raise uniplemented exception

	@QtCore.pyqtSlot(object)
	def parmChanged(self, value):
		parm_type = self.parm.parmTemplate().type()
		if parm_type is ParmTemplateType.Float:
			self.parm.set(float(value))
		elif parm_type is ParmTemplateType.Int:
			self.parm.set(int(value))
		elif parm_type is ParmTemplateType.String:
			self.parm.set(str(value))
		elif parm_type is ParmTemplateType.Menu:
			self.parm.set(int(value))

	'''
	Handle drop event. Validate dropped data and set parameter.
	'''
	def eventFilter(self, source, event):
		if (event.type() == QtCore.QEvent.Drop and source is self.line_edit):
			self.line_edit.setText("")
			self.parm.set(event.mimeData().text())
			#if self.line_edit:
			#	self.line_edit.setText("")
			#	self.line_edit.dropEvent(event)
			#	if event.isAccepted():
					#self.valueChanged.emit()
			#		self.parm.set(str(value))
			#	return True
		
		return QtWidgets.QWidget.eventFilter(self, source, event) # propagate event


class ParameterNumericalBaseWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		parm_template = self.parm.parmTemplate()

		if parm_template.type() is ParmTemplateType.Int:
			self.slider_resolution = 1
		else:
			self.slider_resolution = 1000

		self.line_edit = QtWidgets.QLineEdit(self.calcLineEditValueFromParm())
		self.line_edit.setMinimumWidth(60)
		self.line_edit_needs_update = False
		self.layout.addWidget(self.line_edit)
		self.slider = None

		if self.parm.parmTemplate().numComponents() == 1:
			self.line_edit.setMaximumWidth(140)
			self.slider_needs_update = False
			self.slider = QtWidgets.QSlider(self)
			self.slider.setOrientation(QtCore.Qt.Horizontal)
			self.slider.setMinimum(parm_template.min() * self.slider_resolution)
			self.slider.setMaximum(parm_template.max() * self.slider_resolution)
			self.slider.setValue(self.calcSliderValueFromParm())
			self.slider.setSingleStep(1)
			self.slider.setTracking(True)
			self.slider.sliderMoved[int].connect(self.processSlider)
			self.layout.addWidget(self.slider)

		# connect signals
		self.line_edit.editingFinished.connect(self.processLineEdit)
		#self.line_edit.textChanged.connect(self._lineEditChanged)

	def calcLineEditValueFromParm(self):
		return str(self.parm.eval())

	def calcSliderValueFromParm(self):
		return self.parm.eval() * self.slider_resolution

	@QtCore.pyqtSlot()
	def updateWidget(self):
		if self.line_edit_needs_update:
			self.line_edit.setText(self.calcLineEditValueFromParm())
			self.line_edit_needs_update = False

		if self.slider_needs_update and self.slider:
			self.slider.setValue(self.calcSliderValueFromParm())
			self.slider_needs_update = False

	@QtCore.pyqtSlot(int)
	def processSlider(self, value):
		self.line_edit_needs_update = True
		value = self.slider.value()
		self.signals.valueChanged.emit(float(value)/self.slider_resolution)

	@QtCore.pyqtSlot()
	def processLineEdit(self):
		self.slider_needs_update = True
		value = self.line_edit.text()
		self.signals.valueChanged.emit(value)

class ParameterFloatWidget(ParameterNumericalBaseWidget):
	def __init__(self, parent, parm):
		ParameterNumericalBaseWidget.__init__(self, parent, parm)


class ParameterIntWidget(ParameterNumericalBaseWidget):
	def __init__(self, parent, parm):
		ParameterNumericalBaseWidget.__init__(self, parent, parm)


class ParameterToggleWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.checkbox = QtWidgets.QCheckBox(self)
		self.checkbox.setCheckState(self.parm.evalAsBool())
		self.checkbox.setTristate(on=False)

		self.label = QtWidgets.QLabel(parm.parmTemplate().label())
		self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		self.label.setStatusTip(parm.name())

		self.layout.addWidget(self.checkbox)
		self.layout.addWidget(self.label)
		self.layout.addStretch(1)

		# connect signals
		self.checkbox.stateChanged.connect(self.processCheckbox)

	def processCheckbox(self, state):
		self.signals.valueChanged.emit(state)


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
		self.combobox.currentIndexChanged.connect(self.processMenu)

	def processMenu(self, item):
		self.signals.valueChanged.emit(item)


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
			self.file_button.clicked.connect(self.browseFile)
			self.layout.addWidget(self.file_button)
		elif parm.parmTemplate().stringType() is StringParmType.NodeReference:
			self.op_jump_button = QtWidgets.QToolButton(self)
			self.op_jump_button.setObjectName("op_jump")

			self.op_path_button = QtWidgets.QToolButton(self)
			self.op_path_button.setObjectName("op_path")
			self.op_path_button.clicked.connect(self.browseOp)

			self.layout.addWidget(self.op_jump_button)
			self.layout.addWidget(self.op_path_button)	

		# connect signals
		self.line_edit.editingFinished.connect(self.processLineEdit)

	def processLineEdit(self):
		value = self.line_edit.text()
		self.signals.valueChanged.emit(value)

	def browseFile(self, lineEdit):
		file_path, wildcard = QtWidgets.QFileDialog.getOpenFileName()
		self.line_edit.setText(file_path)
		self.signals.valueChanged.emit(file_path)

	def browseOp(self, lineEdit):
		#op_path = QtWidgets.QFileDialog.getOpenFileName()
		#self.line_edit.setText(op_path)
		#self.valueChanged.emit()
		pass







