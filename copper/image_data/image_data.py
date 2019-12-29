from copper.op.op_data import OP_DataBase


class ImageData(OP_DataBase):
    """docstring for ImageFata"""
    def __init__(self):
        super(ImageData, self).__init__()

    def planes(self) -> tuple([str]):
        '''
        Returns a tuple of plane names in the image data.
        '''

    def components(self, plane_name):
        '''
        Returns a tuple of component names for the specified plane of image data.
        '''

    def xRes(self):
        '''
        Returns the x-resolution of image data.
        '''

    def yRes(self):
        '''
        Returns the x-resolution of image data.
        '''