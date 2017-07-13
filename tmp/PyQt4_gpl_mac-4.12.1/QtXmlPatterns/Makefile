TARGET = QtXmlPatterns.so
OFILES = sipQtXmlPatternscmodule.o sipQtXmlPatternsQVector0100QXmlNodeModelIndex.o sipQtXmlPatternsQVector0100QXmlName.o sipQtXmlPatternsQXmlSchemaValidator.o sipQtXmlPatternsQXmlSchema.o sipQtXmlPatternsQXmlResultItems.o sipQtXmlPatternsQXmlQuery.o sipQtXmlPatternsQXmlNamePool.o sipQtXmlPatternsQXmlName.o sipQtXmlPatternsQXmlFormatter.o sipQtXmlPatternsQXmlSerializer.o sipQtXmlPatternsQSourceLocation.o sipQtXmlPatternsQSimpleXmlNodeModel.o sipQtXmlPatternsQAbstractXmlReceiver.o sipQtXmlPatternsQXmlItem.o sipQtXmlPatternsQAbstractXmlNodeModel.o sipQtXmlPatternsQXmlNodeModelIndex.o sipQtXmlPatternsQAbstractUriResolver.o sipQtXmlPatternsQAbstractMessageHandler.o
HFILES = sipAPIQtXmlPatterns.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_XMLPATTERNS_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I. -I/Users/max/dev/Copperfield_FX/virtualenv/bin/../include/python2.7 -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/usr/local/Cellar/qt@4/4.8.7_1/mkspecs/default -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtXmlPatterns.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtNetwork.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtCore.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/include -F/usr/local/Cellar/qt@4/4.8.7_1/lib
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = -F/usr/local/Cellar/qt@4/4.8.7_1/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtXmlPatterns -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtNetwork -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -framework QtNetwork -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib
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
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qabstractmessagehandler.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qabstractmessagehandler.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qabstracturiresolver.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qabstracturiresolver.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qabstractxmlnodemodel.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qabstractxmlnodemodel.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qabstractxmlreceiver.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qabstractxmlreceiver.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qsimplexmlnodemodel.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qsimplexmlnodemodel.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qsourcelocation.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qsourcelocation.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/QtXmlPatternsmod.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/QtXmlPatternsmod.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qxmlformatter.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qxmlformatter.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qxmlname.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qxmlname.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qxmlnamepool.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qxmlnamepool.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qxmlquery.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qxmlquery.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qxmlresultitems.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qxmlresultitems.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qxmlschema.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qxmlschema.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qxmlschemavalidator.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qxmlschemavalidator.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXmlPatterns/qxmlserializer.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXmlPatterns/qxmlserializer.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtXmlPatternscmodule.o
	-rm -f sipQtXmlPatternsQVector0100QXmlNodeModelIndex.o
	-rm -f sipQtXmlPatternsQVector0100QXmlName.o
	-rm -f sipQtXmlPatternsQXmlSchemaValidator.o
	-rm -f sipQtXmlPatternsQXmlSchema.o
	-rm -f sipQtXmlPatternsQXmlResultItems.o
	-rm -f sipQtXmlPatternsQXmlQuery.o
	-rm -f sipQtXmlPatternsQXmlNamePool.o
	-rm -f sipQtXmlPatternsQXmlName.o
	-rm -f sipQtXmlPatternsQXmlFormatter.o
	-rm -f sipQtXmlPatternsQXmlSerializer.o
	-rm -f sipQtXmlPatternsQSourceLocation.o
	-rm -f sipQtXmlPatternsQSimpleXmlNodeModel.o
	-rm -f sipQtXmlPatternsQAbstractXmlReceiver.o
	-rm -f sipQtXmlPatternsQXmlItem.o
	-rm -f sipQtXmlPatternsQAbstractXmlNodeModel.o
	-rm -f sipQtXmlPatternsQXmlNodeModelIndex.o
	-rm -f sipQtXmlPatternsQAbstractUriResolver.o
	-rm -f sipQtXmlPatternsQAbstractMessageHandler.o
