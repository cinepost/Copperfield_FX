TARGET = QtXml.so
OFILES = sipQtXmlcmodule.o sipQtXmlQXmlDefaultHandler.o sipQtXmlQXmlDeclHandler.o sipQtXmlQXmlLexicalHandler.o sipQtXmlQXmlEntityResolver.o sipQtXmlQXmlDTDHandler.o sipQtXmlQXmlErrorHandler.o sipQtXmlQXmlContentHandler.o sipQtXmlQXmlLocator.o sipQtXmlQXmlSimpleReader.o sipQtXmlQXmlReader.o sipQtXmlQXmlParseException.o sipQtXmlQXmlInputSource.o sipQtXmlQXmlAttributes.o sipQtXmlQXmlNamespaceSupport.o sipQtXmlQDomProcessingInstruction.o sipQtXmlQDomEntityReference.o sipQtXmlQDomEntity.o sipQtXmlQDomNotation.o sipQtXmlQDomCDATASection.o sipQtXmlQDomComment.o sipQtXmlQDomText.o sipQtXmlQDomElement.o sipQtXmlQDomAttr.o sipQtXmlQDomCharacterData.o sipQtXmlQDomDocumentFragment.o sipQtXmlQDomNamedNodeMap.o sipQtXmlQDomDocument.o sipQtXmlQDomDocumentType.o sipQtXmlQDomNodeList.o sipQtXmlQDomNode.o sipQtXmlQDomImplementation.o
HFILES = sipAPIQtXml.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_XML_LIB -DQT_CORE_LIB -I. -I/Users/max/dev/Copperfield_FX/virtualenv/bin/../include/python2.7 -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/usr/local/Cellar/qt@4/4.8.7_1/mkspecs/default -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtXml.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtCore.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/include -F/usr/local/Cellar/qt@4/4.8.7_1/lib
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = -F/usr/local/Cellar/qt@4/4.8.7_1/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtXml -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib
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
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXml || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXml
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXml/qdom.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXml/qdom.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXml/QtXmlmod.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXml/QtXmlmod.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXml/qxml.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXml/qxml.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtXml/qxmlstream.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtXml/qxmlstream.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtXmlcmodule.o
	-rm -f sipQtXmlQXmlDefaultHandler.o
	-rm -f sipQtXmlQXmlDeclHandler.o
	-rm -f sipQtXmlQXmlLexicalHandler.o
	-rm -f sipQtXmlQXmlEntityResolver.o
	-rm -f sipQtXmlQXmlDTDHandler.o
	-rm -f sipQtXmlQXmlErrorHandler.o
	-rm -f sipQtXmlQXmlContentHandler.o
	-rm -f sipQtXmlQXmlLocator.o
	-rm -f sipQtXmlQXmlSimpleReader.o
	-rm -f sipQtXmlQXmlReader.o
	-rm -f sipQtXmlQXmlParseException.o
	-rm -f sipQtXmlQXmlInputSource.o
	-rm -f sipQtXmlQXmlAttributes.o
	-rm -f sipQtXmlQXmlNamespaceSupport.o
	-rm -f sipQtXmlQDomProcessingInstruction.o
	-rm -f sipQtXmlQDomEntityReference.o
	-rm -f sipQtXmlQDomEntity.o
	-rm -f sipQtXmlQDomNotation.o
	-rm -f sipQtXmlQDomCDATASection.o
	-rm -f sipQtXmlQDomComment.o
	-rm -f sipQtXmlQDomText.o
	-rm -f sipQtXmlQDomElement.o
	-rm -f sipQtXmlQDomAttr.o
	-rm -f sipQtXmlQDomCharacterData.o
	-rm -f sipQtXmlQDomDocumentFragment.o
	-rm -f sipQtXmlQDomNamedNodeMap.o
	-rm -f sipQtXmlQDomDocument.o
	-rm -f sipQtXmlQDomDocumentType.o
	-rm -f sipQtXmlQDomNodeList.o
	-rm -f sipQtXmlQDomNode.o
	-rm -f sipQtXmlQDomImplementation.o
