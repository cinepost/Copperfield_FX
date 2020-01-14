import logging
import math
import moderngl
from OpenGL.GL import *
from OpenGL.arrays.vbo import VBO

import moderngl

from ctypes import c_float
import numpy as np

from PyQt5 import QtCore

from copper import hou
from copper.core.utils import Singleton
from copper.core.op.op_node import OP_Node
from copper.core.vmath import Matrix4, Vector3

from .drawable import SimpleGrid, SimpleOrigin, SimpleBackground
from .drawable import OBJDataDrawable

logger = logging.getLogger(__name__)


class OGL_Scene_Manager(object, metaclass=Singleton):
    def __init__(self):
        self._ctx = None
        self._initialized = None
        self._objects = {}
        self._grid = None

        logger.debug("OGL_Scene_Manager created")

    @property
    def ctx(self):
        return self._ctx or moderngl.create_context()
    
    def objects(self):
        return self._objects.values()

    def init(self):
        if not self._initialized:
            self.background = SimpleBackground(self)
            self.grid = SimpleGrid(self)
            self.origin = SimpleOrigin(self)

            for node in hou.node("/obj").children():
                self.getObjNodeDrawable(node)
            
            self._initialized = True

    def getObjNodeDrawable(self, obj_node):
        obj_node_id = obj_node.id()

        if obj_node_id in self._objects:
            return self._objects[obj_node_id]

        # there is no cached geomerty, build it
        if obj_node.displayNode():
            obj_drawable = OBJDataDrawable(self, obj_node)
            if obj_drawable:
                self._objects[obj_node_id] = obj_drawable
                obj_node.signals.needsToCook.connect(lambda node=obj_node: self.updateObjNodeDrawable(node))
                return obj_drawable

        return None

    @QtCore.pyqtSlot(OP_Node)
    def updateObjNodeDrawable(self, obj_node):
        if obj_node.id() in self._objects:
            print("Update drawable in OGL_Scene_Manager")
            obj_node.displayNode().cook()
            self._objects[obj_node.id()].build()

    def buildShaderPrograms(self):
        self.m = MGLMaterial(self.ctx, DEFAULT_VERTEX_SHADER, DEFAULT_FRAGMENT_SHADER)

scene_manager = OGL_Scene_Manager()