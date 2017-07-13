#!/bin/sh

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
	sudo apt-get install virtualenv git wget qt4-default libqt4-dev
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
	if [ ! -d "sip-4.19.3" ]; then
		echo "Downloading SIP"
		if [[ "$OSTYPE" == "msys"]] || [["$OSTYPE" == "cygwin" ]]; then
			# Windows version of PyQt4
			if [ ! -d "sip-4.19.3.zip" ]; then
				wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.3/sip-4.19.3.zip
				unzip sip-4.19.3.zip
			fi
		elif [[ "$OSTYPE" == "linux-gnu" ]] || [[ "$OSTYPE" == "darwin"* ]]; then
			# Linux/Macos version of PyQt4
			if [ ! -d "sip-4.19.3.tar.gz" ]; then
				wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.3/sip-4.19.3.tar.gz
				tar -xvf  sip-4.19.3.tar.gz
			fi
		else
			echo "Unsupported platform ${OSTYPE} ! Abort installation"
			exit
		fi
	fi

	echo "Configuring SIP package ..."
	python configure.py #-d /usr/local/lib/python2.7/site-packages/
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
			echo "Downloading PyQt4 for Mac OS"
			wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_mac-4.12.1.tar.gz
			tar -xvf PyQt4_gpl_mac-4.12.1.tar.gz
			cd PyQt4_gpl_mac-4.12.1
		fi
	elif [[ "$OSTYPE" == "linux-gnu" ]]; then
		# Linux version of PyQt4
		if [ ! -d "PyQt4_gpl_x11-4.12.1" ]; then
			echo "Downloading PyQt4 for GNU/Linux"
			wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_x11-4.12.1.tar.gz
			tar -xvf PyQt4_gpl_x11-4.12.1.tar.gz
			cd PyQt4_gpl_x11-4.12.1
		fi
	elif [[ "$OSTYPE" == "msys"]] || [["$OSTYPE" == "cygwin" ]]; then
		# Windows version of PyQt4
		if [ ! -d "PyQt4_gpl_win-4.12.1" ]; then
			wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_win-4.12.1.zip
			unzip PyQt4_gpl_win-4.12.1.zip
			cd PyQt4_gpl_win-4.12.1
		fi
	else
		echo "Unsupported platform ${OSTYPE} ! Abort installation"
		exit
	fi

	echo "Configuring PyQT4 package ..."
	python configure.py --qmake=/usr/local/bin/qmake --use-arch x86_64 #--sip=/usr/local/bin/sip --sip-incdir=../sip-4.19.3/siplib  -d /usr/local/lib/python2.7/site-packages/
	make
	make install
	cd ..
fi

#rm -rf tmp
