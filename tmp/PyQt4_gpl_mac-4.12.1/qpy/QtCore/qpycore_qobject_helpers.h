// This defines the interfaces of the helpers for QObject.
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


#ifndef _QPYCORE_QOBJECT_HELPERS_H
#define _QPYCORE_QOBJECT_HELPERS_H


#include <Python.h>

#include <QMetaObject>

#include "qpycore_namespace.h"
#include "qpycore_sip.h"


QT_BEGIN_NAMESPACE
class QObject;
QT_END_NAMESPACE


const QMetaObject *qpycore_qobject_metaobject(sipSimpleWrapper *pySelf,
        sipTypeDef *base);
int qpycore_qobject_qt_metacall(sipSimpleWrapper *pySelf, sipTypeDef *base,
        QMetaObject::Call _c, int _id, void **_a);
int qpycore_qobject_qt_metacast(sipSimpleWrapper *pySelf, sipTypeDef *base,
        const char *_clname);
QObject *qpycore_qobject_sender(QObject *obj);
int qpycore_qobject_receivers(QObject *obj, const char *signal, int nr);


#endif
