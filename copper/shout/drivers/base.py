import os, struct, time

class BaseDisplayDriver(object):
    def __init__(self, xres, yres, nchannels=4, datasize=1, name="Test Application"):
        self._xres = xres
        self._yres = yres
        self._nchannels = nchannels
        self._datasize = datasize
        self._name = name

        self.open()

    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def writeTile(self, x, y, width, height, data):
        raise NotImplementedError
