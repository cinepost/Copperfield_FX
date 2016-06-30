from PyQt4 import QtCore, QtGui

from gui.signals import signals

class ParameterFloatWidget(QtGui.QWidget):
	def __init__(self, parent, parm):
		QtGui.QWidget.__init__(self, parent)
		self.parm = parm

		layout = QtGui.QHBoxLayout()
		layout.setSpacing(2)
		layout.setContentsMargins(0, 0, 0, 0)

		self.line_edit = QtGui.QLineEdit(str(self.parm.evalAsFloat())) 
		self.line_edit.setMinimumWidth(60)
		self.line_edit.setMaximumWidth(140)
		self.line_edit.editingFinished.connect(self.setParmValue)

		valueSlider = QtGui.QSlider()
		valueSlider.setOrientation(QtCore.Qt.Horizontal)
		valueSlider.setMinimum(0)
		valueSlider.setMaximum(100)
		valueSlider.setTracking(True)

		layout.addWidget(self.line_edit)
		layout.addWidget(valueSlider)

		self.setLayout(layout)

	def setParmValue(self):
		self.parm.setValueFloat(float(self.line_edit.text()))


class ParameterIntWidget(QtGui.QWidget):
	def __init__(self, parent, parm):
		QtGui.QWidget.__init__(self, parent)
		self.parm = parm

		layout = QtGui.QHBoxLayout()
		layout.setSpacing(2)
		layout.setContentsMargins(0, 0, 0, 0)

		self.line_edit = QtGui.QLineEdit(str(self.parm.evalAsInt())) 
		self.line_edit.setMinimumWidth(60)
		self.line_edit.setMaximumWidth(140)
		self.line_edit.editingFinished.connect(self.setParmValue)

		valueSlider = QtGui.QSlider()
		valueSlider.setOrientation(QtCore.Qt.Horizontal)
		valueSlider.setMinimum(0)
		valueSlider.setMaximum(100)
		valueSlider.setTracking(True)

		layout.addWidget(self.line_edit)
		layout.addWidget(valueSlider)

		self.setLayout(layout)

	def setParmValue(self):
		self.parm.setValueInt(int(self.line_edit.text()))


class ParameterBoolWidget(QtGui.QWidget):
	def __init__(self, parent, parm):
		QtGui.QWidget.__init__(self, parent)
		self.parm = parm

		layout = QtGui.QHBoxLayout()
		layout.setSpacing(2)
		layout.setContentsMargins(0, 0, 0, 0)

		checkbox = QtGui.QCheckBox()
		checkbox.setCheckState(self.parm.evalAsBool())
		checkbox.stateChanged.connect(self.setParmValue)

		label = QtGui.QLabel(parm.label())
		label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		label.setStatusTip(parm.name())

		layout.addWidget(checkbox)
		layout.addWidget(label)
		layout.addStretch(1)

		self.setLayout(layout)

	def setParmValue(self):
		pass

class ParameterChoiceWidget(QtGui.QWidget):
	def __init__(self, parent, parm):
		QtGui.QWidget.__init__(self, parent)
		self.parm = parm

		layout = QtGui.QHBoxLayout()
		layout.setSpacing(2)
		layout.setContentsMargins(0, 0, 0, 0)

		combobox = QtGui.QComboBox()
		for item_name in self.parm.__menu_items__:
			combobox.addItem(parm.__menu_items__[item_name])

		combobox.setCurrentIndex(parm.evalAsInt())

		layout.addWidget(combobox)
		layout.addStretch(1)

		self.setLayout(layout)

	def setParmValue(self):
		pass




