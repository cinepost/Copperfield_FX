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

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvector.sip"
#include <qvector.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQVector0100QTextLength.cpp"

#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qtextformat.sip"
#include <qtextformat.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQVector0100QTextLength.cpp"


extern "C" {static void assign_QVector_0100QTextLength(void *, SIP_SSIZE_T, const void *);}
static void assign_QVector_0100QTextLength(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QVector< ::QTextLength> *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QVector< ::QTextLength> *>(sipSrc);
}


extern "C" {static void *array_QVector_0100QTextLength(SIP_SSIZE_T);}
static void *array_QVector_0100QTextLength(SIP_SSIZE_T sipNrElem)
{
    return new QVector< ::QTextLength>[sipNrElem];
}


extern "C" {static void *copy_QVector_0100QTextLength(const void *, SIP_SSIZE_T);}
static void *copy_QVector_0100QTextLength(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QVector< ::QTextLength>(reinterpret_cast<const QVector< ::QTextLength> *>(sipSrc)[sipSrcIdx]);
}


/* Call the mapped type's destructor. */
extern "C" {static void release_QVector_0100QTextLength(void *, int);}
static void release_QVector_0100QTextLength(void *ptr, int)
{
    Py_BEGIN_ALLOW_THREADS
    delete reinterpret_cast<QVector< ::QTextLength> *>(ptr);
    Py_END_ALLOW_THREADS
}



extern "C" {static int convertTo_QVector_0100QTextLength(PyObject *, void **, int *, PyObject *);}
static int convertTo_QVector_0100QTextLength(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
    QVector< ::QTextLength> **sipCppPtr = reinterpret_cast<QVector< ::QTextLength> **>(sipCppPtrV);

#line 59 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvector.sip"
    // Check the type if that is all that is required.
    if (sipIsErr == NULL)
    {
        if (!PyList_Check(sipPy))
            return 0;

        for (SIP_SSIZE_T i = 0; i < PyList_GET_SIZE(sipPy); ++i)
            if (!sipCanConvertToType(PyList_GET_ITEM(sipPy, i), sipType_QTextLength, SIP_NOT_NONE))
                return 0;

        return 1;
    }

    QVector<QTextLength> *qv = new QVector<QTextLength>;
 
    for (SIP_SSIZE_T i = 0; i < PyList_GET_SIZE(sipPy); ++i)
    {
        int state;
        QTextLength *t = reinterpret_cast<QTextLength *>(sipConvertToType(PyList_GET_ITEM(sipPy, i), sipType_QTextLength, sipTransferObj, SIP_NOT_NONE, &state, sipIsErr));
 
        if (*sipIsErr)
        {
            sipReleaseType(t, sipType_QTextLength, state);

            delete qv;
            return 0;
        }

        qv->append(*t);

        sipReleaseType(t, sipType_QTextLength, state);
    }
 
    *sipCppPtr = qv;
 
    return sipGetState(sipTransferObj);
#line 110 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQVector0100QTextLength.cpp"
}


extern "C" {static PyObject *convertFrom_QVector_0100QTextLength(void *, PyObject *);}
static PyObject *convertFrom_QVector_0100QTextLength(void *sipCppV, PyObject *sipTransferObj)
{
   QVector< ::QTextLength> *sipCpp = reinterpret_cast<QVector< ::QTextLength> *>(sipCppV);

#line 32 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvector.sip"
    // Create the list.
    PyObject *l;

    if ((l = PyList_New(sipCpp->size())) == NULL)
        return NULL;

    // Set the list elements.
    for (int i = 0; i < sipCpp->size(); ++i)
    {
        QTextLength *t = new QTextLength(sipCpp->at(i));
        PyObject *tobj;

        if ((tobj = sipConvertFromNewType(t, sipType_QTextLength, sipTransferObj)) == NULL)
        {
            Py_DECREF(l);
            delete t;

            return NULL;
        }

        PyList_SET_ITEM(l, i, tobj);
    }

    return l;
#line 144 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQVector0100QTextLength.cpp"
}


sipMappedTypeDef sipTypeDef_QtGui_QVector_0100QTextLength = {
    {
        -1,
        0,
        0,
        SIP_TYPE_MAPPED,
        sipNameNr_25879,     /* QVector<QTextLength> */
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
    assign_QVector_0100QTextLength,
    array_QVector_0100QTextLength,
    copy_QVector_0100QTextLength,
    release_QVector_0100QTextLength,
    convertTo_QVector_0100QTextLength,
    convertFrom_QVector_0100QTextLength
};
