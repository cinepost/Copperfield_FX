nodes = [
	("/comp1", "comp", ),
	("/comp1/file1", "file", ),
	("/comp1/file2", "file", ),
	("/comp1/fastblur1", "fastblur", ),
	("/comp1/fastblur2", "fastblur", )
]

links = [
	("/comp1/file1", "/comp1/fastblur1", 0, 0, ),
	("/comp1/file2", "/comp1/fastblur2", 0, 0, )
]

parms = [
	("/comp1/file1": {
		"width": 1280, 
		"height": 720, 
		"filename": "media/dog.jpg"
	}),
	("/comp1/file2": {
		"width": 0, 
		"height": 0, 
		"filename": "media/photo.exr"
	}),
	("/comp1/fastblur1": {
		"blursize":0.1, 
		"blursizey": 0.2, 
		"useindepy" : True
	}),
	("/comp1/fastblur2": {
		"blursize":0.02, 
		"blursizey": 0.2, 
		"useindepy" : False
	}),
]