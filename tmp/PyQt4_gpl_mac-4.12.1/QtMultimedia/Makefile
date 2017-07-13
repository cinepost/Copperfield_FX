TARGET = QtMultimedia.so
OFILES = sipQtMultimediacmodule.o sipQtMultimediaQList0100QAudioDeviceInfo.o sipQtMultimediaQVideoSurfaceFormat.o sipQtMultimediaQList0100QVideoFramePixelFormat.o sipQtMultimediaQVideoFrame.o sipQtMultimediaQAudioOutput.o sipQtMultimediaQAudioInput.o sipQtMultimediaQList0100QAudioFormatSampleType.o sipQtMultimediaQList0100QAudioFormatEndian.o sipQtMultimediaQAudioFormat.o sipQtMultimediaQAudioDeviceInfo.o sipQtMultimediaQAudio.o sipQtMultimediaQAbstractVideoSurface.o sipQtMultimediaQAbstractVideoBuffer.o
HFILES = sipAPIQtMultimedia.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_MULTIMEDIA_LIB -DQT_GUI_LIB -DQT_CORE_LIB -I. -I/Users/max/dev/Copperfield_FX/virtualenv/bin/../include/python2.7 -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/usr/local/Cellar/qt@4/4.8.7_1/mkspecs/default -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtMultimedia.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtGui.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtCore.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/include -F/usr/local/Cellar/qt@4/4.8.7_1/lib
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = -F/usr/local/Cellar/qt@4/4.8.7_1/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtMultimedia -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework ApplicationServices -framework CoreAudio -framework AudioUnit -framework AudioToolbox -framework QtGui -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -framework QtGui -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib
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
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/qabstractvideobuffer.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/qabstractvideobuffer.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/qabstractvideosurface.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/qabstractvideosurface.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/qaudio.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/qaudio.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/qaudiodeviceinfo.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/qaudiodeviceinfo.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/qaudioformat.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/qaudioformat.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/qaudioinput.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/qaudioinput.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/qaudiooutput.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/qaudiooutput.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/QtMultimediamod.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/QtMultimediamod.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/qvideoframe.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/qvideoframe.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtMultimedia/qvideosurfaceformat.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtMultimedia/qvideosurfaceformat.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtMultimediacmodule.o
	-rm -f sipQtMultimediaQList0100QAudioDeviceInfo.o
	-rm -f sipQtMultimediaQVideoSurfaceFormat.o
	-rm -f sipQtMultimediaQList0100QVideoFramePixelFormat.o
	-rm -f sipQtMultimediaQVideoFrame.o
	-rm -f sipQtMultimediaQAudioOutput.o
	-rm -f sipQtMultimediaQAudioInput.o
	-rm -f sipQtMultimediaQList0100QAudioFormatSampleType.o
	-rm -f sipQtMultimediaQList0100QAudioFormatEndian.o
	-rm -f sipQtMultimediaQAudioFormat.o
	-rm -f sipQtMultimediaQAudioDeviceInfo.o
	-rm -f sipQtMultimediaQAudio.o
	-rm -f sipQtMultimediaQAbstractVideoSurface.o
	-rm -f sipQtMultimediaQAbstractVideoBuffer.o
