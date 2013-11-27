class baseCompyTranslator(object):

	def registerExtension(self):
		raise BaseException("Unimlemented baseCompyTranslator.registerExtension(self) !!! Skipping translator.")

	def translateToFile(self, source_project_file_name, dest_project_file_name):
		project_file = open( dest_project_file_name, "wb")
		project_file.write(self.translateToString(source_project_file_name))
		project_file.close()	

class compyNullTranslator(baseCompyTranslator):
	def registerExtension(self):
		return "cpy"

	def translateToString(self, source_project_file_name):
		print "Translating CPY project"
		source_project_file = open(source_project_file_name, "rb")
		project_string = source_project_file.read()
		source_project_file.close()
		return project_string


class boomShotTranslator(baseCompyTranslator):
	def registerExtension(self):
		return "bsp"	

	def translateToString(self, source_project_file_name):
		print "Translating BSP project"
		project_string = ""
		links = []

		# read and compile project  
		source_project_file = open(source_project_file_name, "rb")
		ns = eval(source_project_file.read())
		# parse project prefs
		prefs = ns.get("prefs")

		if not prefs:
			print "Warning! No preferences specified in project %s. Using defaults." % source_project_file_name
			prefs = {
				"engine": "GPU"
			}	
		else:
			# wite out prefs
			project_string += "prefs = %s\n\n" % prefs	

		# create base comp node
		nodes = [{
			"name": "movie",
			"type": "comp",
			"path": "/img"
		}]

		# parse and create bricks
		bricks = ns.get("bricks",[])
		i = 0
		for brick in bricks:
			nodes += [{
				"name": "brick_%s" % i,
				"type": "file",
				"path": "/img/movie",
				"parms": {
					"filename": brick["file_path"],
					"startframe": brick["start_frame"],
					"start": 1
				}
			}]
			i += 1

		# parse and create transitions
		last_transition_path = None
		transitions = ns.get("transitions",[])
		i = 1
		for transition in transitions:
			in_time = float(transition["frame_range"][0]) / prefs.get("fps", 25.0)
			out_time = float(transition["frame_range"][1]) / prefs.get("fps", 25.0)
			transition_name =  "%s_%s" % (transition["type"], i)
			nodes += [{
				"name": transition_name,
				"type": transition["type"],
				"path": "/img/movie",
				"parms": {
					"factor": (
						{"t": in_time, "v": 0.0},
						{"t": out_time, "v": 1.0}
					)
				}
			}]

			# create links for this transition
			links += [
				(last_transition_path or "/img/movie/brick_%s" % transition["brick_indexes"][0], "/img/movie/%s" % transition_name, 0, 0, ),
				("/img/movie/brick_%s" % transition["brick_indexes"][1], "/img/movie/%s" % transition_name, 0, 1, )
			]

			last_transition_path = "/img/movie/%s" % transition_name	

			i += 1

		# generate outputs
		output_parms = ns.get("project")

		if not output_parms:
			print "Warning! No output specified in project %s. Using defaults." % source_project_file_name
		else:	
			nodes += [{
				"name": "composite1",
				"type": "composite",
				"path": "/out",
				"parms": {
					"coppath": last_transition_path,
					"f1": 0,
					"f2": int(output_parms["frame_number"]),
					"f3": 1,
					"copoutput": output_parms["output_file_path"]
				}
			}]
		

		# write out nodes
		project_string += "nodes = %s\n\n" % nodes

		#write out links
		project_string += "links = %s\n\n" % links

		source_project_file.close()
		return project_string	
	