import os
import copy
import logging
import numpy as np

from copper.op.op_data import OP_DataBase
from copper.vmath import Vector3

from .primitive import Point, Polygon
from copper.geometry.iotranslators.base import GeoIORegistry

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
    def __init__(self, dtype, preallocate_chunk_size=100):
        self._dtype = np.dtype(dtype)
        self._size = 0 # length of used data
        self._chunk_size = preallocate_chunk_size
        self._npsize = preallocate_chunk_size # actual ndarray size
        self._data = np.empty(shape=(self._chunk_size,), dtype=self._dtype)

    def append(self, element=None):
        if self._size == self._npsize:
            # time to resize
            logger.debug("Resizing %s by %s elements." % (self.__class__.__name__, self._chunk_size))
            self._npsize += self._chunk_size
            self._data = np.resize(self._data, self._npsize)

        self._size += 1
        if element:
            self._data[self._size - 1] = element
        else:
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


class Geometry(OP_DataBase):
    def __init__(self, sop_node=None):
        super(Geometry, self).__init__()
        self._sop_node = sop_node
        self.clear()

        self._frozen = False


    def clear(self):
        self._points = DynamicArray1D({'names':['P', 'Pw'], 'formats':['3f4','f4']})
        self._prims = []

    def pointsRaw(self)  -> DynamicArray1D:
        '''
        array of data
        '''
        return self._points

    def isEmpty(self):
        if self._points.size == 0:
            return True

        return False

    def points(self) -> tuple([Point]):
        return tuple([Point(self, i) for i in range(len(self._points.data))])

    def iterPoints(self):
        for i in range(len(self._points.data)):
            yield Point(self, i)


    def prims(self):
        return self._prims

    def iterPrims(self):
        for prim in self._prims:
            yield prim


    def createPoint(self) -> Point:
        self._points.append([0,0,0])
        return Point(self, len(self._points)-1)

    def appendPoint(self, x, y, z):
        self._points.append([x, y, z])


    def sopNode(self):
        return self._sop_node


    def freeze(self):
        """
        Return another Geometry object that is not linked to a particular SOP.
        """
        if self._frozen:
            return self
        else:
            frozen_geo = Geometry()
            frozen_geo._data = copy.deepcopy(self._data)
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