import numpy as np
import moderngl
import logging

from copper.vmath import Matrix4
from pyrr import Matrix44 # using it temporarily

logger = logging.getLogger(__name__)


class Drawable():
    gl_version = (3, 3)
    title = "Drawable"

    def __init__(self, scene_viewer, **kwargs):
        self._scene_viewer = scene_viewer
        self._ctx = self._scene_viewer.ctx
        self._visible = True
        self._xform = Matrix4()
        self._name = None

    def name(self):
        return self._name or self.__cls__.title or self.__cls__.__name__

    def show(self, value = True):
        self._visible = value

    def toggleVisibility(self):
        self._visible = not self._visible

    def visible(self):
        return self._visible

    def transform(self):
        return self._xform

    def setTransform(self, xform):
        self._xform = xform

    def draw(self):
        if self._visible:
            self.render()

    def render(self):
        raise NotImplementedError("")

class SimpleGrid(Drawable):
    title = "Simple Grid"

    @classmethod
    def buildGridData(cls, size, steps):
        x = np.repeat(np.linspace(-size, size, steps), 2)
        z = np.tile([-size, size], steps)
        y = np.zeros(steps * 2)
        return np.concatenate([np.dstack([x, y, z]), np.dstack([z, y, x])])

    def __init__(self, scene_viewer):
        super().__init__(scene_viewer)        

        self.prog = self._ctx.program(
            vertex_shader='''
                #version 330
                uniform mat4 Mvp;
                in vec3 in_vert;
                void main() {
                    gl_Position = Mvp * vec4(in_vert, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                out vec4 f_color;
                void main() {
                    f_color = vec4(0.1, 0.1, 0.1, 1.0);
                }
            ''',
        )

        self.mvp = self.prog['Mvp']

        self.vbo = self._ctx.buffer(SimpleGrid.buildGridData(15, 10).astype('f4').tobytes())
        self.vao = self._ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert')

    def render(self):
        self._ctx.enable(moderngl.DEPTH_TEST)
        self.vao.render(moderngl.LINES)

class SimpleOrigin(Drawable):
    title = "Simple Origin"

    def __init__(self, scene_viewer):
        super().__init__(scene_viewer)        

        self.prog = self._ctx.program(
            vertex_shader='''
                #version 330
                uniform mat4 Mvp;
                in vec3 in_vert;
                in vec3 in_color;
                out vec3 v_color;    // Goes to the fragment shader
                void main() {
                    gl_Position = Mvp * vec4(in_vert, 1.0);
                    v_color = in_color;
                }
            ''',
            fragment_shader='''
                #version 330
                in vec3 v_color;
                out vec4 f_color;
                void main() {
                    f_color = vec4(v_color, 1.0);
                }
            ''',
        )

        self.mvp = self.prog['Mvp']

        origin_data = np.array([
            # x,y,z,r,g,b
            [0,0,0],[1,0,0],
            [1,0,0],[1,0,0],
            [0,0,0],[0,1,0],
            [0,1,0],[0,1,0],
            [0,0,0],[0,0,1],
            [0,0,1],[0,0,1],
        ])

        self.vbo = self._ctx.buffer(origin_data.astype('f4').tobytes())
        self.vao = self._ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

    def render(self):
        self._ctx.disable(moderngl.DEPTH_TEST)
        self.vao.render(moderngl.LINES)


class SimpleBackground(Drawable):
    title = "Simple Background"

    def __init__(self, scene_viewer):
        super().__init__(scene_viewer)        

        self.prog = self._ctx.program(
            vertex_shader='''
                #version 330
                uniform mat4 Mvp;
                in vec3 in_vert;
                in vec3 in_color;
                out vec3 v_color;    // Goes to the fragment shader
                void main() {
                    gl_Position = Mvp * vec4(in_vert, 1.0);
                    v_color = in_color;
                }
            ''',
            fragment_shader='''
                #version 330
                in vec3 v_color;
                out vec4 f_color;
                void main() {
                    f_color = vec4(v_color, 1.0);
                }
            ''',
        )

        self.mvp = self.prog['Mvp']

        origin_data = np.array([
            # x,y,z,r,g,b
            [-1,-1,-1], [0.39, 0.50, 0.55],
            [ 1,-1,-1], [0.39, 0.50, 0.55],
            [ 1, 1,-1], [0.75, 0.78, 0.78],
            [-1, 1,-1], [0.75, 0.78, 0.78]
        ])

        self.proj = Matrix44.orthogonal_projection(-1, 1, 1, -1, 1, 10)

        self.vbo = self._ctx.buffer(origin_data.astype('f4').tobytes())
        self.vao = self._ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

    def render(self):
        self.mvp.write(self.proj.astype('f4').tobytes())

        self._ctx.disable(moderngl.DEPTH_TEST)
        self.vao.render(moderngl.TRIANGLE_FAN)

class OBJDataDrawable(Drawable):
    title = "OBJ Data Geometry"

    def __init__(self, scene_viewer, name=None):
        super().__init__(scene_viewer, name=name)        

        self.prog = self._ctx.program(
            vertex_shader='''
                #version 330
                uniform mat4 Mvp;
                in vec3 in_vert;
                in vec3 in_color;
                out vec3 v_color;    // Goes to the fragment shader
                void main() {
                    gl_Position = Mvp * vec4(in_vert, 1.0);
                    v_color = in_color;
                }
            ''',
            fragment_shader='''
                #version 330
                in vec3 v_color;
                out vec4 f_color;
                void main() {
                    f_color = vec4(v_color, 1.0);
                }
            ''',
        )

        self.mvp = self.prog['Mvp']

        origin_data = np.array([
            # x,y,z,r,g,b
            [-1,-1,-1], [0.39, 0.50, 0.55],
            [ 1,-1,-1], [0.39, 0.50, 0.55],
            [ 1, 1,-1], [0.75, 0.78, 0.78],
            [-1, 1,-1], [0.75, 0.78, 0.78]
        ])

        self.proj = Matrix44.orthogonal_projection(-1, 1, 1, -1, 1, 10)

        self.vbo = self._ctx.buffer(origin_data.astype('f4').tobytes())
        self.vao = self._ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

    def render(self):
        self.mvp.write(self.proj.astype('f4').tobytes())

        self._ctx.disable(moderngl.DEPTH_TEST)
        self.vao.render(moderngl.TRIANGLE_FAN)
