// This is the definition of the various Chimera helpers.
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


#ifndef _QPYDECLARATIVECHIMERAHELPERS_H
#define _QPYDECLARATIVECHIMERAHELPERS_H


#include <Python.h>

#include <QVariant>


// Keep these in sync. with those defined in the Chimera class.
typedef bool (*FromQVariantFn)(const QVariant *, PyObject **);
typedef bool (*ToQVariantFn)(PyObject *, QVariant *, bool *);
typedef bool (*ToQVariantDataFn)(PyObject *, void *, int, bool *);


bool qpydeclarative_from_qvariant(const QVariant *varp, PyObject **objp);
bool qpydeclarative_to_qvariant(PyObject *obj, QVariant *varp, bool *okp);
bool qpydeclarative_to_qvariant_data(PyObject *obj, void *data, int metatype,
        bool *okp);


#endif
