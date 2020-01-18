import logging
import math
import moderngl
from OpenGL.GL import *
from OpenGL.arrays.vbo import VBO

import moderngl

from enum import IntEnum
from ctypes import c_float
import numpy as np

from PyQt5 import QtCore

from copper import hou
from copper.core.utils import Singleton
from copper.obj import ObjNode
from copper.core.vmath import Matrix4, Vector3
from copper import hou

from .drawable import SimpleBackground, OBJDataDrawable

logger = logging.getLogger(__name__)


class Signals(QtCore.QObject):
    geometryUpdated = QtCore.pyqtSignal()

    def __init__(self, parent=None):  
        QtCore.QObject.__init__(self, parent)


class Scene(object):
    def __init__(self, ctx, interactive_update=True):
        self.ctx = ctx
        self._interactive_update = interactive_update
        self._shapes = {}
        self._lights = {}
        self._cameras = {}

        self.signals = Signals()

    def init(self):
        self.background = SimpleBackground(self.ctx)
        for node in hou.node("/obj").children():
            self.addObject(node)

        print("Scene shapes %s" % self._shapes)

    def shapes(self):
        return self._shapes.values()

    def addObject(self, obj_node: ObjNode):
        assert isinstance(obj_node, ObjNode), "Only ObjNode instances supported!"

        obj_node_id = obj_node.id()

        if obj_node.id() not in self._shapes:
            if obj_node.displayNode():
                obj_drawable = OBJDataDrawable(self.ctx, obj_node)
                if obj_drawable:
                    self._shapes[obj_node_id] = obj_drawable
                    if self._interactive_update:
                        obj_node.signals.needsToCook.connect(lambda node=obj_node: self.updateObjNodeDrawable(node))

    @QtCore.pyqtSlot(ObjNode)
    def updateObjNodeDrawable(self, obj_node):
        if obj_node.id() in self._shapes:
            print("Update drawable in %s" % self.__class__.__name__)
            obj_node.displayNode().cook()
            self._shapes[obj_node.id()].build()
            self.signals.geometryUpdated.emit()
