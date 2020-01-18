import os
import copy
import logging
import numpy as np
import cython

from copper.core.data.base import OP_DataBase
from copper.core.vmath import Vector3

from .primitive import Prim, Point, Polygon, Vertex
from copper.core.data.geometry_data.iotranslators.base import GeoIORegistry

logger = logging.getLogger(__name__)


class FrozenGeometryMedifyExcpetion(Exception):
    def __init__(self):
        Exception.__init__(self, "Cannot modify frozen geometry !") 

def check_frozen(f):
    def wrapper(*args):
        if args[0]._frozen:
            raise FrozenGeometryMedifyExcpetion()

        return f(*args)

    return wrapper

class DynamicArray1D(object):
    '''
    This class is used to reduce the nd array resize frequency by preallocating chunks.
    '''
    def __init__(self, dtype, default_value, initial_size=0, preallocate_chunk_size=100):
        self._dtype = np.dtype(dtype)
        self._default_value = default_value
        self._size = initial_size # length of used data
        self._chunk_size = max(preallocate_chunk_size, initial_size)
        self._npsize = self._chunk_size # actual ndarray size
        self._data = np.empty((self._chunk_size,), dtype=self._dtype)

    def append(self, element=None):
        if self._size == self._npsize:
            # time to resize
            self._npsize += self._chunk_size
            new_shape = [self._npsize] + list(self._data.shape[1:])
            self._data = np.resize(self._data, new_shape)

        self._size += 1
        self._data[self._size - 1] = element or self._default_value
        return self._data[self._size - 1]

    def extend(self, elements):
        assert isinstance(elements, (tuple, list, np.ndarray))
        self._data = np.concatenate((self.data, elements))
        self._size += len(elements)
        self._npsize = self._size

    def extendByNum(self, num_elements):
        assert isinstance(num_elements, int)
        arr_to_append = np.empty((num_elements,), dtype=self._dtype)

        if self._default_value:
            arr_to_append.fill(self._default_value)
        
        self._data = np.concatenate((self.data, arr_to_append))
        self._size += num_elements
        self._npsize = self._size

    def __len__(self):
        return self._size

    def __str__(self):
        return "%s\n%s" % (self.__class__.__name__, self.data)

    def __getitem__(self, key):
        return self._data[:self._size][key]

    def __setitem__(self, key, value):
        self._data[:self._size][key] = value

    @property
    def data(self):
        return self._data[:self._size]

    @property
    def size(self):
        return self._size

    @property
    def dtype(self):
        return self._dtype


from .attribs import attribType, Attrib

class GeometryData(OP_DataBase):
    def __init__(self, sop_node=None):
        super(GeometryData, self).__init__()
        self._sop_node = sop_node
        self.clear()

        self._frozen = False

    def clear(self):        
        self._pts_index_map = {}
        self._vts_index_map = {}
        self._prims_index_map = {}
        
        self._points_list = []#DynamicArray1D(Point, None) #[]
        self._vertices_list = []#DynamicArray1D(Vertex, None) #[]
        self._prims_list = []#DynamicArray1D(Prim, None) #[]

        self._attribs = [{}, {}, {}, {}]
        self._attribs[attribType.Point] = {
            Attrib(self, attribType.Point, 'P', (0.0, 0.0, 0.0)): DynamicArray1D("3f4", (0.0, 0.0, 0.0)),
            Attrib(self, attribType.Point, 'Pw', 1.0): DynamicArray1D('f4', 1.0),        
        }

        self._attribs[attribType.Prim] = {}
        self._attribs[attribType.Vertex] = {}
        self._attribs[attribType.Global] = {}

        # shortcuts
        self._point_attribs = self._attribs[attribType.Point]
        self._vertex_attribs = self._attribs[attribType.Vertex]
        self._prim_attribs = self._attribs[attribType.Prim]

    def pointsRaw(self)  -> DynamicArray1D:
        '''
        array of data
        '''
        return self._attribs[attribType.Point]

    def isEmpty(self):
        if self._attribs[attribType.Point]['P'].size == 0:
            return True

        return False

    def points(self) -> tuple([Point]):
        return tuple(self._points_list)

    def iterPoints(self):
        for pt in self._points_list:
            yield pt

    def prims(self) -> tuple([Prim]):
        return tuple(self._prims_list)

    def iterPrims(self):
        for prim in self._prims_list:
            yield prim

    def createPoint(self) -> Point:
        """
        Create a new point located at (0, 0, 0) and return the corresponding Point object.
        """

        for attrib in self._attribs[attribType.Point].values():
            attrib.append()

        pt = Point(self, len(self._points_list))
        self._points_list.append(pt)
        
        return pt

    def createVertex(self, prim, point) -> Vertex:

        for attrib in self._attribs[attribType.Vertex].values():
            attrib.append()

        self._vertices_list.append(Vertex(prim, point._pt_index, len(self._vertices_list)))
        return self._vertices_list[-1]

    def createVerticesBulk(self, prim, points_or_indices) -> tuple([Vertex]):
        '''
        create vertices without attributes modification
        '''
        assert isinstance(points_or_indices, (tuple, list, np.ndarray))
        assert isinstance(points_or_indices[0], (int, np.int32, Point))

        new_vertices = [Vertex(prim, pt_index, vt_index) for vt_index, pt_index in enumerate(points_or_indices, len(self._vertices_list))]

        self._vertices_list += new_vertices
        return tuple(new_vertices)

    def createVertices(self, prim, points_or_indices) -> tuple([Vertex]):
        assert isinstance(points_or_indices, (tuple, list, np.ndarray))
        assert isinstance(points_or_indices[0], (int, np.int32, Point))

        for attrib in self._attribs[attribType.Vertex].values():
            attrib.extendByNum(len(points_or_indices))

        return self.createVerticesBulk(prim, points_or_indices)

    def createPoints(self, point_positions: tuple or list or np.ndarray) -> tuple([Point]):
        self._point_attribs['P'].extend(point_positions)
        old_points_num = len(self._points_list)

        new_points_list = [Point(self, idx) for idx in range(old_points_num, len(point_positions))]
        self._points_list.extend(new_points_list)

        return tuple(new_points_list)

    def appendPoint(self, x, y, z):
        self._points.append([x, y, z])

    def createPolygon(self, is_closed=True):
        '''
        Create a new polygon and return the corresponding Polygon object.
        '''
        self._prims_list.append(Polygon(self, len(self._prims_list)))

        return self._prims_list[-1]

    def createPolygons(self, points: tuple or list or np.ndarray, is_closed=True) -> tuple([Polygon]):
        assert isinstance(points, (tuple, list, np.ndarray)), "points should be either tuple/list/ndarray of tuples/lists/ndarray"
        assert isinstance(points[0], (tuple, list, np.ndarray)), "points should be either tuple/list/ndarray of tuples/lists/ndarray"

        total_vtx_count = sum([len(sublist) for sublist in points])
        for attrib in self._attribs[attribType.Vertex].values():
            attrib.extendByNum(total_vtx_count)

        if type(points[0][0]) in (int, np.int32):
            # create polygons using point numbers(indices)
            for pts in points:
                prim = Polygon(self, len(self._prims_list))
                prim._vertices = self.createVerticesBulk(prim, pts)
                self._prims_list.append(prim)

        elif type(points[0][0]) == Point:
            # create polygons using Point objects 
            for pts in points:
                pass

        else:
            raise BaseException("Unknown %s passed as point" % type(points[0][0]))

    def addAttrib(self, attrib_type: attribType, name: str, default_value, transform_as_normal=False, create_local_variable=True) -> Attrib:
        if name not in self._attribs[attrib_type]:
            # attribute not present, create it first
            attrib = Attrib(self, attrib_type, name, default_value)

            initial_size = 1
            if attrib_type == attribType.Point:
                initial_size = len(self._points_list)
            elif attrib_type == attribType.Vertex:
                initial_size = len(self._vertices_list)
            elif attrib_type == attribType.Prim:
                initial_size = len(self._prim_list)

            value_size = 1
            value_type = "f4"
            if isinstance(default_value, (tuple, list, np.ndarray)):
                value_size = len(default_value)

            data_type = "%s%s" % (value_size, value_type)

            self._attribs[attrib_type][attrib] = DynamicArray1D(data_type, default_value, initial_size = initial_size)

        else:
            atrtib = self._attribs[attrib_type][name]

        return attrib
        
    def pointAttribs(self) -> tuple([Attrib]):
        """
        Return a tuple of all the point attributes.
        """
        return tuple(sefl._attribs[attribType.Point])

    def vertexAttribs(self) -> tuple([Attrib]):
        """
        Return a tuple of all the vertex attributes.
        """
        return tuple(sefl._attribs[attribType.Vertex])

    def findVertexAttrib(self, name) -> Attrib or None:
        return self._vertex_attribs.get(name)

    def findPointAttrib(self, name) -> Attrib or None:
        if name in self._point_attribs:
            return self._point_attribs[name]

        return None

    def sopNode(self):
        return self._sop_node


    def freeze(self):
        """
        Return another Geometry object that is not linked to a particular SOP.
        """
        if self._frozen:
            return self
        else:
            frozen_geo = GeometryData()
            frozen_geo._attribs = copy.deepcopy(self._attribs)
            frozen_geo._prims = copy.deepcopy(self._prims)
            frozen_geo._frozen = True
            return frozen_geo

    @check_frozen
    def loadFromFile(self, file_name):
        name, extension = os.path.splitext(file_name)
        self.clear()
        GeoIORegistry.getIOTranslatorByExt(extension).readGeometry(file_name, self)


    def saveToFile(self, file_name):
        name, extension = os.path.splitext(file_name)
        GeoIORegistry.getIOTranslatorByExt(extension).saveGeometry(file_name, self)