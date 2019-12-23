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
        self.ctx = self._scene_viewer.ctx
        self._visible = True
        self._xform = Matrix4()
        self._name = None

    def name(self):
        return self._name or self.__class__.title or self.__class__.__name__

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

        self.prog = self.ctx.program(
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

        self.vbo = self.ctx.buffer(SimpleGrid.buildGridData(15, 10).astype('f4').tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert')

    def render(self):
        self.ctx.enable(moderngl.DEPTH_TEST)
        self.vao.render(moderngl.LINES)

class SimpleOrigin(Drawable):
    title = "Simple Origin"

    def __init__(self, scene_viewer):
        super().__init__(scene_viewer)        

        self.prog = self.ctx.program(
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

        self.vbo = self.ctx.buffer(origin_data.astype('f4').tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

    def render(self):
        self.ctx.disable(moderngl.DEPTH_TEST)
        self.vao.render(moderngl.LINES)


class SimpleBackground(Drawable):
    title = "Simple Background"

    def __init__(self, scene_viewer):
        super().__init__(scene_viewer)        

        self.prog = self.ctx.program(
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

        self.vbo = self.ctx.buffer(origin_data.astype('f4').tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

    def render(self):
        self.mvp.write(self.proj.astype('f4').tobytes())

        self.ctx.disable(moderngl.DEPTH_TEST)
        self.vao.render(moderngl.TRIANGLE_FAN)

class OBJDataDrawable(Drawable):
    title = "OBJ Data Geometry"

    def __init__(self, scene_viewer, geometry, name=None):
        super().__init__(scene_viewer, name=name)        
        self._geometry = geometry
        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                uniform mat4 Mvp;
                in vec3 in_vert;
                //in vec3 in_color;
                out vec3 v_vert;
                out vec3 v_color;    // Goes to the fragment shader
                void main() {
                    v_vert = in_vert;
                    v_color = vec3(1.0, 1.0, 1.0);//in_color;
                    gl_Position = Mvp * vec4(in_vert, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                in vec3 v_vert;
                in vec3 v_color;
                out vec4 f_color;
                void main() {
                    vec3 Light = vec3(5.0, 5.0, 5.0);

                    float lum = 1.0;
                    //float lum = dot(normalize(v_norm), normalize(v_vert - Light));
                    //lum = acos(lum) / 3.14159265;
                    //lum = clamp(lum, 0.0, 1.0);
                    //lum = lum * lum;
                    //lum = smoothstep(0.0, 1.0, lum);
                    //lum *= smoothstep(0.0, 80.0, v_vert.z) * 0.3 + 0.7;
                    //lum = lum * 0.8 + 0.2;

                    f_color = vec4(v_vert * lum, 1.0);
                }
            ''',
        )

        self.mvp = self.prog['Mvp']

        self.build()

    def build(self):
        logger.debug("Building geometry drawable for node: %s" % self._geometry.sopNode().path())

        if self._geometry.isEmpty():
            self.vao = None
            return

        self.vbo = self.ctx.buffer(self._geometry.pointsRaw().data['P'].astype('f4').tobytes()) # geometry point positions

        indecies = []

        for prim in self._geometry.prims():
            # now we just build simple triangle fan for any type of polygon
            vertices = prim.vertices()
            root_vtx = vertices[0]

            for p_indices in [vertices[i:i+2] for i in range(1,len(vertices)-1,1)]:
                indecies.append(root_vtx.pointIndex())
                indecies.append(p_indices[0].pointIndex())
                indecies.append(p_indices[1].pointIndex())

        self.ibo = self.ctx.buffer(np.array(indecies).astype('i4').tobytes())


        vao_content = [
            # 3 floats are assigned to the 'in' variable named 'in_vert' in the shader code
            (self.vbo, '3f', 'in_vert')
        ]

        self.vao = self.ctx.vertex_array(self.prog, vao_content, self.ibo)

    def render(self):
        if self.vao:
            self.ctx.enable(moderngl.DEPTH_TEST)
            self.vao.render(moderngl.TRIANGLE_FAN)
