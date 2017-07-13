// This is the definition of the ListWrapper class.
//
// Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt4.
// 
// This file may be used under the terms of the GNU General Public License
// version 3.0 as published by the Free Software Foundation and appearing in
// the file LICENSE included in the packaging of this file.  Please review the
// following information to ensure the GNU General Public License version 3.0
// requirements will be met: http://www.gnu.org/copyleft/gpl.html.
// 
// If you do not wish to use this file under the terms of the GPL version 3.0
// then you may purchase a commercial license.  For more information contact
// info@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


#ifndef _QPYDECLARATIVELISTWRAPPER_H
#define _QPYDECLARATIVELISTWRAPPER_H


#include <Python.h>

#include <QObject>
#include <QList>


class ListWrapper : public QObject
{
    Q_OBJECT

public:
    static ListWrapper *wrapper(PyObject *py_list, QObject *parent);

    static void append(QObject *qobj, QList<QObject *> *qlist, QObject *el);
    static void clear(QObject *qobj, QList<QObject *> *qlist);

    QList<QObject *> qobject_list;

private:
    ListWrapper(PyObject *py_list, QObject *parent);
    ~ListWrapper();

    static ListWrapper *findWrapper(QObject *qobj, QList<QObject *> *qlist);

    PyObject *_py_list;
};


#endif
