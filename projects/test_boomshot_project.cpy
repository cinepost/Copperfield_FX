# Example compy (.cpy) project for boomShot clip assembling

# project preferences
prefs = {
	"engine": "GPU", # optional parameter to specify engine calculation traget. use "CPU" for low priority jobs. "GPU" is set by default
	"fps": 25.0 # set project frames_per_second to 25
}

# list all the nodes here. files and transititons in case of boomShot project 
nodes = [
	# (node_type, creation_directory, name )
	{ # this is a root level network. this node holds all our movie network
		"type": "comp",
		"name": "comp1",
		"path": "/img",	
	},
	{ # brick one
		"type": "file",
		"name": "brick1",
		"path": "/img/comp1",
		"parms": {
			"filename": "$PROJECT_ROOT/brick1/brick_$F4.jpg",
			"startframe": 0 # shift sequence start to a specific frame 0
		}
	},
	{ # brick two
		"type": "file",
		"name": "brick2",
		"path": "/img/comp1",
		"parms": {
			"filename": "$PROJECT_ROOT/brick2/brick_$F4.jpg",
			"startframe": 100 # shift sequence start to a specific frame 100
		}
	},
	{ # brick three
		"type": "file",
		"name": "brick3",
		"path": "/img/comp1",
		"parms": {
			"filename": "$PROJECT_ROOT/brick3/brick_$F4.jpg",
			"startframe": 175 # shift sequence start to a specific frame 100
		}
	},
	{ # transition 1
		"type": "blend",
		"name": "blend1",
		"path": "/img/comp1",
		"parms": {
			"factor":(
				{"t":4.0, "v":0.0}, # set "factor" to 0 at frame 100
				{"t":5.0, "v":1.0}  # set "factor" to 1 at frame 125
			)
		}
	},
	{ # transition 2
		"type": "blend",
		"name": "blend2",
		"path": "/img/comp1",
		"parms": {
			"factor":(
				{"t":7.0, "v":0.0}, # set "factor" to 0 at frame 175
				{"t":8.0, "v":1.0}  # set "factor" to 1 at frame 200
			)
		}
	}
]

# list all the links between our nodes
links = [
	# (from_node_path, to_node_path, output_index, input_index )
	# in case of boomShot output_index is always 0
	("/img/comp1/brick1", "/img/comp1/blend1", 0, 0, ), # connect brick1 to input 0 of blend1
	("/img/comp1/brick2", "/img/comp1/blend1", 0, 1, ), # connect brick2 to input 1 of blend1

	("/img/comp1/blend1", "/img/comp1/blend2", 0, 0, ), # connect blend1 to input 0 of blend2
	("/img/comp1/brick3", "/img/comp1/blend2", 0, 1, )  # connect brick3 to input 1 of blend2
]

output = {
	"node_path": "/img/comp1/blend2",
	"frame_range": (0, 250, 1), # range(first_frame, last_frame, step_size)
	"filename": "$PROJECT_ROOT/movie/movie_$F4.jpg",
	"resolution": (1280, 720) # this is optional parameter. if not supplied calculation engine will use the input files resolution e.g "brick1"
}

#  Here is some ASCII art for this netwoek :))
#
################################################
#
# /--------\       /--------\
# | brick1 |       | brick2 |
# \--------/       \--------/
#     |                 |
#     \------\  /------/
#            |  |
#         /--------\       /--------\
#         | blend1 |       | brick3 |
#         \--------/       \--------/
#              |               |
#              \-----\   /-----/
#                    |   |
#                  /--------\
#                  | blend2 |
#                  \--------/
#
#