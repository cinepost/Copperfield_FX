import os
import copy
import logging
import numpy as np

from copper.core.data.base import OP_DataBase
from copper.core.vmath import Vector3

from .primitive import Point, Polygon
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
    def __init__(self, dtype, default_value, preallocate_chunk_size=100):
        self._dtype = np.dtype(dtype)
        self._default_value = default_value
        self._size = 0 # length of used data
        self._chunk_size = preallocate_chunk_size
        self._npsize = preallocate_chunk_size # actual ndarray size
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
        for element in elements:
            self.append(element)

    def __len__(self):
        return self._size

    @property
    def data(self):
        return self._data[:self._size]

    @property
    def size(self):
        return self._size

    @property
    def dtype(self):
        return self._dtype

#dt = np.dtype({ 'names'     : ['r','g','b','a'],
#                'formats'   : [uint8, uint8, uint8, uint8]})

from .attribs import attribType, Attrib

class GeometryData(OP_DataBase):
    def __init__(self, sop_node=None):
        super(GeometryData, self).__init__()
        self._sop_node = sop_node
        self.clear()

        self._frozen = False


    def clear(self):
        #self._points = DynamicArray1D({'names':['P', 'Pw'], 'formats':['3f4','f4']})
        self._prims = []
        self._attribs = [{}, {}, {}, {}]
        self._attribs[attribType.Point] = {
            'P': DynamicArray1D("3f4", (0.0, 0.0, 0.0)),
            'Pw': DynamicArray1D('f4', 1.0),        
        }

        self._attribs[attribType.Prim] = {}
        self._attribs[attribType.Vertex] = {}
        self._attribs[attribType.Global] = {}

        # shortcuts
        self._point_attribs = self._attribs[attribType.Point]

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
        return tuple([Point(self, i) for i in range(len(self._attribs[attribType.Point]['P'].data))])

    def iterPoints(self):
        for i in range(len(self._attribs[attribType.Point]['P'].data)):
            yield Point(self, i)


    def prims(self):
        return self._prims

    def iterPrims(self):
        for prim in self._prims:
            yield prim


    def createPoint(self) -> Point:
        """
        Create a new point located at (0, 0, 0) and return the corresponding hou.Point object.
        """

        for attrib in self._attribs[attribType.Point].values():
            attrib.append()
        
        return Point(self, len(self._attribs[attribType.Point]['P'])-1)

    def createPoints(self, point_positions) -> tuple([Point]):
        pass

    def appendPoint(self, x, y, z):
        self._points.append([x, y, z])

    def addAttrib(self, attrib_type: attribType, name: str, default_value, transform_as_normal=False, create_local_variable=True) -> Attrib:
        if name not in self._attribs[attrib_type]:
            # attribute not present, create it first
            self._attribs[attrib_type][name] = Attrib(self, 
                attrib_type=attrib_type,
                name=name,
                default_value=default_value,
                data_type=data_type,
                data_size=data_size)
        
        return self._attribs[attrib_type][name]
        
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