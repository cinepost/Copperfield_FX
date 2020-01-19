import numpy as np
import time
import sys
import logging
import tinyobjloader

from ..base import GeoBaseIO
from copper.core.data.geometry_data.primitive import Polygon
from copper.core.data.geometry_data.attribs import attribType

logger = logging.getLogger(__name__)


class ObjIO(GeoBaseIO):

    @classmethod
    def registerMIMETypes(cls):
        return [
            ['application/wobj', '.obj'],
        ]

    @staticmethod 
    def readGeometry(filename, geometry, swapyz=False):
        start_time = time.time()

        """ Loads a Wavefront OBJ file. """
        reader = tinyobjloader.ObjReader()

        # Load .obj(and .mtl) using default configuration
        ret = reader.ParseFromFile(filename)

        if ret == False:
            logger.warning(reader.Warning())
            logger.error(reader.Error())
            logger.error("Failed to load : %s" % filename)

            raise BaseException("HUY")
        else:
            if reader.Warning():
                logger.warning(reader.Warning())

        attrib = reader.GetAttrib()
        print("attrib.vertices = ", len(attrib.vertices))
        print("attrib.normals = ", len(attrib.normals))
        print("attrib.texcoords = ", len(attrib.texcoords))

        # vertex data must be `xyzxyzxyz...`
        assert len(attrib.vertices) % 3 == 0

        # normal data must be `xyzxyzxyz...`
        assert len(attrib.normals) % 3 == 0

        # texcoords data must be `uvuvuv...`
        assert len(attrib.texcoords) % 2 == 0

        # create Point's
        geometry.createPoints(np.reshape(attrib.numpy_vertices(), (-1, 3)))

        # create primitives
        shapes = reader.GetShapes()
        print("Num shapes: ", len(shapes))
        for shape in shapes:
            print(shape.name)
            #print("num_indices = {}".format(len(shape.mesh.indices)))
            #print(shape.mesh.numpy_indices())
            #print(shape.mesh.numpy_num_face_vertices())

            point_indices = shape.mesh.numpy_indices()[0::3]

            normal_indices = None
            if len(attrib.normals) > 0:
                normal_indices = shape.mesh.numpy_indices()[1::3]

            txcoord_indices = None
            if len(attrib.texcoords) > 0:
                txcoord_indices = shape.mesh.numpy_indices()[2::3]

            face_pts_offset = 0
            points = []
            for face_pts_num in shape.mesh.numpy_num_face_vertices():
                points.append(point_indices[face_pts_offset: face_pts_offset+face_pts_num])
                face_pts_offset += face_pts_num

            geometry.createPolygons(points)

        end_time = time.time()
        logger.debug("Geometry read from .obj in %s seconds" % (end_time - start_time))

    @staticmethod
    def saveGeometry(filename, geometry, swapyz=False):
        raise NotImplementedError

