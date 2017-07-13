TARGET = QtDesigner.so
OFILES = sipQtDesignercmodule.o sipQtDesignerQList0101QDesignerCustomWidgetInterface.o sipQtDesignerQPyDesignerTaskMenuExtension.o sipQtDesignerQPyDesignerPropertySheetExtension.o sipQtDesignerQPyDesignerMemberSheetExtension.o sipQtDesignerQPyDesignerCustomWidgetPlugin.o sipQtDesignerQPyDesignerCustomWidgetCollectionPlugin.o sipQtDesignerQPyDesignerContainerExtension.o sipQtDesignerQDesignerTaskMenuExtension.o sipQtDesignerQExtensionManager.o sipQtDesignerQDesignerPropertySheetExtension.o sipQtDesignerQDesignerMemberSheetExtension.o sipQtDesignerQFormBuilder.o sipQtDesignerQAbstractExtensionManager.o sipQtDesignerQExtensionFactory.o sipQtDesignerQAbstractExtensionFactory.o sipQtDesignerQDesignerCustomWidgetCollectionInterface.o sipQtDesignerQDesignerCustomWidgetInterface.o sipQtDesignerQDesignerContainerExtension.o sipQtDesignerQDesignerWidgetBoxInterface.o sipQtDesignerQDesignerPropertyEditorInterface.o sipQtDesignerQDesignerObjectInspectorInterface.o sipQtDesignerQDesignerFormWindowManagerInterface.o sipQtDesignerQDesignerFormWindowCursorInterface.o sipQtDesignerQDesignerFormWindowInterfaceFeature.o sipQtDesignerQDesignerFormWindowInterface.o sipQtDesignerQDesignerFormEditorInterface.o sipQtDesignerQAbstractFormBuilder.o sipQtDesignerQDesignerActionEditorInterface.o
HFILES = sipAPIQtDesigner.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_GUI_LIB -DQT_CORE_LIB -I. -I/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/qpy/QtDesigner -I/Users/max/dev/Copperfield_FX/virtualenv/bin/../include/python2.7 -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/usr/local/Cellar/qt@4/4.8.7_1/mkspecs/default -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtDesigner.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtGui.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/lib/QtCore.framework/Headers -I/usr/local/Cellar/qt@4/4.8.7_1/include -F/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/qpy/QtDesigner -F/usr/local/Cellar/qt@4/4.8.7_1/lib
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = -F/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/qpy/QtDesigner -L/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/qpy/QtDesigner -F/usr/local/Cellar/qt@4/4.8.7_1/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -lqpydesigner -framework QtDesigner -L/usr/local/opt/openssl/lib -L/private/tmp/qt@4-20170407-5068-1e4ad1h/qt-everywhere-opensource-src-4.8.7/lib -F/private/tmp/qt@4-20170407-5068-1e4ad1h/qt-everywhere-opensource-src-4.8.7/lib -framework QtScript -L/usr/local/opt/openssl/lib -L/private/tmp/qt@4-20170407-5068-1e4ad1h/qt-everywhere-opensource-src-4.8.7/lib -F/private/tmp/qt@4-20170407-5068-1e4ad1h/qt-everywhere-opensource-src-4.8.7/lib -framework QtCore -framework QtXml -framework QtGui -framework QtGui -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -F/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib -framework QtCore -L/usr/local/opt/openssl/lib -L/usr/local/Cellar/qt@4/4.8.7_1/lib
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
	@test -d $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner || mkdir -p $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/abstractactioneditor.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/abstractactioneditor.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/abstractformbuilder.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/abstractformbuilder.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/abstractformeditor.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/abstractformeditor.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/abstractformwindow.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/abstractformwindow.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/abstractformwindowcursor.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/abstractformwindowcursor.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/abstractformwindowmanager.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/abstractformwindowmanager.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/abstractobjectinspector.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/abstractobjectinspector.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/abstractpropertyeditor.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/abstractpropertyeditor.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/abstractwidgetbox.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/abstractwidgetbox.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/container.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/container.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/customwidget.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/customwidget.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/default_extensionfactory.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/default_extensionfactory.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/extension.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/extension.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/formbuilder.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/formbuilder.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/membersheet.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/membersheet.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/propertysheet.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/propertysheet.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/qextensionmanager.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/qextensionmanager.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/qpydesignercontainerextension.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/qpydesignercontainerextension.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/qpydesignercustomwidgetcollectionplugin.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/qpydesignercustomwidgetcollectionplugin.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/qpydesignercustomwidgetplugin.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/qpydesignercustomwidgetplugin.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/qpydesignermembersheetextension.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/qpydesignermembersheetextension.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/qpydesignerpropertysheetextension.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/qpydesignerpropertysheetextension.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/qpydesignertaskmenuextension.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/qpydesignertaskmenuextension.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/QtDesignermod.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/QtDesignermod.sip
	cp -f /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtDesigner/taskmenu.sip $(DESTDIR)/Users/max/dev/Copperfield_FX/virtualenv/bin/../share/sip/PyQt4/QtDesigner/taskmenu.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtDesignercmodule.o
	-rm -f sipQtDesignerQList0101QDesignerCustomWidgetInterface.o
	-rm -f sipQtDesignerQPyDesignerTaskMenuExtension.o
	-rm -f sipQtDesignerQPyDesignerPropertySheetExtension.o
	-rm -f sipQtDesignerQPyDesignerMemberSheetExtension.o
	-rm -f sipQtDesignerQPyDesignerCustomWidgetPlugin.o
	-rm -f sipQtDesignerQPyDesignerCustomWidgetCollectionPlugin.o
	-rm -f sipQtDesignerQPyDesignerContainerExtension.o
	-rm -f sipQtDesignerQDesignerTaskMenuExtension.o
	-rm -f sipQtDesignerQExtensionManager.o
	-rm -f sipQtDesignerQDesignerPropertySheetExtension.o
	-rm -f sipQtDesignerQDesignerMemberSheetExtension.o
	-rm -f sipQtDesignerQFormBuilder.o
	-rm -f sipQtDesignerQAbstractExtensionManager.o
	-rm -f sipQtDesignerQExtensionFactory.o
	-rm -f sipQtDesignerQAbstractExtensionFactory.o
	-rm -f sipQtDesignerQDesignerCustomWidgetCollectionInterface.o
	-rm -f sipQtDesignerQDesignerCustomWidgetInterface.o
	-rm -f sipQtDesignerQDesignerContainerExtension.o
	-rm -f sipQtDesignerQDesignerWidgetBoxInterface.o
	-rm -f sipQtDesignerQDesignerPropertyEditorInterface.o
	-rm -f sipQtDesignerQDesignerObjectInspectorInterface.o
	-rm -f sipQtDesignerQDesignerFormWindowManagerInterface.o
	-rm -f sipQtDesignerQDesignerFormWindowCursorInterface.o
	-rm -f sipQtDesignerQDesignerFormWindowInterfaceFeature.o
	-rm -f sipQtDesignerQDesignerFormWindowInterface.o
	-rm -f sipQtDesignerQDesignerFormEditorInterface.o
	-rm -f sipQtDesignerQAbstractFormBuilder.o
	-rm -f sipQtDesignerQDesignerActionEditorInterface.o
