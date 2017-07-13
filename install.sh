#!/bin/bash
CWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

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

	brew list python &>/dev/null || brew install python
	brew list wget &>/dev/null || brew install wget
	brew list git &>/dev/null || brew install git
	brew list qt@4 &>/dev/null || brew install qt@4
	brew list qt-webkit@2.3 &>/dev/null || brew install qt-webkit@2.3

elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	sudo apt-get install virtualenv git wget python-dev python-qt4 python-qt4-dev python-sip python-sip-dev build-essential gfortran libqt4-dev qt4-qmake libpq-dev libsqlite3-dev qt4-dev-tools qt4-doc unixodbc-dev pyqt4-dev-tools -y
fi

# Create python virtual environment if needed
if [ ! -d "virtualenv" ]; then
	virtualenv virtualenv --no-site-packages
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


python -c "import pyopencl"  &> /dev/null
if [ $? -eq 0 ]; then
	echo "PyOpenCL already installed"
else
	# Install and configure PyOpenCl
	if [ ! -d "pyopencl-2017.2" ]; then
		echo "Downloading pyopencl-2017.2"
		wget https://pypi.python.org/packages/51/cd/6142228eb3b02df9e23e5468ce6c53d1c57275bdc05bccab11e1a1e1bfec/pyopencl-2017.2.tar.gz#md5=3af7bebe41c59e12bc21d58607812445
	else
		echo "Removing previous build"
		rm -rf pyopencl-2017.2/build
		rm pyopencl-2017.2/siteconf.py
	fi

	echo "Configuring PyOpenCL package"
	tar -xvf pyopencl-2017.2.tar.gz
	cd pyopencl-2017.2
	git submodule init
	git submodule update
	python configure.py #--cl-enable-gl
	python setup.py build
	make
	python setup.py install
	cd ..
fi

python -c "import sip"  &> /dev/null
if [ $? -eq 0 ]; then
	echo "SIP already installed."
else
	echo "Installing SIP package ..."
	# Install and configure SIP
	if [ ! -d "sip-4.16.7" ]; then
		echo "Downloading SIP"
		if [[ "$OSTYPE" == "msys"]] || [["$OSTYPE" == "cygwin" ]]; then
			# Windows version of SIP
			if [ ! -d "sip-4.16.7.zip" ]; then
				wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.16.7/sip-4.16.7.zip
				unzip sip-4.16.7.zip
			fi
		elif [[ "$OSTYPE" == "linux-gnu" ]] || [[ "$OSTYPE" == "darwin"* ]]; then
			# Linux/Macos version of SIP
			if [ ! -d "sip-4.16.7.tar.gz" ]; then
				wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.16.7/sip-4.16.7.tar.gz
				tar -xvf sip-4.16.7.tar.gz
			fi
		else
			echo "Unsupported platform ${OSTYPE} ! Abort installation"
			exit
		fi
	fi

	echo "Configuring SIP package ..."
	cd sip-4.16.7
	python config.py #-d /usr/local/lib/python2.7/site-packages/
	make
	make install
	cd ..
fi

python -c "import PyQt4"  &> /dev/null
if [ $? -eq 0 ]; then
	echo "PyQt4 already installed."
else
	echo "Installing PyQT4 package ..."
	if [[ "$OSTYPE" == "darwin"* ]]; then
		# Macos version of PyQt4
		if [ ! -d "PyQt4_gpl_mac-4.12.1" ]; then
			if [ ! -d "PyQt4_gpl_mac-4.12.1.tar.gz" ]; then
				echo "Downloading PyQt4 for Mac OS"
				wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_mac-4.12.1.tar.gz
			fi
			tar -xvf PyQt4_gpl_mac-4.12.1.tar.gz
		fi
		cd PyQt4_gpl_mac-4.12.1
	elif [[ "$OSTYPE" == "linux-gnu" ]]; then
		# Linux version of PyQt4
		if [ ! -d "PyQt-x11-gpl-4.10.4" ]; then
			if [ ! -d "PyQt-x11-gpl-4.10.4.tar.gz" ]; then
				echo "Downloading PyQt4 for GNU/Linux"
				wget https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.10.4/PyQt-x11-gpl-4.10.4.tar.gz
			fi
			tar -xvf PyQt-x11-gpl-4.10.4.tar.gz
		fi
		cd PyQt-x11-gpl-4.10.4
	elif [[ "$OSTYPE" == "msys"]] || [["$OSTYPE" == "cygwin" ]]; then
		# Windows version of PyQt4
		if [ ! -d "PyQt4_gpl_win-4.12.1" ]; then
			if [ ! -d "PyQt4_gpl_win-4.12.1.zip" ]; then
				echo "Downloading PyQt4 for Windows"
				wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_win-4.12.1.zip
			fi
			unzip PyQt4_gpl_win-4.12.1.zip
		fi
		cd PyQt4_gpl_win-4.12.1
	else
		echo "Unsupported platform ${OSTYPE} ! Abort installation"
		exit
	fi

	echo "Configuring PyQt4 package ..."
	#python configure-ng.py --qmake=$(which qmake) --sip-incdir=$CWD/tmp/sip-4.19.3/siplib --confirm-license #--use-arch x86_64 --sip=/usr/local/bin/sip --sip-incdir=../sip-4.19.3/siplib  -d /usr/local/lib/python2.7/site-packages/
	python configure-ng.py --confirm-license
	make
	make install
	cd ..
fi

#rm -rf tmp
