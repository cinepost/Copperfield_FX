TARGET = QtDeclarative.so
OFILES = sipQtDeclarativecmodule.o sipQtDeclarativeQList0100QDeclarativeError.o sipQtDeclarativeQPyDeclarativePropertyValueSource.o sipQtDeclarativeQDeclarativeListProperty0100QObject.o sipQtDeclarativeQDeclarativeView.o sipQtDeclarativeQDeclarativeScriptString.o sipQtDeclarativeQDeclarativePropertyValueSource.o sipQtDeclarativeQDeclarativePropertyMap.o sipQtDeclarativeQDeclarativeProperty.o sipQtDeclarativeQDeclarativeNetworkAccessManagerFactory.o sipQtDeclarativeQDeclarativeListReference.o sipQtDeclarativeQDeclarativeItem.o sipQtDeclarativeQDeclarativeParserStatus.o sipQtDeclarativeQDeclarativeImageProvider.o sipQtDeclarativeQDeclarativeExtensionPlugin.o sipQtDeclarativeQDeclarativeExpression.o sipQtDeclarativeQDeclarativeError.o sipQtDeclarativeQDeclarativeEngine.o sipQtDeclarativeQDeclarativeContext.o sipQtDeclarativeQDeclarativeComponent.o
HFILES = sipAPIQtDeclarative.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_DECLARATIVE_LIB -DQT_GUI_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I. -I/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/qpy/QtDeclarative -I/Users/max/dev/Copperfield_FX/virtualenv/bin/../include/python2.7 -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/usr/local/Cellar/qt@4/4.8.7_1/mkspecs/default -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtDeclarative.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtGui.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtNetwork.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtCore.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/include -F/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/qpy/QtDeclarative -F/usr/local/Cellar/qt@4/4.8.7_1/lib
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = -F/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/qpy/QtDeclarative -L/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/qpy/QtDeclarative -F/usr/local/Cellar/qt@4/4.8.7_1/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -lqpydeclarative -framework QtDeclarative -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtScript -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -framework QtSvg -framework QtGui -framework QtSql -framework QtXmlPatterns -framework QtNetwork -framework QtGui -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtNetwork -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib
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
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativecomponent.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativecomponent.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativecontext.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativecontext.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativeengine.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativeengine.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativeerror.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativeerror.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativeexpression.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativeexpression.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativeextensionplugin.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativeextensionplugin.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativeimageprovider.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativeimageprovider.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativeitem.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativeitem.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativelist.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativelist.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativenetworkaccessmanagerfactory.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativenetworkaccessmanagerfactory.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativeparserstatus.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativeparserstatus.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativeproperty.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativeproperty.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativepropertymap.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativepropertymap.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativepropertyvaluesource.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativepropertyvaluesource.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativescriptstring.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativescriptstring.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qdeclarativeview.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qdeclarativeview.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qpydeclarativelistproperty.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qpydeclarativelistproperty.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/qpydeclarativepropertyvaluesource.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/qpydeclarativepropertyvaluesource.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDeclarative/QtDeclarativemod.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDeclarative/QtDeclarativemod.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtDeclarativecmodule.o
	-rm -f sipQtDeclarativeQList0100QDeclarativeError.o
	-rm -f sipQtDeclarativeQPyDeclarativePropertyValueSource.o
	-rm -f sipQtDeclarativeQDeclarativeListProperty0100QObject.o
	-rm -f sipQtDeclarativeQDeclarativeView.o
	-rm -f sipQtDeclarativeQDeclarativeScriptString.o
	-rm -f sipQtDeclarativeQDeclarativePropertyValueSource.o
	-rm -f sipQtDeclarativeQDeclarativePropertyMap.o
	-rm -f sipQtDeclarativeQDeclarativeProperty.o
	-rm -f sipQtDeclarativeQDeclarativeNetworkAccessManagerFactory.o
	-rm -f sipQtDeclarativeQDeclarativeListReference.o
	-rm -f sipQtDeclarativeQDeclarativeItem.o
	-rm -f sipQtDeclarativeQDeclarativeParserStatus.o
	-rm -f sipQtDeclarativeQDeclarativeImageProvider.o
	-rm -f sipQtDeclarativeQDeclarativeExtensionPlugin.o
	-rm -f sipQtDeclarativeQDeclarativeExpression.o
	-rm -f sipQtDeclarativeQDeclarativeError.o
	-rm -f sipQtDeclarativeQDeclarativeEngine.o
	-rm -f sipQtDeclarativeQDeclarativeContext.o
	-rm -f sipQtDeclarativeQDeclarativeComponent.o
