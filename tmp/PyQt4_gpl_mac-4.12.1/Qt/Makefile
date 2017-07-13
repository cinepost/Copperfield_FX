TARGET = Qt.so
OFILES = sipQtcmodule.o
HFILES =  

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -I. -I/Users/max/dev/Copperfield_FX/virtualenv/bin/../include/python2.7 -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = 
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
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/Qt || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/Qt
	cp -f ../sip/Qt/Qtmod.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/Qt/Qtmod.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtcmodule.o
