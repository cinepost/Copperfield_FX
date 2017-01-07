import math
from OpenGL.GL import *
from OpenGL.arrays.vbo import VBO
from ctypes import c_float
import numpy as np

from copper.vmath import Matrix4, Vector3


class OGL_ObjCache(object):
    def __init__(self, sop_node):
        print "Init OGL_ObjCache"
        geometry = sop_node.geometry()
        points = geometry._points
        self.n_points = len(points)

        #glEnable(GL_VERTEX_ARRAY)
        self.vbo = glGenBuffers (1)
        glBindBuffer (GL_ARRAY_BUFFER, self.vbo)
        
        #glBufferData (GL_ARRAY_BUFFER, len(points)*4, (c_float*len(points))(*points), GL_STATIC_DRAW)
        glBufferData (GL_ARRAY_BUFFER, self.n_points*3*4, np.array (points, dtype="float32"), GL_STATIC_DRAW)
        print "Init OGL_ObjCache done"

class OGL_ObjCacheManager(object):
    def __init__(self):
        self._objects = {}

    def getObjNodeGeometry(self, obj_node):
        display_node = obj_node.displayNode()
        if display_node:
            display_node_path = display_node.path()
            if display_node.needsToCook() or display_node_path not in self._objects:
                # object geometry need's to be updated rebuild it
                # or no cached geomerty, build it
                obl_objcache = OGL_ObjCache(display_node)
                self._objects[display_node_path] = obl_objcache

                return obl_objcache

            return self._objects[display_node_path]

        return None
