#!/bin/bash
CWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

SIP_VERSION=4.19.3 
PYQT4_VERSION=4.12.1 #4.10.4 #4.12.1

trap '{ echo "Hey, you pressed Ctrl-C.  Time to quit." ; exit 1; }' INT

# Install wget, git, virtualenv, qt4
if [[ "$OSTYPE" == "darwin"* ]]; then
	which -s brew
	if [[ $? != 0 ]] ; then
    	# Install Homebrew
    	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	else
		echo "Updating brew ..."
    	brew update
	fi

	brew tap cartr/qt4
	brew tap-pin cartr/qt4
	brew list python &>/dev/null || brew install python
	brew list wget &>/dev/null || brew install wget
	brew list git &>/dev/null || brew install git
	brew list qt@4 &>/dev/null || brew install qt@4
	brew list qt-webkit@2.3 &>/dev/null || brew install qt-webkit@2.3

elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	sudo apt-get install python-virtualenv git wget python-dev python-qt4 python-qt4-dev python-sip python-sip-dev build-essential gfortran libqt4-dev libqtwebkit-dev qt4-qmake libpq-dev libsqlite3-dev qt4-dev-tools qt4-doc unixodbc-dev pyqt4-dev-tools -y
fi

# Create python virtual environment if needed
if [ ! -d "virtualenv" ]; then
	virtualenv virtualenv --no-site-packages #--always-copy
fi

# Activate python virtual environment
source virtualenv/bin/activate

# Install third party python packages
pip install -r requirements.txt

# Create temp directory to collect PyOpenCl, SIP, PyQT4
if [ ! -d "tmp" ]; then
	echo "Creating temp directory ..."
	mkdir tmp
fi
cd tmp


function check_pyopencl {
	python -c "exec(\"import pyopencl\\nif not pyopencl.have_gl(): exit(1)\")"  &> /dev/null
	[ $? -eq 0 ]
}

function check_sip {
	python -c "import sip"  &> /dev/null
	[ $? -eq 0 ]
}

function check_pyqt4 {
	python -c "import PyQt4"  &> /dev/null
	[ $? -eq 0 ]
}

if check_pyopencl; then
	echo "PyOpenCL already installed. All good!"
else
	# Install and configure PyOpenCl
	if [ -d "pyopencl-2017.2" ]; then
		# clean previous build
		rm -rf pyopencl-2017.2
	fi 

	if [ ! -f "pyopencl-2017.2.tar.gz" ]; then
		echo "Downloading pyopencl-2017.2"
		wget https://pypi.python.org/packages/51/cd/6142228eb3b02df9e23e5468ce6c53d1c57275bdc05bccab11e1a1e1bfec/pyopencl-2017.2.tar.gz#md5=3af7bebe41c59e12bc21d58607812445
	else
		# clean previous build
		rm -rf pyopencl-2017.2
	fi

	echo "Configuring PyOpenCL package"
	tar -xvf pyopencl-2017.2.tar.gz
	cd pyopencl-2017.2
	git submodule init
	git submodule update
	python configure.py --cl-enable-gl
	python setup.py build
	make
	python setup.py install
	cd ..
fi

if check_sip; then
	echo "SIP v$SIP_VERSION already installed. All good!"
else
	echo "Installing SIP package ..."
	# Install and configure SIP
	if [ -d "sip-$SIP_VERSION" ]; then
		# clean previous build
		rm -rf sip-$SIP_VERSION
	fi 

	echo "Downloading SIP"
	if [[ "$OSTYPE" == "msys"]] || [["$OSTYPE" == "cygwin" ]]; then
		# Windows version of SIP
		if [ ! -f "sip-$SIP_VERSION.zip" ]; then
			wget https://sourceforge.net/projects/pyqt/files/sip/sip-$SIP_VERSION/sip-$SIP_VERSION.zip
		fi

		unzip sip-$SIP_VERSION.zip
		cd sip-$SIP_VERSION

	elif [[ "$OSTYPE" == "linux-gnu" ]] || [[ "$OSTYPE" == "darwin"* ]]; then
		# Linux/Macos version of SIP
		if [ ! -f "sip-$SIP_VERSION.tar.gz" ]; then
			wget https://sourceforge.net/projects/pyqt/files/sip/sip-$SIP_VERSION/sip-$SIP_VERSION.tar.gz
		fi

		tar -xvf sip-$SIP_VERSION.tar.gz
		cd sip-$SIP_VERSION
	
	else
		echo "Unsupported platform ${OSTYPE} ! Abort installation"
		return 1
	fi

	echo "Configuring SIP package ..."
	python configure.py --incdir=../../virtualenv/include/python2.7
	make
	make install
	cd ..
fi

if check_pyqt4; then
	echo "PyQt4 v$PYQT4_VERSION already installed. All good!"
else
	echo "Installing PyQT4 package ..."
	if [[ "$OSTYPE" == "darwin"* ]]; then
		# Macos version of PyQt4
		if [ -d "PyQt4_gpl_mac-$PYQT4_VERSION" ]; then
			# clean previous build
			rm -rf PyQt4_gpl_mac-$PYQT4_VERSION
		fi

		if [ ! -f "PyQt4_gpl_mac-$PYQT4_VERSION.tar.gz" ]; then
			echo "Downloading PyQt4 for Mac OS"
			wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-$PYQT4_VERSION/PyQt4_gpl_mac-$PYQT4_VERSION.tar.gz
		fi
		
		tar -xvf PyQt4_gpl_mac-$PYQT4_VERSION.tar.gz
		cd PyQt4_gpl_mac-$PYQT4_VERSION

	elif [[ "$OSTYPE" == "linux-gnu" ]]; then
		# Linux version of PyQt4
		if [ -d "PyQt4_gpl_x11-$PYQT4_VERSION" ]; then
			# clean previous build
			rm -rf PyQt4_gpl_x11-$PYQT4_VERSION
		fi

		if [ ! -f "PyQt4_gpl_x11-$PYQT4_VERSION.tar.gz" ]; then
			echo "Downloading PyQt4 for GNU/Linux"
			wget https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-$PYQT4_VERSION/PyQt4_gpl_x11-$PYQT4_VERSION.tar.gz
		fi

		tar -xvf PyQt4_gpl_x11-$PYQT4_VERSION.tar.gz
		cd PyQt4_gpl_x11-$PYQT4_VERSION
	
	elif [[ "$OSTYPE" == "msys"]] || [["$OSTYPE" == "cygwin" ]]; then
		# Windows version of PyQt4
		if [ -d "PyQt4_gpl_win-$PYQT4_VERSION" ]; then
			# clean previous build
			rm -rf PyQt4_gpl_win-$PYQT4_VERSION
		fi

		if [ ! -f "PyQt4_gpl_win-$PYQT4_VERSION.zip" ]; then
			echo "Downloading PyQt4 for Windows"
			wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-$PYQT4_VERSION/PyQt4_gpl_win-$PYQT4_VERSION.zip
		fi
		
		unzip PyQt4_gpl_win-$PYQT4_VERSION.zip
		cd PyQt4_gpl_win-$PYQT4_VERSION
	else
		echo "Unsupported platform ${OSTYPE} ! Abort installation"
		return 1
	fi

	echo "Configuring PyQt4 package ..."
	python configure-ng.py --confirm-license --sip-incdir $CWD/tmp/sip-$SIP_VERSION/siplib
	make
	make install
	cd ..
fi

echo ""
if [ ! check_pyopencl ]; then
	echo "Unfortunately PyOpenCL installation failed. Please check the output ... :((("
	return 1
fi

if [ ! check_sip ]; then 
	echo "Unfortunately SIP v$SIP_VERSION installation failed. Please check the output ... :((("
	return 1
fi

if [ ! check_pyqt4 ]; then
	echo "Unfortunately PyQt4 v$PYQT4_VERSION installation failed. Please check the output ... :((("
	return 1
fi


echo "Everything seems to be configured and installed OK !\n"
cd $CWD
. ./copper_setup
#rm -rf tmp
