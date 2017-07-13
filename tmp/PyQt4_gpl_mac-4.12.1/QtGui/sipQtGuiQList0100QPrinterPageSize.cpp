/*
 * Interface wrapper code.
 *
 * Generated by SIP 4.19.3
 *
 * Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
 * 
 * This file is part of PyQt4.
 * 
 * This file may be used under the terms of the GNU General Public License
 * version 3.0 as published by the Free Software Foundation and appearing in
 * the file LICENSE included in the packaging of this file.  Please review the
 * following information to ensure the GNU General Public License version 3.0
 * requirements will be met: http://www.gnu.org/copyleft/gpl.html.
 * 
 * If you do not wish to use this file under the terms of the GPL version 3.0
 * then you may purchase a commercial license.  For more information contact
 * info@riverbankcomputing.com.
 * 
 * This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
 * WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
 */

#include "sipAPIQtGui.h"

#line 128 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qprinterinfo.sip"
#include <qlist.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQList0100QPrinterPageSize.cpp"

#line 210 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qprinter.sip"
#include <qprinter.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQList0100QPrinterPageSize.cpp"


extern "C" {static void assign_QList_0100QPrinter_PageSize(void *, SIP_SSIZE_T, const void *);}
static void assign_QList_0100QPrinter_PageSize(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast< ::QList< ::QPrinter::PageSize> *>(sipDst)[sipDstIdx] = *reinterpret_cast<const  ::QList< ::QPrinter::PageSize> *>(sipSrc);
}


extern "C" {static void *array_QList_0100QPrinter_PageSize(SIP_SSIZE_T);}
static void *array_QList_0100QPrinter_PageSize(SIP_SSIZE_T sipNrElem)
{
    return new  ::QList< ::QPrinter::PageSize>[sipNrElem];
}


extern "C" {static void *copy_QList_0100QPrinter_PageSize(const void *, SIP_SSIZE_T);}
static void *copy_QList_0100QPrinter_PageSize(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new  ::QList< ::QPrinter::PageSize>(reinterpret_cast<const  ::QList< ::QPrinter::PageSize> *>(sipSrc)[sipSrcIdx]);
}


/* Call the mapped type's destructor. */
extern "C" {static void release_QList_0100QPrinter_PageSize(void *, int);}
static void release_QList_0100QPrinter_PageSize(void *ptr, int)
{
    Py_BEGIN_ALLOW_THREADS
    delete reinterpret_cast< ::QList< ::QPrinter::PageSize> *>(ptr);
    Py_END_ALLOW_THREADS
}



extern "C" {static int convertTo_QList_0100QPrinter_PageSize(PyObject *, void **, int *, PyObject *);}
static int convertTo_QList_0100QPrinter_PageSize(PyObject *sipPy,void **,int *sipIsErr,PyObject *)
{
#line 156 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qprinterinfo.sip"
    if (sipIsErr == NULL)
    {
        // We don't support passing the type as an argument as it isn't
        // currently needed.
        PyErr_SetString(PyExc_NotImplementedError, "converting to QList<QPrinter::PageSize> is unsupported");

        return 0;
    }

    // Keep the compiler quiet.
    sipPy = NULL;
    return 0;
#line 84 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQList0100QPrinterPageSize.cpp"
}


extern "C" {static PyObject *convertFrom_QList_0100QPrinter_PageSize(void *, PyObject *);}
static PyObject *convertFrom_QList_0100QPrinter_PageSize(void *sipCppV, PyObject *)
{
    ::QList< ::QPrinter::PageSize> *sipCpp = reinterpret_cast< ::QList< ::QPrinter::PageSize> *>(sipCppV);

#line 132 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qprinterinfo.sip"
    // Create the list.
    PyObject *l = PyList_New(sipCpp->size());

    if (!l)
        return 0;

    // Set the list elements.
    for (int i = 0; i < sipCpp->size(); ++i)
    {
        PyObject *obj = sipConvertFromEnum(sipCpp->at(i), sipType_QPrinter_PageSize);

        if (!obj)
        {
            Py_DECREF(l);
            return 0;
        }

        PyList_SET_ITEM(l, i, obj);
    }

    return l;
#line 115 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQList0100QPrinterPageSize.cpp"
}


sipMappedTypeDef sipTypeDef_QtGui_QList_0100QPrinter_PageSize = {
    {
        -1,
        0,
        0,
        SIP_TYPE_MAPPED,
        sipNameNr_14424,     /* QList<QPrinter::PageSize> */
        {0},
        0
    },
    {
        -1,
        {0, 0, 1},
        0, 0,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
    },
    assign_QList_0100QPrinter_PageSize,
    array_QList_0100QPrinter_PageSize,
    copy_QList_0100QPrinter_PageSize,
    release_QList_0100QPrinter_PageSize,
    convertTo_QList_0100QPrinter_PageSize,
    convertFrom_QList_0100QPrinter_PageSize
};
