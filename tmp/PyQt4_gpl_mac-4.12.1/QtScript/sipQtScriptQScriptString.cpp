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

#include "sipAPIQtScript.h"

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptstring.sip"
#include <qscriptstring.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptString.cpp"

#line 27 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qstring.sip"
#include <qstring.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptString.cpp"
#line 32 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptstring.sip"
#include <QHash>
#line 36 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptString.cpp"


PyDoc_STRVAR(doc_QScriptString_isValid, "isValid(self) -> bool");

extern "C" {static PyObject *meth_QScriptString_isValid(PyObject *, PyObject *);}
static PyObject *meth_QScriptString_isValid(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QScriptString *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QScriptString, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->isValid();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QScriptString, sipName_isValid, doc_QScriptString_isValid);

    return NULL;
}


PyDoc_STRVAR(doc_QScriptString_toString, "toString(self) -> str");

extern "C" {static PyObject *meth_QScriptString_toString(PyObject *, PyObject *);}
static PyObject *meth_QScriptString_toString(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QScriptString *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QScriptString, &sipCpp))
        {
             ::QString*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QString(sipCpp->toString());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QScriptString, sipName_toString, doc_QScriptString_toString);

    return NULL;
}


PyDoc_STRVAR(doc_QScriptString_toArrayIndex, "toArrayIndex(self) -> Tuple[int, bool]");

extern "C" {static PyObject *meth_QScriptString_toArrayIndex(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QScriptString_toArrayIndex(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
        bool a0;
        const  ::QScriptString *sipCpp;

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, NULL, NULL, "B", &sipSelf, sipType_QScriptString, &sipCpp))
        {
             ::quint32 sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->toArrayIndex(&a0);
            Py_END_ALLOW_THREADS

            return sipBuildResult(0,"(ub)",sipRes,a0);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QScriptString, sipName_toArrayIndex, doc_QScriptString_toArrayIndex);

    return NULL;
}


extern "C" {static PyObject *slot_QScriptString___ne__(PyObject *,PyObject *);}
static PyObject *slot_QScriptString___ne__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QScriptString *sipCpp = reinterpret_cast< ::QScriptString *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptString));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QScriptString* a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J9", sipType_QScriptString, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp-> ::QScriptString::operator!=(*a0);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtScript, ne_slot, sipType_QScriptString, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_QScriptString___eq__(PyObject *,PyObject *);}
static PyObject *slot_QScriptString___eq__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QScriptString *sipCpp = reinterpret_cast< ::QScriptString *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptString));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QScriptString* a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J9", sipType_QScriptString, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp-> ::QScriptString::operator==(*a0);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtScript, eq_slot, sipType_QScriptString, sipSelf, sipArg);
}


extern "C" {static long slot_QScriptString___hash__(PyObject *);}
static long slot_QScriptString___hash__(PyObject *sipSelf)
{
     ::QScriptString *sipCpp = reinterpret_cast< ::QScriptString *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptString));

    if (!sipCpp)
        return 0;


    {
        {
            long sipRes = 0;

#line 42 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptstring.sip"
        sipRes = qHash(*sipCpp);
#line 213 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptString.cpp"

            return sipRes;
        }
    }

    return 0;
}


/* Call the instance's destructor. */
extern "C" {static void release_QScriptString(void *, int);}
static void release_QScriptString(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast< ::QScriptString *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void assign_QScriptString(void *, SIP_SSIZE_T, const void *);}
static void assign_QScriptString(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast< ::QScriptString *>(sipDst)[sipDstIdx] = *reinterpret_cast<const  ::QScriptString *>(sipSrc);
}


extern "C" {static void *array_QScriptString(SIP_SSIZE_T);}
static void *array_QScriptString(SIP_SSIZE_T sipNrElem)
{
    return new  ::QScriptString[sipNrElem];
}


extern "C" {static void *copy_QScriptString(const void *, SIP_SSIZE_T);}
static void *copy_QScriptString(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new  ::QScriptString(reinterpret_cast<const  ::QScriptString *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_QScriptString(sipSimpleWrapper *);}
static void dealloc_QScriptString(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_QScriptString(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_QScriptString(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QScriptString(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
     ::QScriptString *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QScriptString();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const  ::QScriptString* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J9", sipType_QScriptString, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QScriptString(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's Python slots. */
static sipPySlotDef slots_QScriptString[] = {
    {(void *)slot_QScriptString___ne__, ne_slot},
    {(void *)slot_QScriptString___eq__, eq_slot},
    {(void *)slot_QScriptString___hash__, hash_slot},
    {0, (sipPySlotType)0}
};


static PyMethodDef methods_QScriptString[] = {
    {SIP_MLNAME_CAST(sipName_isValid), meth_QScriptString_isValid, METH_VARARGS, SIP_MLDOC_CAST(doc_QScriptString_isValid)},
    {SIP_MLNAME_CAST(sipName_toArrayIndex), (PyCFunction)meth_QScriptString_toArrayIndex, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QScriptString_toArrayIndex)},
    {SIP_MLNAME_CAST(sipName_toString), meth_QScriptString_toString, METH_VARARGS, SIP_MLDOC_CAST(doc_QScriptString_toString)}
};

PyDoc_STRVAR(doc_QScriptString, "\1QScriptString()\n"
    "QScriptString(QScriptString)");


static pyqt4ClassPluginDef plugin_QScriptString = {
    0,
    0,
    0
};


sipClassTypeDef sipTypeDef_QtScript_QScriptString = {
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_QScriptString,
        {0},
        &plugin_QScriptString
    },
    {
        sipNameNr_QScriptString,
        {0, 0, 1},
        3, methods_QScriptString,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QScriptString,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
    slots_QScriptString,
    init_type_QScriptString,
    0,
    0,
#if PY_MAJOR_VERSION >= 3
    0,
    0,
#else
    0,
    0,
    0,
    0,
#endif
    dealloc_QScriptString,
    assign_QScriptString,
    array_QScriptString,
    copy_QScriptString,
    release_QScriptString,
    0,
    0,
    0,
    0,
    0,
    0,
    0
};
