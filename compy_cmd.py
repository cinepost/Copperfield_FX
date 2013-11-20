import argparse
import compy

def main():
	parser = argparse.ArgumentParser(description='This is a demo script by nixCraft.')
	parser.add_argument('-p', '--project', help='Input project file name', required=True)
	parser.add_argument('-o', '--output', help='Output node path', required=False)
	parser.add_argument('-r', '--render', help='Render', action='store_true', required=False)
	parser.add_argument('-f', '--frange', help='Frame range', nargs=3, required=False)
	parser.add_argument('-e', '--engine', help='Engine: GPU or CPU', required=False)
	

	args = parser.parse_args()

	eng = "GPU"
	if args.engine: eng = args.engine
	engine = compy.CreateEngine(eng)
	engine.open_project(args.project)

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

if __name__ == "__main__":
    main()