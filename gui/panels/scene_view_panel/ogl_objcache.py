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
        
        # fill in points
        points = geometry._points
        self.n_points = len(points)
        self._points_vbo = glGenBuffers (1)
        glBindBuffer (GL_ARRAY_BUFFER, self._points_vbo)
        glBufferData (GL_ARRAY_BUFFER, self.n_points*3*4, np.array(points, dtype="float32"), GL_STATIC_DRAW) # 3*4 number of bytes in point which is 3 * float32
        glBindBuffer (GL_ARRAY_BUFFER, 0)

        # fill in polygons
        poly_indices =[]
        self._poly_count = 0
        self._poly_indices_vbo = glGenBuffers (1)
        
        if len(geometry.prims()) > 0:
            for prim in geometry.prims():
                for vtx in prim.vertices()[:3]:
                    poly_indices.append(vtx.pointIndex())
                    self._poly_count += 1

            glBindBuffer (GL_ELEMENT_ARRAY_BUFFER, self._poly_indices_vbo)
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, self._poly_count*4, np.array(poly_indices, dtype="int"), GL_STATIC_DRAW)
            glBindBuffer (GL_ELEMENT_ARRAY_BUFFER, 0)

        print "Init OGL_ObjCache done"

    def pointsVBO(self):
        return self._points_vbo


    def polyIndicesVBO(self):
        return self._poly_indices_vbo


    def polyCount(self):
        return self._poly_count

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
