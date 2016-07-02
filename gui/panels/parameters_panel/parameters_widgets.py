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
		self.line_edit.editingFinished.connect(self.setParmValue)

		self.slider = QtGui.QSlider(self)
		self.slider.setOrientation(QtCore.Qt.Horizontal)
		self.slider.setMinimum(0)
		self.slider.setMaximum(100)
		self.slider.setTracking(True)

		self.layout.addWidget(self.line_edit)
		self.layout.addWidget(self.slider)


class ParameterIntWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.line_edit = QtGui.QLineEdit(str(self.parm.evalAsInt())) 
		self.line_edit.setMinimumWidth(60)
		self.line_edit.setMaximumWidth(140)
		self.line_edit.editingFinished.connect(self.setParmValue)

		self.slider = QtGui.QSlider(self)
		self.slider.setOrientation(QtCore.Qt.Horizontal)
		self.slider.setMinimum(0)
		self.slider.setMaximum(100)
		self.slider.setTracking(True)

		self.layout.addWidget(self.line_edit)
		self.layout.addWidget(self.slider)


class ParameterBoolWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.checkbox = QtGui.QCheckBox(self)
		self.checkbox.setCheckState(self.parm.evalAsBool())
		self.checkbox.stateChanged.connect(self.setParmValue)

		self.label = QtGui.QLabel(parm.label())
		self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		self.label.setStatusTip(parm.name())

		self.layout.addWidget(self.checkbox)
		self.layout.addWidget(self.label)
		self.layout.addStretch(1)


class ParameterChoiceWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		combobox = QtGui.QComboBox(self)
		for item_name in self.parm.__menu_items__:
			combobox.addItem(parm.__menu_items__[item_name])

		combobox.setCurrentIndex(parm.evalAsInt())

		self.layout.addWidget(combobox)
		self.layout.addStretch(1)


class ParameterFilePathWidget(ParameterBaseWidget):
	def __init__(self, parent, parm):
		ParameterBaseWidget.__init__(self, parent, parm)

		self.file_path_widget = QtGui.QLineEdit(parm.evalAsStr())
		self.file_path_widget.editingFinished.connect(self.setParmValue)           
		self.file_button = QtGui.QToolButton(self)
		self.file_button.setObjectName("file")
		self.file_button.clicked.connect(lambda: self.BrowseFile(self.file_path_widget))
		
		self.layout.addWidget(self.file_path_widget)
		self.layout.addWidget(self.file_button)

	def BrowseFile(self, lineEdit):
		file_name = QtGui.QFileDialog.getOpenFileName()
		self.file_path_widget.setText(file_name)



