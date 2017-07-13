// This defines access to the SIP helpers for the rest of the library.
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


#ifndef _QPYCORE_SIP_HELPERS_H
#define _QPYCORE_SIP_HELPERS_H


#include <Python.h>

#include "qpycore_chimera.h"
#include "qpycore_namespace.h"


QT_BEGIN_NAMESPACE
class QObject;
QT_END_NAMESPACE


// Forward declarations.
QObject *qpycore_find_signal(QObject *qtx, const char **sigp);
QObject *qpycore_create_universal_signal(QObject *qtx, const char **sigp);
QObject *qpycore_create_universal_slot(sipWrapper *tx, const char *sig,
        PyObject *rxObj, const char *slot, const char **member, int flags);
bool qpycore_emit(QObject *qtx, int signal_index,
        const Chimera::Signature *parsed_signature, const char *docstring,
        PyObject *sigargs);


#endif
