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

#line 247 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvector.sip"
#include <qvector.h>
#include <qpair.h>
#line 30 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQVector0600QPair24000100QColor.cpp"

#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qcolor.sip"
#include <qcolor.h>
#line 34 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQVector0600QPair24000100QColor.cpp"


extern "C" {static void assign_QVector_0600QPair_2400_0100QColor(void *, SIP_SSIZE_T, const void *);}
static void assign_QVector_0600QPair_2400_0100QColor(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QVector<QPair< ::qreal,QColor> > *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QVector<QPair< ::qreal,QColor> > *>(sipSrc);
}


extern "C" {static void *array_QVector_0600QPair_2400_0100QColor(SIP_SSIZE_T);}
static void *array_QVector_0600QPair_2400_0100QColor(SIP_SSIZE_T sipNrElem)
{
    return new QVector<QPair< ::qreal,QColor> >[sipNrElem];
}


extern "C" {static void *copy_QVector_0600QPair_2400_0100QColor(const void *, SIP_SSIZE_T);}
static void *copy_QVector_0600QPair_2400_0100QColor(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QVector<QPair< ::qreal,QColor> >(reinterpret_cast<const QVector<QPair< ::qreal,QColor> > *>(sipSrc)[sipSrcIdx]);
}


/* Call the mapped type's destructor. */
extern "C" {static void release_QVector_0600QPair_2400_0100QColor(void *, int);}
static void release_QVector_0600QPair_2400_0100QColor(void *ptr, int)
{
    Py_BEGIN_ALLOW_THREADS
    delete reinterpret_cast<QVector<QPair< ::qreal,QColor> > *>(ptr);
    Py_END_ALLOW_THREADS
}



extern "C" {static int convertTo_QVector_0600QPair_2400_0100QColor(PyObject *, void **, int *, PyObject *);}
static int convertTo_QVector_0600QPair_2400_0100QColor(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
    QVector<QPair< ::qreal,QColor> > **sipCppPtr = reinterpret_cast<QVector<QPair< ::qreal,QColor> > **>(sipCppPtrV);

#line 280 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvector.sip"
    // Check the type if that is all that is required.
    if (sipIsErr == NULL)
    {
        if (!PyList_Check(sipPy))
            return 0;

        for (SIP_SSIZE_T i = 0; i < PyList_GET_SIZE(sipPy); ++i)
        {
            PyObject *tup = PyList_GET_ITEM(sipPy, i);

            if (PyTuple_Size(tup) != 2)
                return 0;

            if (!sipCanConvertToType(PyTuple_GET_ITEM(tup, 1), sipType_QColor, SIP_NOT_NONE))
                return 0;
        }

        return 1;
    }

    QVector<QPair<qreal, QColor> > *qv = new QVector<QPair<qreal, QColor> >;
 
    for (SIP_SSIZE_T i = 0; i < PyList_GET_SIZE(sipPy); ++i)
    {
        PyObject *tup = PyList_GET_ITEM(sipPy, i);
        int state;
        QColor *s;
        QPair<qreal, QColor> p;

        p.first = PyFloat_AsDouble(PyTuple_GET_ITEM(tup, 0));

        s = reinterpret_cast<QColor *>(sipConvertToType(PyTuple_GET_ITEM(tup, 1), sipType_QColor, sipTransferObj, SIP_NOT_NONE, &state, sipIsErr));
 
        if (*sipIsErr)
        {
            sipReleaseType(s, sipType_QColor, state);

            delete qv;
            return 0;
        }

        p.second = *s;

        qv->append(p);

        sipReleaseType(s, sipType_QColor, state);
    }

    *sipCppPtr = qv;

    return sipGetState(sipTransferObj);
#line 126 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQVector0600QPair24000100QColor.cpp"
}


extern "C" {static PyObject *convertFrom_QVector_0600QPair_2400_0100QColor(void *, PyObject *);}
static PyObject *convertFrom_QVector_0600QPair_2400_0100QColor(void *sipCppV, PyObject *sipTransferObj)
{
   QVector<QPair< ::qreal,QColor> > *sipCpp = reinterpret_cast<QVector<QPair< ::qreal,QColor> > *>(sipCppV);

#line 252 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qvector.sip"
    // Create the list.
    PyObject *l;

    if ((l = PyList_New(sipCpp->size())) == NULL)
        return NULL;

    // Set the list elements.
    for (int i = 0; i < sipCpp->size(); ++i)
    {
        const QPair<qreal, QColor> &p = sipCpp->at(i);
        QColor *pt = new QColor(p.second);
        PyObject *pobj;

        if ((pobj = sipBuildResult(NULL, "(dN)", p.first, pt, sipType_QColor, sipTransferObj)) == NULL)
        {
            Py_DECREF(l);
            delete pt;

            return NULL;
        }

        PyList_SET_ITEM(l, i, pobj);
    }

    return l;
#line 161 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQVector0600QPair24000100QColor.cpp"
}


sipMappedTypeDef sipTypeDef_QtGui_QVector_0600QPair_2400_0100QColor = {
    {
        -1,
        0,
        0,
        SIP_TYPE_MAPPED,
        sipNameNr_8521,     /* QVector<QPair<qreal,QColor> > */
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
    assign_QVector_0600QPair_2400_0100QColor,
    array_QVector_0600QPair_2400_0100QColor,
    copy_QVector_0600QPair_2400_0100QColor,
    release_QVector_0600QPair_2400_0100QColor,
    convertTo_QVector_0600QPair_2400_0100QColor,
    convertFrom_QVector_0600QPair_2400_0100QColor
};
