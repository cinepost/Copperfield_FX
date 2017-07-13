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

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qlist.sip"
#include <qlist.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQList0100QTextBlock.cpp"

#line 129 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qtextobject.sip"
#include <qtextobject.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQList0100QTextBlock.cpp"


extern "C" {static void assign_QList_0100QTextBlock(void *, SIP_SSIZE_T, const void *);}
static void assign_QList_0100QTextBlock(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QList< ::QTextBlock> *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QList< ::QTextBlock> *>(sipSrc);
}


extern "C" {static void *array_QList_0100QTextBlock(SIP_SSIZE_T);}
static void *array_QList_0100QTextBlock(SIP_SSIZE_T sipNrElem)
{
    return new QList< ::QTextBlock>[sipNrElem];
}


extern "C" {static void *copy_QList_0100QTextBlock(const void *, SIP_SSIZE_T);}
static void *copy_QList_0100QTextBlock(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QList< ::QTextBlock>(reinterpret_cast<const QList< ::QTextBlock> *>(sipSrc)[sipSrcIdx]);
}


/* Call the mapped type's destructor. */
extern "C" {static void release_QList_0100QTextBlock(void *, int);}
static void release_QList_0100QTextBlock(void *ptr, int)
{
    Py_BEGIN_ALLOW_THREADS
    delete reinterpret_cast<QList< ::QTextBlock> *>(ptr);
    Py_END_ALLOW_THREADS
}



extern "C" {static int convertTo_QList_0100QTextBlock(PyObject *, void **, int *, PyObject *);}
static int convertTo_QList_0100QTextBlock(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
    QList< ::QTextBlock> **sipCppPtr = reinterpret_cast<QList< ::QTextBlock> **>(sipCppPtrV);

#line 59 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qlist.sip"
    SIP_SSIZE_T len;

    // Check the type if that is all that is required.
    if (sipIsErr == NULL)
    {
        if (!PySequence_Check(sipPy) || (len = PySequence_Size(sipPy)) < 0)
            return 0;

        for (SIP_SSIZE_T i = 0; i < len; ++i)
        {
            PyObject *itm = PySequence_ITEM(sipPy, i);
            bool ok = (itm && sipCanConvertToType(itm, sipType_QTextBlock, SIP_NOT_NONE));

            Py_XDECREF(itm);

            if (!ok)
                return 0;
        }

        return 1;
    }

    QList<QTextBlock> *ql = new QList<QTextBlock>;
    len = PySequence_Size(sipPy);
 
    for (SIP_SSIZE_T i = 0; i < len; ++i)
    {
        PyObject *itm = PySequence_ITEM(sipPy, i);
        int state;
        QTextBlock *t = reinterpret_cast<QTextBlock *>(sipConvertToType(itm, sipType_QTextBlock, sipTransferObj, SIP_NOT_NONE, &state, sipIsErr));

        Py_DECREF(itm);
 
        if (*sipIsErr)
        {
            sipReleaseType(t, sipType_QTextBlock, state);

            delete ql;
            return 0;
        }

        ql->append(*t);

        sipReleaseType(t, sipType_QTextBlock, state);
    }
 
    *sipCppPtr = ql;
 
    return sipGetState(sipTransferObj);
#line 123 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQList0100QTextBlock.cpp"
}


extern "C" {static PyObject *convertFrom_QList_0100QTextBlock(void *, PyObject *);}
static PyObject *convertFrom_QList_0100QTextBlock(void *sipCppV, PyObject *sipTransferObj)
{
   QList< ::QTextBlock> *sipCpp = reinterpret_cast<QList< ::QTextBlock> *>(sipCppV);

#line 32 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qlist.sip"
    // Create the list.
    PyObject *l;

    if ((l = PyList_New(sipCpp->size())) == NULL)
        return NULL;

    // Set the list elements.
    for (int i = 0; i < sipCpp->size(); ++i)
    {
        QTextBlock *t = new QTextBlock(sipCpp->at(i));
        PyObject *tobj;

        if ((tobj = sipConvertFromNewType(t, sipType_QTextBlock, sipTransferObj)) == NULL)
        {
            Py_DECREF(l);
            delete t;

            return NULL;
        }

        PyList_SET_ITEM(l, i, tobj);
    }

    return l;
#line 157 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQList0100QTextBlock.cpp"
}


sipMappedTypeDef sipTypeDef_QtGui_QList_0100QTextBlock = {
    {
        -1,
        0,
        0,
        SIP_TYPE_MAPPED,
        sipNameNr_39123,     /* QList<QTextBlock> */
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
    assign_QList_0100QTextBlock,
    array_QList_0100QTextBlock,
    copy_QList_0100QTextBlock,
    release_QList_0100QTextBlock,
    convertTo_QList_0100QTextBlock,
    convertFrom_QList_0100QTextBlock
};
