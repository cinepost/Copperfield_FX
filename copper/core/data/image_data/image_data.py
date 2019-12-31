import logging
import numpy as np
from enum import Enum

from copper.core.data.base import OP_DataBase

logger = logging.getLogger(__name__)


class ImageDepth(Enum):
    Int8 = 1
    Int16 = 2
    Int32 = 3
    Float16 = 4
    Float32 = 5

    @classmethod
    def fromNumpy(cls, numpy_dtype):
        '''
        Returns image component depth from numpy dtype
        '''
        pass


class ImageData(OP_DataBase):
    """docstring for ImageFata"""
    def __init__(self, size, dtype = {'names':['C', 'A'], 'formats':['3f4', 'f4']}):
        super(ImageData, self).__init__()

        assert len(size)==2, "size argument must be a two integer elements"
        assert type(size[0])==type(size[1])==int, "size argument must be a two integer elements"

        self._dtype = np.dtype(dtype)
        self._size = size

        self._data = np.zeros(shape=self._size, dtype=self._dtype)

    def planes(self) -> tuple([str]):
        '''
        Returns a tuple of plane names in the image data.
        '''
        return self._dtype.names

    def components(self, plane_name):
        '''
        Returns a tuple of component names for the specified plane of image data.
        '''
        pass

    def depth(self, plane_name):
        '''
        Return the data format used to represent one component of one pixel in the given image plane.
        '''
        try:
            plane = self._data[plane_name]
        except:
            raise ValueError()
        else:
            return ImageDepth.fromNumpyDtype(plane.dtype)

    def xRes(self):
        '''
        Returns the x-resolution of image data.
        '''
        return self._size[0]

    def yRes(self):
        '''
        Returns the x-resolution of image data.
        '''
        return self._size[1]