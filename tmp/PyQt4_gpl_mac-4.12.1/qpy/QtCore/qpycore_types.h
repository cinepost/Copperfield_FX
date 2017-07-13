// This defines the interfaces for the meta-type used by PyQt.
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


#ifndef _QPYCORE_TYPES_H
#define _QPYCORE_TYPES_H


#include <Python.h>

#include <QByteArray>
#include <QList>
#include <QMetaObject>

#include "qpycore_chimera.h"
#include "qpycore_pyqtproperty.h"
#include "qpycore_qtlib.h"
#include "qpycore_sip.h"


// This describes a slot.
struct qpycore_slot
{
    // The slot itself.
    sipSlot sip_slot;

    // The parsed signature.
    const Chimera::Signature *signature;
};


// This describes a dynamic meta-object.
struct qpycore_metaobject
{
#if QT_VERSION >= 0x050000
    // The meta-object built by QMetaObjectBuilder.
    QMetaObject *mo;
#define QPYCORE_QMETAOBJECT(qo) ((qo)->mo)
#else
    // The meta-object.
    QMetaObject mo;
#define QPYCORE_QMETAOBJECT(qo) (&(qo)->mo)

    // The meta-object string data.
    QByteArray str_data;

#if QT_VERSION >= 0x040600
    QMetaObjectExtraData ed;
#endif
#endif

    // The list of properties.
    QList<qpycore_pyqtProperty *> pprops;

    // The list of slots.
    QList<qpycore_slot> pslots;

    // The number of signals.
    int nr_signals;
};


extern "C" {

/*
 * The meta-type of a PyQt wrapper type.
 */
typedef struct _pyqtWrapperType {
    /*
     * The super-meta-type.  This must be first in the structure so that it can
     * be cast to a sipWrapperType *.
     */
    sipWrapperType super;

    /*
     * The type's dynamic metaobject (for QObject sub-classes) created by
     * introspecting the Python type.
     */
    qpycore_metaobject *metaobject;
} pyqtWrapperType;


extern PyTypeObject qpycore_pyqtWrapperType_Type;

}


#endif
