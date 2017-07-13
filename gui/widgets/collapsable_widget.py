from PyQt4 import QtGui, Qt

class CollapsableWidget(QtGui.QFrame):
	def __init__(self, parent=None, direction=QtGui.QBoxLayout.LeftToRight, collapsed=False):
		QtGui.QFrame.__init__(self, parent)
		self.direction = direction
		self.collapsed = collapsed

		self.layout = QtGui.QBoxLayout(direction)
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.box_frame = QtGui.QFrame()
		self.box_frame.setObjectName("collapsable_frame")
		self.box_layout = QtGui.QBoxLayout(direction)
		self.box_layout.setSpacing(2)
		self.box_layout.setContentsMargins(2, 2, 2, 2)
		self.box_frame.setLayout(self.box_layout)

		self.button_min = QtGui.QPushButton()
		self.button_min.setMinimumWidth(10)
		self.button_min.setMinimumHeight(10)
		self.button_min.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum))
		self.button_min.setObjectName("btn_min")
		self.button_min.clicked.connect(self.switchState)

		self.layout.addWidget(self.button_min)
		self.layout.addWidget(self.box_frame)
		self.layout.setStretch(0, 0)
		self.layout.setStretch(1, 1)
		self.setLayout(self.layout)
		self.setArrow()

		self.setObjectName("collapsable")

	def addWidget(self, widget):
		self.box_layout.addWidget(widget)

	def addLayout(self, layout):
		self.box_layout.addLayout(layout)

	def addStretch(self, stretch):
		self.box_layout.addStretch(stretch)

	def setArrow(self):
		self.button_min.setIcon(QtGui.QIcon("gui/icons/main/min-right.svg"))

	def switchState(self):
		if self.collapsed:
			self.box_frame.show()
			self.collapsed = False
		else:
			self.box_frame.hide()
			self.collapsed = True

		self.setArrow()

	def collapse(self):
		if not self.collapsed:
			self.switchState()

	def uncollapse(self):
		if self.collapsed:
			self.switchState()
