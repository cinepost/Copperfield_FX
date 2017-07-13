TARGET = QtNetwork.so
OFILES = sipQtNetworkcmodule.o sipQtNetworkQList0100QSslCipher.o sipQtNetworkQList0100QSslCertificate.o sipQtNetworkQList0100QNetworkProxy.o sipQtNetworkQList0100QNetworkInterface.o sipQtNetworkQList0100QNetworkAddressEntry.o sipQtNetworkQList0100QNetworkCookie.o sipQtNetworkQList0100QNetworkConfiguration.o sipQtNetworkQList0100QSslError.o sipQtNetworkQList0100QHostAddress.o sipQtNetworkQPair0100QHostAddress1800.o sipQtNetworkQUrlInfo.o sipQtNetworkQUdpSocketBindMode.o sipQtNetworkQUdpSocket.o sipQtNetworkQTcpServer.o sipQtNetworkQSslSocket.o sipQtNetworkQTcpSocket.o sipQtNetworkQSslKey.o sipQtNetworkQSslError.o sipQtNetworkQSslCipher.o sipQtNetworkQSslConfiguration.o sipQtNetworkQMultiMap0100QSslAlternateNameEntryType0100QString.o sipQtNetworkQSslCertificate.o sipQtNetworkQSslSslOptions.o sipQtNetworkQSsl.o sipQtNetworkQNetworkSession.o sipQtNetworkQNetworkRequest.o sipQtNetworkQNetworkReply.o sipQtNetworkQNetworkProxyFactory.o sipQtNetworkQNetworkProxyQuery.o sipQtNetworkQNetworkProxyCapabilities.o sipQtNetworkQNetworkProxy.o sipQtNetworkQNetworkInterfaceInterfaceFlags.o sipQtNetworkQNetworkInterface.o sipQtNetworkQNetworkAddressEntry.o sipQtNetworkQNetworkDiskCache.o sipQtNetworkQNetworkCookieJar.o sipQtNetworkQNetworkCookie.o sipQtNetworkQNetworkConfigurationStateFlags.o sipQtNetworkQNetworkConfiguration.o sipQtNetworkQNetworkConfigurationManagerCapabilities.o sipQtNetworkQNetworkConfigurationManager.o sipQtNetworkQNetworkAccessManager.o sipQtNetworkQLocalSocket.o sipQtNetworkQLocalServer.o sipQtNetworkQHttpMultiPart.o sipQtNetworkQHttpPart.o sipQtNetworkQHttp.o sipQtNetworkQHttpRequestHeader.o sipQtNetworkQHttpResponseHeader.o sipQtNetworkQHttpHeader.o sipQtNetworkQHostInfo.o sipQtNetworkQ_IPV6ADDR.o sipQtNetworkQHostAddress.o sipQtNetworkQFtp.o sipQtNetworkQAuthenticator.o sipQtNetworkQAbstractSocket.o sipQtNetworkQAbstractNetworkCache.o sipQtNetworkQNetworkCacheMetaData.o sipQtNetworkQHash0100QNetworkRequestAttribute0100QVariant.o
HFILES = sipAPIQtNetwork.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_NETWORK_LIB -DQT_CORE_LIB -I. -I/Users/max/dev/Copperfield_FX/virtualenv/bin/../include/python2.7 -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/usr/local/Cellar/qt@4/4.8.7_1/mkspecs/default -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtNetwork.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtCore.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/include -F/usr/local/Cellar/qt@4/4.8.7_1/lib
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = -F/usr/local/Cellar/qt@4/4.8.7_1/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtNetwork -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib
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
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qabstractnetworkcache.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qabstractnetworkcache.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qabstractsocket.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qabstractsocket.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qauthenticator.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qauthenticator.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qdnslookup.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qdnslookup.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qftp.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qftp.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qhostaddress.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qhostaddress.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qhostinfo.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qhostinfo.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qhttp.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qhttp.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qhttpmultipart.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qhttpmultipart.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qlocalserver.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qlocalserver.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qlocalsocket.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qlocalsocket.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkaccessmanager.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkaccessmanager.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkconfigmanager.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkconfigmanager.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkconfiguration.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkconfiguration.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkcookie.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkcookie.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkcookiejar.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkcookiejar.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkdiskcache.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkdiskcache.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkinterface.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkinterface.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkproxy.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkproxy.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkreply.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkreply.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkrequest.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworkrequest.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworksession.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qnetworksession.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qssl.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qssl.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qsslcertificate.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qsslcertificate.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qsslcertificateextension.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qsslcertificateextension.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qsslcipher.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qsslcipher.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qsslconfiguration.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qsslconfiguration.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qsslerror.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qsslerror.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qsslkey.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qsslkey.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qsslsocket.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qsslsocket.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qtcpserver.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qtcpserver.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qtcpsocket.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qtcpsocket.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/QtNetworkmod.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/QtNetworkmod.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qudpsocket.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qudpsocket.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qurlinfo.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtNetwork/qurlinfo.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtNetworkcmodule.o
	-rm -f sipQtNetworkQList0100QSslCipher.o
	-rm -f sipQtNetworkQList0100QSslCertificate.o
	-rm -f sipQtNetworkQList0100QNetworkProxy.o
	-rm -f sipQtNetworkQList0100QNetworkInterface.o
	-rm -f sipQtNetworkQList0100QNetworkAddressEntry.o
	-rm -f sipQtNetworkQList0100QNetworkCookie.o
	-rm -f sipQtNetworkQList0100QNetworkConfiguration.o
	-rm -f sipQtNetworkQList0100QSslError.o
	-rm -f sipQtNetworkQList0100QHostAddress.o
	-rm -f sipQtNetworkQPair0100QHostAddress1800.o
	-rm -f sipQtNetworkQUrlInfo.o
	-rm -f sipQtNetworkQUdpSocketBindMode.o
	-rm -f sipQtNetworkQUdpSocket.o
	-rm -f sipQtNetworkQTcpServer.o
	-rm -f sipQtNetworkQSslSocket.o
	-rm -f sipQtNetworkQTcpSocket.o
	-rm -f sipQtNetworkQSslKey.o
	-rm -f sipQtNetworkQSslError.o
	-rm -f sipQtNetworkQSslCipher.o
	-rm -f sipQtNetworkQSslConfiguration.o
	-rm -f sipQtNetworkQMultiMap0100QSslAlternateNameEntryType0100QString.o
	-rm -f sipQtNetworkQSslCertificate.o
	-rm -f sipQtNetworkQSslSslOptions.o
	-rm -f sipQtNetworkQSsl.o
	-rm -f sipQtNetworkQNetworkSession.o
	-rm -f sipQtNetworkQNetworkRequest.o
	-rm -f sipQtNetworkQNetworkReply.o
	-rm -f sipQtNetworkQNetworkProxyFactory.o
	-rm -f sipQtNetworkQNetworkProxyQuery.o
	-rm -f sipQtNetworkQNetworkProxyCapabilities.o
	-rm -f sipQtNetworkQNetworkProxy.o
	-rm -f sipQtNetworkQNetworkInterfaceInterfaceFlags.o
	-rm -f sipQtNetworkQNetworkInterface.o
	-rm -f sipQtNetworkQNetworkAddressEntry.o
	-rm -f sipQtNetworkQNetworkDiskCache.o
	-rm -f sipQtNetworkQNetworkCookieJar.o
	-rm -f sipQtNetworkQNetworkCookie.o
	-rm -f sipQtNetworkQNetworkConfigurationStateFlags.o
	-rm -f sipQtNetworkQNetworkConfiguration.o
	-rm -f sipQtNetworkQNetworkConfigurationManagerCapabilities.o
	-rm -f sipQtNetworkQNetworkConfigurationManager.o
	-rm -f sipQtNetworkQNetworkAccessManager.o
	-rm -f sipQtNetworkQLocalSocket.o
	-rm -f sipQtNetworkQLocalServer.o
	-rm -f sipQtNetworkQHttpMultiPart.o
	-rm -f sipQtNetworkQHttpPart.o
	-rm -f sipQtNetworkQHttp.o
	-rm -f sipQtNetworkQHttpRequestHeader.o
	-rm -f sipQtNetworkQHttpResponseHeader.o
	-rm -f sipQtNetworkQHttpHeader.o
	-rm -f sipQtNetworkQHostInfo.o
	-rm -f sipQtNetworkQ_IPV6ADDR.o
	-rm -f sipQtNetworkQHostAddress.o
	-rm -f sipQtNetworkQFtp.o
	-rm -f sipQtNetworkQAuthenticator.o
	-rm -f sipQtNetworkQAbstractSocket.o
	-rm -f sipQtNetworkQAbstractNetworkCache.o
	-rm -f sipQtNetworkQNetworkCacheMetaData.o
	-rm -f sipQtNetworkQHash0100QNetworkRequestAttribute0100QVariant.o
