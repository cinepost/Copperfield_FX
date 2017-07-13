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

#include "sipAPIQtCore.h"

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qhash.sip"
#include <qhash.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQHash0100QString0100QVariant.cpp"

#line 68 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qstring.sip"
#include <qstring.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQHash0100QString0100QVariant.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvariant.sip"
#include <qvariant.h>
#line 36 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQHash0100QString0100QVariant.cpp"
#line 27 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qstring.sip"
#include <qstring.h>
#line 39 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQHash0100QString0100QVariant.cpp"
#line 265 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvariant.sip"
#include <qvariant.h>
#line 42 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQHash0100QString0100QVariant.cpp"


extern "C" {static void assign_QHash_0100QString_0100QVariant(void *, SIP_SSIZE_T, const void *);}
static void assign_QHash_0100QString_0100QVariant(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QHash< ::QString, ::QVariant> *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QHash< ::QString, ::QVariant> *>(sipSrc);
}


extern "C" {static void *array_QHash_0100QString_0100QVariant(SIP_SSIZE_T);}
static void *array_QHash_0100QString_0100QVariant(SIP_SSIZE_T sipNrElem)
{
    return new QHash< ::QString, ::QVariant>[sipNrElem];
}


extern "C" {static void *copy_QHash_0100QString_0100QVariant(const void *, SIP_SSIZE_T);}
static void *copy_QHash_0100QString_0100QVariant(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QHash< ::QString, ::QVariant>(reinterpret_cast<const QHash< ::QString, ::QVariant> *>(sipSrc)[sipSrcIdx]);
}


/* Call the mapped type's destructor. */
extern "C" {static void release_QHash_0100QString_0100QVariant(void *, int);}
static void release_QHash_0100QString_0100QVariant(void *ptr, int)
{
    Py_BEGIN_ALLOW_THREADS
    delete reinterpret_cast<QHash< ::QString, ::QVariant> *>(ptr);
    Py_END_ALLOW_THREADS
}



extern "C" {static int convertTo_QHash_0100QString_0100QVariant(PyObject *, void **, int *, PyObject *);}
static int convertTo_QHash_0100QString_0100QVariant(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
    QHash< ::QString, ::QVariant> **sipCppPtr = reinterpret_cast<QHash< ::QString, ::QVariant> **>(sipCppPtrV);

#line 84 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qhash.sip"
    PyObject *t1obj, *t2obj;
    SIP_SSIZE_T i = 0;

    // Check the type if that is all that is required.
    if (sipIsErr == NULL)
    {
        if (!PyDict_Check(sipPy))
            return 0;

        while (PyDict_Next(sipPy, &i, &t1obj, &t2obj))
        {
            if (!sipCanConvertToType(t1obj, sipType_QString, SIP_NOT_NONE))
                return 0;

            if (!sipCanConvertToType(t2obj, sipType_QVariant, SIP_NOT_NONE))
                return 0;
        } 

        return 1;
    }

    QHash<QString, QVariant> *qm = new QHash<QString, QVariant>;
 
    while (PyDict_Next(sipPy, &i, &t1obj, &t2obj))
    {
        int state1, state2;

        QString *t1 = reinterpret_cast<QString *>(sipConvertToType(t1obj, sipType_QString, sipTransferObj, SIP_NOT_NONE, &state1, sipIsErr));
        QVariant *t2 = reinterpret_cast<QVariant *>(sipConvertToType(t2obj, sipType_QVariant, sipTransferObj, SIP_NOT_NONE, &state2, sipIsErr));
 
        if (*sipIsErr)
        {
            sipReleaseType(t1, sipType_QString, state1);
            sipReleaseType(t2, sipType_QVariant, state2);

            delete qm;
            return 0;
        }

        qm->insert(*t1, *t2);

        sipReleaseType(t1, sipType_QString, state1);
        sipReleaseType(t2, sipType_QVariant, state2);
    }
 
    *sipCppPtr = qm;
 
    return sipGetState(sipTransferObj);
#line 131 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQHash0100QString0100QVariant.cpp"
}


extern "C" {static PyObject *convertFrom_QHash_0100QString_0100QVariant(void *, PyObject *);}
static PyObject *convertFrom_QHash_0100QString_0100QVariant(void *sipCppV, PyObject *sipTransferObj)
{
   QHash< ::QString, ::QVariant> *sipCpp = reinterpret_cast<QHash< ::QString, ::QVariant> *>(sipCppV);

#line 32 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qhash.sip"
    // Create the dictionary.
    PyObject *d = PyDict_New();

    if (!d)
        return NULL;

    // Set the dictionary elements.
    QHash<QString, QVariant>::const_iterator i = sipCpp->constBegin();

    while (i != sipCpp->constEnd())
    {
        QString *t1 = new QString(i.key());
        QVariant *t2 = new QVariant(i.value());

        PyObject *t1obj = sipConvertFromNewType(t1, sipType_QString, sipTransferObj);
        PyObject *t2obj = sipConvertFromNewType(t2, sipType_QVariant, sipTransferObj);

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
#line 190 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQHash0100QString0100QVariant.cpp"
}


sipMappedTypeDef sipTypeDef_QtCore_QHash_0100QString_0100QVariant = {
    {
        -1,
        0,
        0,
        SIP_TYPE_MAPPED,
        sipNameNr_5159,     /* QHash<QString,QVariant> */
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
    assign_QHash_0100QString_0100QVariant,
    array_QHash_0100QString_0100QVariant,
    copy_QHash_0100QString_0100QVariant,
    release_QHash_0100QString_0100QVariant,
    convertTo_QHash_0100QString_0100QVariant,
    convertFrom_QHash_0100QString_0100QVariant
};
