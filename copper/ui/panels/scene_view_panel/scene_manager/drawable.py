import numpy as np
import moderngl
import logging

from copper.ui.context_manager import ContextManager
from copper.core.vmath import Matrix4, normalize_v3
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


class QuadFS(Drawable):
    def __init__(self, scene_viewer):
        super().__init__(scene_viewer)
        """
        Creates a 2D quad VAO using 2 triangles with normals and texture coordinates.
        """
        width, height = (1.0, 1.0)
        xpos, ypos = (0.0, 0.0)

        self.program = self.ctx.program(
            vertex_shader='''
                #version 330
                
                in vec3 in_position;
                in vec2 in_texcoord_0;

                uniform mat4 m_proj;
                uniform mat4 m_model;
                uniform mat4 m_view;

                out vec2 uv;

                void main() {
                    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
                    uv = in_texcoord_0;
                }
            ''',
            fragment_shader='''
                #version 330
                
                uniform sampler2D texture0;

                out vec4 fragColor;
                
                in vec2 uv;

                void main() {
                    vec4 color = texture(texture0, uv);
                    fragColor = color;
                }
            ''',
        )

        pos_data = np.array([
            xpos - width / 1.0, ypos + height / 1.0, -1.0,
            xpos - width / 1.0, ypos - height / 1.0, -1.0,
            xpos + width / 1.0, ypos - height / 1.0, -1.0,
            xpos + width / 1.0, ypos + height / 1.0, -1.0,
        ], dtype=np.float32)

        normal_data = np.array([
            0.0, 0.0, 1.0,
            0.0, 0.0, 1.0,
            0.0, 0.0, 1.0,
            0.0, 0.0, 1.0,
        ], dtype=np.float32)

        uv_data = np.array([
            0.0, 0.0,
            0.0, 1.0,
            1.0, 1.0,
            1.0, 0.0,
        ], dtype=np.float32)

        self.ibo = self.ctx.buffer(np.array([0,1,2,0,2,3]).astype('i4').tobytes())

        self.vbo1 = self.ctx.buffer(pos_data.astype('f4').tobytes())
        #self.vbo2 = self.ctx.buffer(normal_data.astype('f4').tobytes())
        self.vbo3 = self.ctx.buffer(uv_data.astype('f4').tobytes())


        self.vao_content = [
            (self.vbo1, "3f", "in_position"),
            #(self.vbo2, "3f", "in_normal"),
            (self.vbo3, "2f", "in_texcoord_0")
        ]

    def render(self):
        vao = self.ctx.vertex_array(self.program, self.vao_content, index_buffer=self.ibo)
        vao.render(moderngl.TRIANGLES)
        vao.release()

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

        self.model = self.prog['model']
        self.view = self.prog['view']
        self.projection = self.prog['projection']

        self.model.write(self.m_identity.astype('f4').tobytes())

    def render(self):

        #self.ctx.enable(moderngl.DEPTH_TEST)
        vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert')
        vao.render(moderngl.LINES)
        vao.release()


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
        vao.release()

from .shaders import SURFACE, POINTS

class OBJDataDrawable(Drawable):
    title = "OBJ Data Geometry"

    def __init__(self, scene_viewer, obj_node, name=None):
        super().__init__(scene_viewer, name=name)        
        self._obj_node = obj_node

        self.surface_prog = self.ctx.program( vertex_shader = SURFACE.VS, fragment_shader = SURFACE.FS )
        self.points_prog = self.ctx.program( vertex_shader = POINTS.VS, fragment_shader = POINTS.FS )

        self.programs = (self.surface_prog, self.points_prog)

        self.build()

    def objNode(self):
        return self._obj_node

    def renderNull(self):
        # dummy render
        pass

    def uniformWrite(self, unifrom_name, unifrom_value):
        for prog in self.programs:
            prog[unifrom_name].write(unifrom_value)

    def build(self):
        self.points_vbo = None
        self.surface_vbo_v = None
        self.surface_vbo_n = None
        self.surface_vao_content = None

        self._prims_count = 0

        self.renderPoints = self.renderNull
        self.renderSurface = self.renderNull
        self.renderNormals = self.renderNull
        
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

        # Points
        if len(geometry._point_attribs['P']) > 0:
            self.points_vbo = self.ctx.buffer(geometry.pointsRaw()['P'].data.astype('f4').tobytes()) # geometry point positions
            self.renderPoints = self._renderPoints

        # Vertex/Points/Prims Normals
        if geometry.findVertexAttrib('N'):
            pass

        # Surface
        if len(geometry._prims_list) > 0:
            positions = []
            indices = []
            start_index = 0

            # vetrices
            for prim in geometry.iterPrims():
                # now we just build simple triangles for any type of polygon
                start_index = len(positions)
                prim_vertices = prim.vertices()
                
                positions += [v.point().positionData() for v in prim_vertices]
                indices += [[start_index, start_index+x,start_index+x+1] for x in range(1, len(prim_vertices),2)]


            vertices = np.array(positions).astype('f4')
            faces = np.array(indices).astype('i4')
            # normals
            normals = np.zeros((len(vertices),3), dtype="f4" )

            # create an indexed view into the vertex array using the array of three indices for triangles
            tris = vertices[faces]

            #Calculate the normal for all the triangles, by taking the cross product of the vectors v1-v0, and v2-v0 in each triangle             
            n = np.cross( tris[::,1 ] - tris[::,0]  , tris[::,2 ] - tris[::,0] )
            # n is now an array of normals per triangle. The length of each normal is dependent the vertices, 
            # we need to normalize these, so that our next step weights each normal equally.
            normalize_v3(n)
            # now we have a normalized array of normals, one per triangle, i.e., per triangle normals.
            # But instead of one per triangle (i.e., flat shading), we add to each vertex in that triangle, 
            # the triangles' normal. Multiple triangles would then contribute to every vertex, so we need to normalize again afterwards.
            # The cool part, we can actually add the normals through an indexed view of our (zeroed) per vertex normal array
            normals[ faces[:,0] ] += n
            normals[ faces[:,1] ] += n
            normals[ faces[:,2] ] += n
            normalize_v3(normals)

            self.surface_vbo_v = self.ctx.buffer(vertices.tobytes()) # geometry vertices
            self.surface_vbo_n = self.ctx.buffer(normals.tobytes()) # geometry normals
            self.surface_ibo = self.ctx.buffer(faces.tobytes())

            self.surface_vao_content = [
                # 3 floats are assigned to the 'in' variable named 'in_vert' in the shader code
                (self.surface_vbo_v, '3f', 'in_vert'),
                (self.surface_vbo_n, '3f', 'in_norm')
            ]

            self.renderSurface = self._renderSurface

            logger.debug("Done for %s" % self._obj_node.path())

    def _renderNormals(self):
        vao = self.ctx.vertex_array(self.normals_prog, self.normals_vao_content, self.normals_ibo)
        vao.render(moderngl.LINES)
        vao.release()

    def _renderSurface(self):
        #print("surface %s with %s prims" % (self._obj_node.path(), self._prims_count))
        vao = self.ctx.vertex_array(self.surface_prog, self.surface_vao_content, self.surface_ibo)
        vao.render(moderngl.TRIANGLES)
        vao.release()

    def _renderPoints(self):
        vao = self.ctx.simple_vertex_array(self.points_prog, self.points_vbo, 'in_vert')
        vao.render(moderngl.POINTS)
        vao.release()

    def render(self, show_points=True):
        self.renderSurface()
        self.renderNormals()

        if show_points:
            self.renderPoints()