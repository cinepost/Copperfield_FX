TARGET = QtTest.so
OFILES = sipQtTestcmodule.o sipQtTestQTest.o
HFILES = sipAPIQtTest.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_TEST_LIB -DQT_GUI_LIB -DQT_CORE_LIB -I. -I/Users/max/dev/Copperfield_FX/virtualenv/bin/../include/python2.7 -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/usr/local/Cellar/qt@4/4.8.7_1/mkspecs/default -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtTest.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtGui.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtCore.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/include -F/usr/local/Cellar/qt@4/4.8.7_1/lib
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = -F/usr/local/Cellar/qt@4/4.8.7_1/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtTest -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework IOKit -framework Security -framework ApplicationServices -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtGui -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib
MOC = /usr/local/Cellar/qt@4/4.8.7_1/bin/moc
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/lib/python2.7/site-packages/PyQt4 || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/lib/python2.7/site-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/lib/python2.7/site-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtTest || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtTest
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtTest/qtestcase.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtTest/qtestcase.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtTest/qtestkeyboard.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtTest/qtestkeyboard.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtTest/qtestmouse.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtTest/qtestmouse.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtTest/qtestsystem.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtTest/qtestsystem.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtTest/QtTestmod.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtTest/QtTestmod.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtTestcmodule.o
	-rm -f sipQtTestQTest.o
