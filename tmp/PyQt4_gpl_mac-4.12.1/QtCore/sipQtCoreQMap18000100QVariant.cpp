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

#line 139 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qmap.sip"
#include <qmap.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQMap18000100QVariant.cpp"

#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvariant.sip"
#include <qvariant.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQMap18000100QVariant.cpp"
#line 265 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvariant.sip"
#include <qvariant.h>
#line 36 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQMap18000100QVariant.cpp"


extern "C" {static void assign_QMap_1800_0100QVariant(void *, SIP_SSIZE_T, const void *);}
static void assign_QMap_1800_0100QVariant(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QMap<int, ::QVariant> *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QMap<int, ::QVariant> *>(sipSrc);
}


extern "C" {static void *array_QMap_1800_0100QVariant(SIP_SSIZE_T);}
static void *array_QMap_1800_0100QVariant(SIP_SSIZE_T sipNrElem)
{
    return new QMap<int, ::QVariant>[sipNrElem];
}


extern "C" {static void *copy_QMap_1800_0100QVariant(const void *, SIP_SSIZE_T);}
static void *copy_QMap_1800_0100QVariant(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QMap<int, ::QVariant>(reinterpret_cast<const QMap<int, ::QVariant> *>(sipSrc)[sipSrcIdx]);
}


/* Call the mapped type's destructor. */
extern "C" {static void release_QMap_1800_0100QVariant(void *, int);}
static void release_QMap_1800_0100QVariant(void *ptr, int)
{
    Py_BEGIN_ALLOW_THREADS
    delete reinterpret_cast<QMap<int, ::QVariant> *>(ptr);
    Py_END_ALLOW_THREADS
}



extern "C" {static int convertTo_QMap_1800_0100QVariant(PyObject *, void **, int *, PyObject *);}
static int convertTo_QMap_1800_0100QVariant(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
    QMap<int, ::QVariant> **sipCppPtr = reinterpret_cast<QMap<int, ::QVariant> **>(sipCppPtrV);

#line 190 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qmap.sip"
    PyObject *kobj, *tobj;
    SIP_SSIZE_T i = 0;

    // Check the type if that is all that is required.
    if (sipIsErr == NULL)
    {
        if (!PyDict_Check(sipPy))
            return 0;

        while (PyDict_Next(sipPy, &i, &kobj, &tobj))
            if (!sipCanConvertToType(tobj, sipType_QVariant, SIP_NOT_NONE))
                return 0;

        return 1;
    }

    QMap<int, QVariant> *qm = new QMap<int, QVariant>;
 
    while (PyDict_Next(sipPy, &i, &kobj, &tobj))
    {
        int state, k = SIPLong_AsLong(kobj);
        QVariant *t = reinterpret_cast<QVariant *>(sipConvertToType(tobj, sipType_QVariant, sipTransferObj, SIP_NOT_NONE, &state, sipIsErr));
 
        if (*sipIsErr)
        {
            sipReleaseType(t, sipType_QVariant, state);

            delete qm;
            return 0;
        }

        qm->insert(k, *t);

        sipReleaseType(t, sipType_QVariant, state);
    }
 
    *sipCppPtr = qm;
 
    return sipGetState(sipTransferObj);
#line 116 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQMap18000100QVariant.cpp"
}


extern "C" {static PyObject *convertFrom_QMap_1800_0100QVariant(void *, PyObject *);}
static PyObject *convertFrom_QMap_1800_0100QVariant(void *sipCppV, PyObject *sipTransferObj)
{
   QMap<int, ::QVariant> *sipCpp = reinterpret_cast<QMap<int, ::QVariant> *>(sipCppV);

#line 143 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qmap.sip"
    // Create the dictionary.
    PyObject *d = PyDict_New();

    if (!d)
        return NULL;

    // Set the dictionary elements.
    QMap<int, QVariant>::const_iterator i = sipCpp->constBegin();

    while (i != sipCpp->constEnd())
    {
        QVariant *t = new QVariant(i.value());

        PyObject *kobj = SIPLong_FromLong(i.key());
        PyObject *tobj = sipConvertFromNewType(t, sipType_QVariant, sipTransferObj);

        if (kobj == NULL || tobj == NULL || PyDict_SetItem(d, kobj, tobj) < 0)
        {
            Py_DECREF(d);

            if (kobj)
            {
                Py_DECREF(kobj);
            }

            if (tobj)
            {
                Py_DECREF(tobj);
            }
            else
            {
                delete t;
            }

            return NULL;
        }

        Py_DECREF(kobj);
        Py_DECREF(tobj);

        ++i;
    }

    return d;
#line 170 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQMap18000100QVariant.cpp"
}


sipMappedTypeDef sipTypeDef_QtCore_QMap_1800_0100QVariant = {
    {
        -1,
        0,
        0,
        SIP_TYPE_MAPPED,
        sipNameNr_12692,     /* QMap<int,QVariant> */
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
    assign_QMap_1800_0100QVariant,
    array_QMap_1800_0100QVariant,
    copy_QMap_1800_0100QVariant,
    release_QMap_1800_0100QVariant,
    convertTo_QMap_1800_0100QVariant,
    convertFrom_QMap_1800_0100QVariant
};
