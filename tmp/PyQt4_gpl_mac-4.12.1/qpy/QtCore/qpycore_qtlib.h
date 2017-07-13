// This defines the interfaces to the legacy signal/slot support from sip v4.
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


#ifndef _QPYCORE_QTLIB_H
#define _QPYCORE_QTLIB_H


#include <Python.h>

#include <sip.h>


#if SIP_VERSION >= 0x050000

// A Python method's component parts.  This allows us to re-create the method
// without changing the reference counts of the components.
struct sipPyMethod
{
    // The function.
    PyObject *mfunc;

    // Self if it is a bound method.
    PyObject *mself;

#if PY_MAJOR_VERSION < 3
    // The class.
    PyObject *mclass;
#endif
};


// A slot (in the Qt, rather than Python, sense).
struct sipSlot
{
    // Name if a Qt or Python signal.
    char *name;

    // Signal or Qt slot object.
    PyObject *pyobj;

    // Python slot method, pyobj is 0. */
    sipPyMethod meth;

    // A weak reference to the slot, Py_True if pyobj has an extra reference.
    PyObject *weakSlot;
};

#endif


void qtlib_free_slot(sipSlot *slot);
PyObject *qtlib_invoke_slot(const sipSlot *slot, PyObject *sigargs,
        int no_receiver_check);
bool qtlib_same_slot(const sipSlot *sp, PyObject *rxObj, const char *slot);
int qtlib_save_slot(sipSlot *sp, PyObject *rxObj, const char *slot);


#endif
