import logging
import math
from OpenGL.GL import *
from OpenGL.arrays.vbo import VBO

import moderngl

from ctypes import c_float
import numpy as np

from copper.vmath import Matrix4, Vector3

logger = logging.getLogger(__name__)


DEFAULT_VERTEX_SHADER = """
#version 330

in vec3 in_vert;

void main() {
    gl_Position = vec4(in_vert, 1.0);
}
"""

DEFAULT_FRAGMENT_SHADER = """
#version 330

uniform float ambientLightStrength;
uniform vec3  ambientLightColor; 

void main() {
    vec3 objectColor = vec3(1.0, 1.0, 1.0);
    vec3 ambient_term = ambientLightStrength * ambientLightColor;

    vec3 result = ambient_term * objectColor;
    gl_FragColor = vec4(result, 1.0);
}
"""

class MGLMaterial(object):
    def __init__(self, mgl_ctx, vertex_shader_source, fragment_shader_source):
        self._ctx = mgl_ctx
        self._vertex_shader_source = vertex_shader_source
        self._fragment_shader_source = fragment_shader_source
        self._program = None
        self._uniforms = {}

        self.__compile()
        self.__parse_uniforms()

    @property
    def program(self):
        return self._program
    

    def __compile(self):
        self._program = self._ctx.program(
            vertex_shader=self._vertex_shader_source,
            fragment_shader=self._fragment_shader_source,
        )

    def __parse_uniforms(self):
        print(self._program)
        for name in self._program:
            print(name)
            print(self._program[name])

def compile_vertex_shader(source):
    """Compile a vertex shader from source."""
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, source)
    glCompileShader(vertex_shader)
    # check compilation error
    result = glGetShaderiv(vertex_shader, GL_COMPILE_STATUS)
    if not(result):
        raise RuntimeError(glGetShaderInfoLog(vertex_shader))
    return vertex_shader

def compile_fragment_shader(source):
    """Compile a fragment shader from source."""
    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, source)
    glCompileShader(fragment_shader)
    # check compilation error
    result = glGetShaderiv(fragment_shader, GL_COMPILE_STATUS)
    if not(result):
        raise RuntimeError(glGetShaderInfoLog(fragment_shader))
    return fragment_shader

def link_shader_program(vertex_shader, fragment_shader):
    """Create a shader program with from compiled shaders."""
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    # check linking error
    result = glGetProgramiv(program, GL_LINK_STATUS)
    if not(result):
        raise RuntimeError(glGetProgramInfoLog(program))
    return program


from .drawable import OBJDataDrawable

class OGL_ObjCache(object):

    def __init__(self, ogl_manager, sop_node):
        logger.debug("Init OGL_ObjCache")
        self._ctx = ogl_manager.ctx
        self._ogl_manager = ogl_manager
        self._sop_node = sop_node

        self.buildFromSOP()
        logger.debug("Init OGL_ObjCache done")

    def buildFromSOP(self):
        geometry = self._sop_node.geometry()
        
        # fill in points
        points = geometry._points
        self._n_points = len(points)

        # generate points VBO
        self._points_vbo = self._ctx.buffer( np.array(points, dtype="float32").tobytes())
        return

        self._points_vbo = glGenBuffers (1)

        # bind points VBO in order to use
        glBindBuffer (GL_ARRAY_BUFFER, self._points_vbo)

        # upload points data
        glBufferData (GL_ARRAY_BUFFER, self._n_points*3*4, np.array(points, dtype="float32"), GL_STATIC_DRAW) # 3*4 number of bytes in point which is 3 * float32
        glBindBuffer (GL_ARRAY_BUFFER, 0)

        # fill in polygons
        poly_indices =[]
        self._poly_count = 0

        # generate indices VBO
        self._poly_indices_vbo = glGenBuffers (1)
        
        if len(geometry.prims()) > 0:
            for prim in geometry.prims():

                # now we just build simple triangle fan for any type of polygon
                vertices = prim.vertices()
                root_vtx = vertices[0]

                for indices in [vertices[i:i+2] for i in range(1,len(vertices)-1,1)]:
                    poly_indices.append(root_vtx.pointIndex())
                    poly_indices.append(indices[0].pointIndex())
                    poly_indices.append(indices[1].pointIndex())
                    self._poly_count += 1

                #for vtx in prim.vertices()[:3]:
                #    poly_indices.append(vtx.pointIndex())
                

            # bind indices data
            glBindBuffer (GL_ELEMENT_ARRAY_BUFFER, self._poly_indices_vbo)

            # upload indices data
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(poly_indices)*4, np.array(poly_indices, dtype="uint32"), GL_STATIC_DRAW)
            glBindBuffer (GL_ELEMENT_ARRAY_BUFFER, 0)


    def sopNode(self):
        return self._sop_node

    def oglManager(self):
        return self._ogl_manager

    def pointsVBO(self):
        return self._points_vbo


    def pointsCount(self):
        return self._n_points


    def polyIndicesVBO(self):
        return self._poly_indices_vbo


    def polyCount(self):
        return self._poly_count


class OGL_Scene_Manager(object):
    def __init__(self):
        self._ctx = None
        self._objects = {}
        logger.debug("OGL_Scene_Manager created")

    def setCtx(self, ctx):
        self._ctx = ctx

    @property
    def ctx(self):
        return self._ctx or moderngl.create_context()
    

    def getObjNodeGeometry(self, obj_node):
        display_node = obj_node.displayNode()
        if display_node:
            display_node_path = display_node.path()
            if display_node_path not in self._objects:
                # there is no cached geomerty, build it
                display_node.cook()
                self._objects[display_node_path] = OBJDataDrawable(self, display_node.geometry())

            elif display_node.needsToCook():
                # object geometry need's to be updated rebuild it
                display_node.cook()
                self._objects[display_node_path].build()

            return self._objects[display_node_path]

        return None

    def buildShaderPrograms(self):
        self.m = MGLMaterial(self.ctx, DEFAULT_VERTEX_SHADER, DEFAULT_FRAGMENT_SHADER)
