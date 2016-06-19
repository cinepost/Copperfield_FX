#!/usr/bin/python
import argparse

def main():
	parser = argparse.ArgumentParser(description='This is a demo script by nixCraft.')
	parser.add_argument('-p', '--project', help='Input project file name', required=False)
	parser.add_argument('-o', '--output', help='Output node path', required=False)
	parser.add_argument('-r', '--render', help='Render', action='store_true', required=False)
	parser.add_argument('-f', '--frange', help='Frame range', nargs=3, required=False)
	parser.add_argument('-e', '--engine', help='Engine: GPU or CPU', required=False)
	parser.add_argument('-l', '--list', help='List OpenCL devices', action='store_true', required=False)
	parser.add_argument('-d', '--device', help='Device index to use. example: -g GPU -d 0', required=False)
	parser.add_argument('-c', '--convert', help='Convert projects. example -c new_project.cpy', required=False)
	

	args = parser.parse_args()

	if args.list:
		import pyopencl as cl
		for platform in cl.get_platforms():
			print("===============================================================")
			print("Platform name:", platform.name)
			print("Platform profile:", platform.profile)
			print("Platform vendor:", platform.vendor)
			print("Platform version:", platform.version)
			for device in platform.get_devices():
				print("---------------------------------------------------------------")
				print("Device name:", device.name)
				print("Device type:", cl.device_type.to_string(device.type))
				print("Device memory: ", device.global_mem_size//1024//1024, 'MB')
				print("Device max clock speed:", device.max_clock_frequency, 'MHz')
				print("Device compute units:", device.max_compute_units)

		exit(True)
				
	import copper
	eng = "GPU"
	dev = None
	if args.engine: eng = args.engine
	if args.device: dev = int(args.device)
	engine = copper.CreateEngine(device_type = eng, device_index = dev)
	engine.open_project(args.project)

	if args.convert:
		engine.save_project(args.convert)
		exit(True)

	# try to get output node
	if args.output and args.render:
		out_node = engine.node(args.output)
		if not out_node:
			raise BaseException("Invalid output node path specified")

	if args.render:
		# do rendering here
		if args.frange:
			out_node.setParms({'f1': args.frange[0], 'f2': args.frange[1],'f3': args.frange[2]})

		print "Rendering frames from %s to %s with step %s" % (out_node.parm('f1').eval(), out_node.parm('f2').eval(), out_node.parm('f3').eval())
		out_node.render()
		exit(True)

if __name__ == "__main__":
    main()
