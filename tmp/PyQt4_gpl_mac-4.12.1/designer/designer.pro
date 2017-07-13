VPATH = /Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/designer
CONFIG      += plugin @QTCONFIG@ warn_on

greaterThan(QT_MAJOR_VERSION, 4) {
    QT += designer

    # Work around QTBUG-39300.
    CONFIG -= android_install
}

lessThan(QT_MAJOR_VERSION, 5) {
    CONFIG += designer
}

TARGET      = pyqt4
TEMPLATE    = lib

INCLUDEPATH += /usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7
LIBS        += -L/usr/local/opt/python/Frameworks/Python.framework/Versions/2.7/lib -lpython2.7
DEFINES     += PYTHON_LIB=\\\"Python.framework/Versions/2.7/Python\\\"

SOURCES     = pluginloader.cpp
HEADERS     = pluginloader.h

# Install.
target.path = /usr/local/Cellar/qt@4/4.8.7_1/lib/qt4/plugins/designer

python.path = /usr/local/Cellar/qt@4/4.8.7_1/lib/qt4/plugins/designer
python.files = python

INSTALLS    += target python
