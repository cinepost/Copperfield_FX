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

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qmap.sip"
#include <qmap.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQMap0100QDate0100QTextCharFormat.cpp"

#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qdatetime.sip"
#include <qdatetime.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQMap0100QDate0100QTextCharFormat.cpp"
#line 336 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qtextformat.sip"
#include <qtextformat.h>
#line 36 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQMap0100QDate0100QTextCharFormat.cpp"


extern "C" {static void assign_QMap_0100QDate_0100QTextCharFormat(void *, SIP_SSIZE_T, const void *);}
static void assign_QMap_0100QDate_0100QTextCharFormat(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QMap< ::QDate, ::QTextCharFormat> *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QMap< ::QDate, ::QTextCharFormat> *>(sipSrc);
}


extern "C" {static void *array_QMap_0100QDate_0100QTextCharFormat(SIP_SSIZE_T);}
static void *array_QMap_0100QDate_0100QTextCharFormat(SIP_SSIZE_T sipNrElem)
{
    return new QMap< ::QDate, ::QTextCharFormat>[sipNrElem];
}


extern "C" {static void *copy_QMap_0100QDate_0100QTextCharFormat(const void *, SIP_SSIZE_T);}
static void *copy_QMap_0100QDate_0100QTextCharFormat(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QMap< ::QDate, ::QTextCharFormat>(reinterpret_cast<const QMap< ::QDate, ::QTextCharFormat> *>(sipSrc)[sipSrcIdx]);
}


/* Call the mapped type's destructor. */
extern "C" {static void release_QMap_0100QDate_0100QTextCharFormat(void *, int);}
static void release_QMap_0100QDate_0100QTextCharFormat(void *ptr, int)
{
    Py_BEGIN_ALLOW_THREADS
    delete reinterpret_cast<QMap< ::QDate, ::QTextCharFormat> *>(ptr);
    Py_END_ALLOW_THREADS
}



extern "C" {static int convertTo_QMap_0100QDate_0100QTextCharFormat(PyObject *, void **, int *, PyObject *);}
static int convertTo_QMap_0100QDate_0100QTextCharFormat(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
    QMap< ::QDate, ::QTextCharFormat> **sipCppPtr = reinterpret_cast<QMap< ::QDate, ::QTextCharFormat> **>(sipCppPtrV);

#line 84 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qmap.sip"
    PyObject *t1obj, *t2obj;
    SIP_SSIZE_T i = 0;

    // Check the type if that is all that is required.
    if (sipIsErr == NULL)
    {
        if (!PyDict_Check(sipPy))
            return 0;

        while (PyDict_Next(sipPy, &i, &t1obj, &t2obj))
        {
            if (!sipCanConvertToType(t1obj, sipType_QDate, SIP_NOT_NONE))
                return 0;

            if (!sipCanConvertToType(t2obj, sipType_QTextCharFormat, SIP_NOT_NONE))
                return 0;
        } 

        return 1;
    }

    QMap<QDate, QTextCharFormat> *qm = new QMap<QDate, QTextCharFormat>;
 
    while (PyDict_Next(sipPy, &i, &t1obj, &t2obj))
    {
        int state1, state2;

        QDate *t1 = reinterpret_cast<QDate *>(sipConvertToType(t1obj, sipType_QDate, sipTransferObj, SIP_NOT_NONE, &state1, sipIsErr));
        QTextCharFormat *t2 = reinterpret_cast<QTextCharFormat *>(sipConvertToType(t2obj, sipType_QTextCharFormat, sipTransferObj, SIP_NOT_NONE, &state2, sipIsErr));
 
        if (*sipIsErr)
        {
            sipReleaseType(t1, sipType_QDate, state1);
            sipReleaseType(t2, sipType_QTextCharFormat, state2);

            delete qm;
            return 0;
        }

        qm->insert(*t1, *t2);

        sipReleaseType(t1, sipType_QDate, state1);
        sipReleaseType(t2, sipType_QTextCharFormat, state2);
    }
 
    *sipCppPtr = qm;
 
    return sipGetState(sipTransferObj);
#line 125 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQMap0100QDate0100QTextCharFormat.cpp"
}


extern "C" {static PyObject *convertFrom_QMap_0100QDate_0100QTextCharFormat(void *, PyObject *);}
static PyObject *convertFrom_QMap_0100QDate_0100QTextCharFormat(void *sipCppV, PyObject *sipTransferObj)
{
   QMap< ::QDate, ::QTextCharFormat> *sipCpp = reinterpret_cast<QMap< ::QDate, ::QTextCharFormat> *>(sipCppV);

#line 32 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qmap.sip"
    // Create the dictionary.
    PyObject *d = PyDict_New();

    if (!d)
        return NULL;

    // Set the dictionary elements.
    QMap<QDate, QTextCharFormat>::const_iterator i = sipCpp->constBegin();

    while (i != sipCpp->constEnd())
    {
        QDate *t1 = new QDate(i.key());
        QTextCharFormat *t2 = new QTextCharFormat(i.value());

        PyObject *t1obj = sipConvertFromNewType(t1, sipType_QDate, sipTransferObj);
        PyObject *t2obj = sipConvertFromNewType(t2, sipType_QTextCharFormat, sipTransferObj);

        if (t1obj == NULL || t2obj == NULL || PyDict_SetItem(d, t1obj, t2obj) < 0)
        {
            Py_DECREF(d);

            if (t1obj)
            {
                Py_DECREF(t1obj);
            }
            else
            {
                delete t1;
            }

            if (t2obj)
            {
                Py_DECREF(t2obj);
            }
            else
            {
                delete t2;
            }

            return NULL;
        }

        Py_DECREF(t1obj);
        Py_DECREF(t2obj);

        ++i;
    }

    return d;
#line 184 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQMap0100QDate0100QTextCharFormat.cpp"
}


sipMappedTypeDef sipTypeDef_QtGui_QMap_0100QDate_0100QTextCharFormat = {
    {
        -1,
        0,
        0,
        SIP_TYPE_MAPPED,
        sipNameNr_10972,     /* QMap<QDate,QTextCharFormat> */
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
    assign_QMap_0100QDate_0100QTextCharFormat,
    array_QMap_0100QDate_0100QTextCharFormat,
    copy_QMap_0100QDate_0100QTextCharFormat,
    release_QMap_0100QDate_0100QTextCharFormat,
    convertTo_QMap_0100QDate_0100QTextCharFormat,
    convertFrom_QMap_0100QDate_0100QTextCharFormat
};
