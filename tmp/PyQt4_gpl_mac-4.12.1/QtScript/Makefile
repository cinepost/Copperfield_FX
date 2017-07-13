TARGET = QtScript.so
OFILES = sipQtScriptcmodule.o sipQtScriptQList0100QScriptValue.o sipQtScriptQList0100QScriptContextInfo.o sipQtScriptQScriptValueIterator.o sipQtScriptQScriptValuePropertyFlags.o sipQtScriptQScriptValueResolveFlags.o sipQtScriptQScriptValue.o sipQtScriptQScriptString.o sipQtScriptQScriptEngineAgent.o sipQtScriptQScriptSyntaxCheckResult.o sipQtScriptQScriptEngineQObjectWrapOptions.o sipQtScriptQScriptEngine.o sipQtScriptQScriptContextInfo.o sipQtScriptQScriptContext.o sipQtScriptQScriptClassPropertyIterator.o sipQtScriptQScriptClassQueryFlags.o sipQtScriptQScriptClass.o
HFILES = sipAPIQtScript.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_SCRIPT_LIB -DQT_CORE_LIB -I. -I/Users/max/dev/Copperfield_FX/virtualenv/bin/../include/python2.7 -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/usr/local/Cellar/qt@4/4.8.7_1/mkspecs/default -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtScript.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtCore.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/include -F/usr/local/Cellar/qt@4/4.8.7_1/lib
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = -F/usr/local/Cellar/qt@4/4.8.7_1/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtScript -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib
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
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptclass.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/qscriptclass.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptclasspropertyiterator.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/qscriptclasspropertyiterator.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptcontext.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/qscriptcontext.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptcontextinfo.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/qscriptcontextinfo.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptengine.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/qscriptengine.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptengineagent.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/qscriptengineagent.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptstring.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/qscriptstring.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptvalue.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/qscriptvalue.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptvalueiterator.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/qscriptvalueiterator.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/QtScriptmod.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtScript/QtScriptmod.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtScriptcmodule.o
	-rm -f sipQtScriptQList0100QScriptValue.o
	-rm -f sipQtScriptQList0100QScriptContextInfo.o
	-rm -f sipQtScriptQScriptValueIterator.o
	-rm -f sipQtScriptQScriptValuePropertyFlags.o
	-rm -f sipQtScriptQScriptValueResolveFlags.o
	-rm -f sipQtScriptQScriptValue.o
	-rm -f sipQtScriptQScriptString.o
	-rm -f sipQtScriptQScriptEngineAgent.o
	-rm -f sipQtScriptQScriptSyntaxCheckResult.o
	-rm -f sipQtScriptQScriptEngineQObjectWrapOptions.o
	-rm -f sipQtScriptQScriptEngine.o
	-rm -f sipQtScriptQScriptContextInfo.o
	-rm -f sipQtScriptQScriptContext.o
	-rm -f sipQtScriptQScriptClassPropertyIterator.o
	-rm -f sipQtScriptQScriptClassQueryFlags.o
	-rm -f sipQtScriptQScriptClass.o
