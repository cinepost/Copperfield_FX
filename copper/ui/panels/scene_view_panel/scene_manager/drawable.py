import numpy as np
import moderngl
import logging

from copper.ui.context_manager import ContextManager
from copper.core.vmath import Matrix4
from pyrr import Matrix44 # using it temporarily

logger = logging.getLogger(__name__)

class Drawable():
    gl_version = (3, 3)
    title = "Drawable"

    def __init__(self, scene_viewer, **kwargs):
        self._scene_viewer = scene_viewer
        
        self.ctx = ContextManager.get_default_context()
        #self.ctx = moderngl.create_context()

        self._visible = True
        self._xform = Matrix4()
        self._name = None

        self.m_identity = Matrix44.identity()

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

    def draw(self, **kwargs):
        if self._visible:
            self.render(**kwargs)

    def render(self):
        raise NotImplementedError("")

from moderngl.buffer import Buffer

class SimpleGrid(Drawable):
    title = "Simple Grid"

    @classmethod
    def buildGridData(cls, size, cells):
        x = np.repeat(np.linspace(-size, size, cells+1), 2)
        z = np.tile([-size, size], cells+1)
        y = np.zeros((cells+1) * 2)
        return np.concatenate([np.dstack([x, y, z]), np.dstack([z, y, x])])

    def __init__(self, scene_viewer):
        super().__init__(scene_viewer)        

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                uniform mat4 model;
                uniform mat4 view;
                uniform mat4 projection;
                in vec3 in_vert;
                void main() {
                    gl_Position = projection * view * model * vec4(in_vert, 1.0);
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

        self.vbo = self.ctx.buffer(SimpleGrid.buildGridData(10, 10).astype('f4').tobytes())
        #self.vao = self.ctx.simple_vertex_array(prog, vbo, 'in_vert')

        self.model = self.prog['model']
        self.view = self.prog['view']
        self.projection = self.prog['projection']

        self.model.write(self.m_identity.astype('f4').tobytes())

    def render(self):

        #self.ctx.enable(moderngl.DEPTH_TEST)
        vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert')
        vao.render(moderngl.LINES)

class SimpleOrigin(Drawable):
    title = "Simple Origin"

    def __init__(self, scene_viewer):
        super().__init__(scene_viewer)        

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                
                uniform mat4 model;
                uniform mat4 view;
                uniform mat4 projection;

                in vec3 in_vert;
                in vec3 in_color;
                out vec3 v_color;    // Goes to the fragment shader
                void main() {
                    gl_Position = projection * view * model * vec4(in_vert, 1.0);
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

        self.model = self.prog['model']
        self.view = self.prog['view']
        self.projection = self.prog['projection']

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
        
    def render(self):
        #self.ctx.disable(moderngl.DEPTH_TEST)
        vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')
        vao.render(moderngl.LINES)


class SimpleBackground(Drawable):
    title = "Simple Background"

    def __init__(self, scene_viewer):
        super().__init__(scene_viewer)        

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                
                uniform mat4 model;
                uniform mat4 view;
                uniform mat4 projection;

                in vec3 in_vert;
                in vec3 in_color;
                out vec3 v_color;    // Goes to the fragment shader
                void main() {
                    gl_Position = projection * view * model * vec4(in_vert, 1.0);
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

        self.model = self.prog['model']
        self.view = self.prog['view']
        self.projection = self.prog['projection']

        origin_data = np.array([
            # x,y,z,r,g,b
            [-1,-1,-1], [0.39, 0.50, 0.55],
            [ 1,-1,-1], [0.39, 0.50, 0.55],
            [ 1, 1,-1], [0.75, 0.78, 0.78],
            [-1, 1,-1], [0.75, 0.78, 0.78]
        ])

        self.m_projection = Matrix44.orthogonal_projection(-1, 1, 1, -1, 1, 10)

        self.vbo = self.ctx.buffer(origin_data.astype('f4').tobytes())

        self.model.write(self.m_identity.astype('f4').tobytes())
        self.view.write(self.m_identity.astype('f4').tobytes())
        self.projection.write(self.m_projection.astype('f4').tobytes())

    def render(self):
        #self.model.write(self.m_identity.astype('f4').tobytes())
        #self.view.write(self.m_identity.astype('f4').tobytes())
        #self.projection.write(self.m_projection.astype('f4').tobytes())

        #self.ctx.disable(moderngl.DEPTH_TEST)
        vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')
        vao.render(moderngl.TRIANGLE_FAN)


import struct

class OBJDataDrawable(Drawable):
    title = "OBJ Data Geometry"

    def __init__(self, scene_viewer, obj_node, name=None):
        super().__init__(scene_viewer, name=name)        
        self._obj_node = obj_node
        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                
                uniform mat4 model;
                uniform mat4 view;
                uniform mat4 projection;
                uniform float points_mode;

                in vec3 in_vert;
                //in vec3 in_color;
                out vec3 v_vert;
                out vec3 v_color;    // Goes to the fragment shader
                out float pts_mode;

                void main() {
                    v_vert = in_vert;
                    if( points_mode < 0.5) {
                        // surfce mode
                        v_color = vec3(1.0, 1.0, 1.0);//in_color;
                    } else {
                        // points mode
                        v_color = vec3(0.0, 0.0, 1.0);
                    }
                    pts_mode = points_mode;
                    gl_Position = projection * view * model * vec4(in_vert, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                in vec3 v_vert;
                in vec3 v_color;
                in float pts_mode;

                out vec4 f_color;
                
                void main() {
                    if ( pts_mode < 0.5 ) {
                        // surfce mode
                        vec3 Light = vec3(5.0, 5.0, 5.0);

                        float lum = 1.0;
                        //float lum = dot(normalize(v_norm), normalize(v_vert - Light));
                        //lum = acos(lum) / 3.14159265;
                        //lum = clamp(lum, 0.0, 1.0);
                        //lum = lum * lum;
                        //lum = smoothstep(0.0, 1.0, lum);
                        //lum *= smoothstep(0.0, 80.0, v_vert.z) * 0.3 + 0.7;
                        //lum = lum * 0.8 + 0.2;
                        f_color = vec4(v_color * lum, 1.0);
                    } else {
                        // points mode
                        f_color = vec4(v_color, 1.0);
                    }
                }
            ''',
        )

        self.model = self.prog['model']
        self.view = self.prog['view']
        self.projection = self.prog['projection']
        self.points_mode = self.prog['points_mode']

        self.build()

    def objNode(self):
        return self._obj_node

    def renderNull(self):
        # dummy render
        pass

    def build(self):
        self.vbo = None
        self.vao_content = None
        self.points_vao = None
        self._prims_count = 0

        self.renderPoints = self.renderNull
        self.renderSurface = self.renderNull
        
        display_node = self._obj_node.displayNode()

        if not display_node:
            # Empty obj node
            logger.debug("No display node to build geometry for %s !" % self._obj_node.path())
            return 

        geometry = display_node.geometry()

        if len(geometry._prims_list) == 0:
            # No prims in geometry
            logger.warning("No prims in geometry %s !!!" % display_node.path())

        self._prims_count = len(geometry._prims_list)

        logger.debug("Building geometry drawable for node: %s" % self._obj_node.path())

        if geometry._point_attribs['P'].size > 0:
            self.vbo = self.ctx.buffer(geometry.pointsRaw()['P'].data.astype('f4').tobytes()) # geometry point positions
            self.renderPoints = self._renderPoints

        if len(geometry._prims_list) > 0:
            indecies = []

            for prim in geometry.iterPrims():
                # now we just build simple triangles for any type of polygon
                vertices = prim.vertices()
                root_vtx = vertices[0]

                for p_indices in [vertices[i:i+2] for i in range(1,len(vertices)-1,1)]:
                    indecies.append(root_vtx.pointIndex())
                    indecies.append(p_indices[0].pointIndex())
                    indecies.append(p_indices[1].pointIndex())

            self.ibo = self.ctx.buffer(np.array(indecies).astype('i4').tobytes())

            self.vao_content = [
                # 3 floats are assigned to the 'in' variable named 'in_vert' in the shader code
                (self.vbo, '3f', 'in_vert')
            ]

            self.renderSurface = self._renderSurface

            logger.debug("Done for %s" % self._obj_node.path())

    def _renderSurface(self):
        #print("surface %s with %s prims" % (self._obj_node.path(), self._prims_count))
        vao = self.ctx.vertex_array(self.prog, self.vao_content, self.ibo)
        self.points_mode.write(bytearray(struct.pack("f", 0)) )
        vao.render(moderngl.TRIANGLES)

    def _renderPoints(self):
        points_vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert')
        self.points_mode.write(bytearray(struct.pack("f", 1)) )
        points_vao.render(moderngl.POINTS)

    def render(self, show_points=True):
        self.renderSurface()

        if show_points:
            self.renderPoints()