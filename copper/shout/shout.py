#!/usr/bin/env python

import sys
import timeit
import argparse
import logging
from parsers.base import ParsersRegistry
from renderers import Renderer

import pyximport
pyximport.install()


logger = logging.getLogger(__name__)

description = """
Reads an geometry scene from standard input and renders the image described.

If the first argument after options ends in .ifd, .ifd.gz, .ifd.bz2,
.rib or any other supported scene file format, shout will read the 
scene description from that file.  If the argument does not have an 
supported scene extension it will be used as the output image/device
"""

if __name__ == "__main__":
	start = timeit.default_timer()

	parser = argparse.ArgumentParser(prog='shout', usage="%(prog)s [options] [ifd] [outputimage]", description=description)
	
	# rendering options 
	group_rend_opts = parser.add_argument_group('Rendering Options')
	group_rend_opts.add_argument('-r', action='store', dest='simple_value', help='Store a simple value')

	# image options 
	group_img_opts = parser.add_argument_group('Image Options')
	group_img_opts.add_argument('-i', action='store', dest='interactive', type=bool, help='Render interactively')

	# control options 
	group_ctrl_opts = parser.add_argument_group('Control Options')
	group_ctrl_opts.add_argument('-t', dest="type", metavar="type", type=str, default="", help="Scene file format to use when listening to stdin")
	group_ctrl_opts.add_argument('-f', dest="file", metavar="file", type=argparse.FileType('r'), nargs='?', help="Read scene file specified instead of reading from stdin")
	group_ctrl_opts.add_argument('-V', metavar='val', type=int, default=0, help="Set verbose level 1-5")

	parser.add_argument('ifd', nargs='?', default=None, help=argparse.SUPPRESS)
	parser.add_argument('outputimage', nargs='?', default=None, help=argparse.SUPPRESS)

	args, unknown = parser.parse_known_args()
	logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

	scene_ext = None
	scene_filename = None
	output_image_filename = None

	if args.file: 
		# if -f option provided we use it as it is
		scene_filename = args.file.name
	elif args.ifd:
		# if no -f option provided we should analyze last positional arguments
		scene_filename = args.ifd

	# guess file fromat from extnesion
	if scene_filename:
		if any(map(scene_filename.__contains__, ['gz', 'bz2'])):
			scene_ext = scene_filename.rsplit(".",1)[0].rsplit(".",1)[-1]
		else:
			scene_ext = scene_filename.rsplit(".",1)[-1]


	logger.debug("scene_ext %s" % scene_ext)
	logger.debug("scene_filename: %s" % scene_filename)
	logger.debug("output_image_filename %s" % output_image_filename)

	import cProfile
	 
	#pr = cProfile.Profile()
	#pr.enable()

	renderer = Renderer()

	scene_parser = ParsersRegistry.getParserByExt(args.type or scene_ext or 'ifd')
	scene_parser.parseFile(scene_filename, echo=(args.V > 0))

	#from drivers import MPlay
	#output_driver = MPlay(800, 600, nchannels=4, datasize=1, name="Test Application")
	#output_driver.open()
	#output_driver.close()

	#pr.disable()
	#pr.print_stats(sort='cumtime')

	stop = timeit.default_timer()
	logger.info("Scene read in : %s secs." % (stop - start))
	print("Scene read in : %s secs." % (stop - start))
