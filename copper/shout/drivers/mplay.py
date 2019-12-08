#!/usr/bin/env python
#
#  This program shows how to write data to mplay by writing data to the
#  imdisplay program using a pipe.
#
#  This program uses the -k option on imdisplay to perform progressive
#  refinement when rendering an image.  The image is quite simple.
#
#  Notes:
#       This uses the simple format (no deep rasters)
#       It only writes 8-bit data
# 

import os, struct, time
import subprocess
from .base import BaseDisplayDriver


MAGIC = (ord('h')<<24) + (ord('M')<<16) + (ord('P')<<8) + ord('0')
DATASIZE = 1    # See .c file for meaning
NCHANNELS = 4   # See .c file for meaning
EO_IMAGE = -2   # End of image marker
RES = 256

COLORS = [
    (0, 0, 0, 255),
    (255, 0, 0, 255),
    (0, 255, 0, 255),
    (0, 0, 255, 255),
    (255, 255, 0, 255),
    (0, 255, 255, 255),
    (255, 0, 255, 255),
    (255, 255, 255, 255),
]


class MPlay(BaseDisplayDriver):
    def open(self):
        # Open a pipe to imdisplay
        #   -p tells imdisplay to read the data from the pipe
        #   -k tells imdisplay to keep reading data after the image has
        #      been fully written
        #self.fp = os.popen('imdisplay -p -k -n "%s"' % self._name, mode='w')
        self.fp = subprocess.Popen(['imdisplay -p -k -n "%s"' % self._name], stdin=subprocess.PIPE)
        # The header is documented in the C code examples
        header = struct.pack('I'*8, MAGIC, self._xres, self._yres, self._datasize, self._nchannels, 0, 0, 0)
        #self.fp.write(header)
        proc.communicate(header)

    def close(self):
        # To tell imdisplay that the image has been finished, we send a special
        # header.
        header = struct.pack('iiii', EO_IMAGE, 0, 0, 0)
        self.fp.write(header)
        self.fp.close()
        self.fp = None

    def writeTile(self, x, y, width, height, data):
        # The tile header is documented in the c code.
        header = struct.pack('IIII', x0, x1, y0, y1)
        self.fp.write(header)

        # The tile's bounds are inclusive, so to find the number of pixels we
        # need to add one to each dimension.
        size = (x1 - x0 + 1) * (y1 - y0 + 1)
        pixel = struct.pack('BBBB', clr[0], clr[1], clr[2], clr[3])
        # Write a bunch of pixel data
        self.fp.write(pixel * size)
