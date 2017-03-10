import math
from OpenGL.GL import *
from OpenGL.arrays.vbo import VBO
from ctypes import c_float
import numpy as np

from copper.vmath import Matrix4, Vector3


DEFAULT_VERTEX_SHADER = """
void main()
{
    gl_Position = ftransform();
}
"""

DEFAULT_FRAGMENT_SHADER = """
void main()
{
    gl_FragColor = vec4(0.4,0.4,0.8,1.0);
}
"""

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


class OGL_ObjCache(object):

    def __init__(self, ogl_manager, sop_node):
        print "Init OGL_ObjCache"
        self._ogl_manager = ogl_manager
        self._sop_node = sop_node

        self.buildFromSOP()
        print "Init OGL_ObjCache done"

    def buildFromSOP(self):
        geometry = self._sop_node.geometry()
        
        # fill in points
        points = geometry._points
        self._n_points = len(points)

        # generate points VBO
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

                for indices in [vertices[i:i+2] for i in xrange(1,len(vertices)-1,1)]:
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
        self._objects = {}
        self._shader_programs = {}
        self._default_shader_program = None
        print "OGL_Scene_Manager created"

    def getObjNodeGeometry(self, obj_node):
        display_node = obj_node.displayNode()
        if display_node:
            display_node_path = display_node.path()

            if display_node_path not in self._objects:
                # there is no cached geomerty, build it
                self._objects[display_node_path] = OGL_ObjCache(self, display_node)

            elif display_node.needsToCook():
                # object geometry need's to be updated rebuild it
                self._objects[display_node_path].buildFromSOP()

            return self._objects[display_node_path]

        return None

    def buildShaderPrograms(self):
        if not self._default_shader_program:
            # create default shader programs
            default_vertex_shader = compile_vertex_shader(DEFAULT_VERTEX_SHADER)
            default_fragment_shader = compile_fragment_shader(DEFAULT_FRAGMENT_SHADER)
            self._default_shader_program = link_shader_program(default_vertex_shader, default_fragment_shader)

    def defaultShaderProgram(self):
        return self._default_shader_program

    def shaderPrograms(self):
        return self._shader_programs
