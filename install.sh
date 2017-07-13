#brew install wget
brew install qt@5.9

mkdir deps
cd deps
wget http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.9/PyQt5_gpl-5.9.tar.gz
#wget http://freefr.dl.sourceforge.net/project/pyqt/sip/sip-4.18/sip-4.18.tar.gz

tar -xvf sip-4.18.tar.gz
cd sip-4.18
python configure.py -d /usr/local/lib/python2.7/site-packages/
make
make install

cd ..
tar -xvf PyQt5_gpl-5.9.tar.gz
cd PyQt5_gpl-5.9
python configure.py -d /usr/local/lib/python2.7/site-packages/ --qmake=/usr/local/Cellar/qt5/5.9/bin/qmake --sip=/usr/local/bin/sip --sip-incdir=../sip-4.18/siplib
make
make install

#rm -rf ../deps
