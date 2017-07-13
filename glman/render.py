from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT


if __name__ == "__main__":
	import sys, argparse

	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-i', '--interactive', help='Interactive windowed mode', action='store_true', required=False)

	args = vars(parser.parse_args())

	if args['interactive']:
		from PyQt4.QtWidgets import QApplication, QWidget

		app = QApplication(sys.argv)

		w = QWidget()
		w.resize(250, 150)
		w.move(300, 300)
		w.setWindowTitle('GLMan')
		w.show()

		sys.exit(app.exec_())