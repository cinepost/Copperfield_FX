import argparse
import compy

def main():
	parser = argparse.ArgumentParser(description='This is a demo script by nixCraft.')
	parser.add_argument('-p','--project', help='Input project file name',required=True)
	parser.add_argument('-o','--output',help='Output node path', required=False)
	

	args = parser.parse_args()

	engine = compy.CreateEngine("GPU")
	engine.open_project(args.project)


if __name__ == "__main__":
    main()