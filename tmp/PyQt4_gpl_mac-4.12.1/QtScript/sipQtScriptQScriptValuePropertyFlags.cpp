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

#line 34 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptvalue.sip"
#include <qscriptvalue.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptValuePropertyFlags.cpp"

#line 34 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtScript/qscriptvalue.sip"
#include <qscriptvalue.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptValuePropertyFlags.cpp"


extern "C" {static int slot_QScriptValue_PropertyFlags___bool__(PyObject *);}
static int slot_QScriptValue_PropertyFlags___bool__(PyObject *sipSelf)
{
     ::QScriptValue::PropertyFlags *sipCpp = reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptValue_PropertyFlags));

    if (!sipCpp)
        return -1;


    {
        {
            int sipRes = 0;

#line 381 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QScriptValue::PropertyFlags::Int() != 0);
#else
        sipRes = (sipCpp->operator int() != 0);
#endif
#line 55 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptValuePropertyFlags.cpp"

            return sipRes;
        }
    }

    return 0;
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___ne__(PyObject *,PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___ne__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QScriptValue::PropertyFlags *sipCpp = reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptValue_PropertyFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QScriptValue::PropertyFlags* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_QScriptValue_PropertyFlags, &a0, &a0State))
        {
            bool sipRes = 0;

#line 372 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QScriptValue::PropertyFlags::Int() != a0->operator QScriptValue::PropertyFlags::Int());
#else
        sipRes = (sipCpp->operator int() != a0->operator int());
#endif
#line 89 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptValuePropertyFlags.cpp"
            sipReleaseType(const_cast< ::QScriptValue::PropertyFlags *>(a0),sipType_QScriptValue_PropertyFlags,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtScript, ne_slot, sipType_QScriptValue_PropertyFlags, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___eq__(PyObject *,PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___eq__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QScriptValue::PropertyFlags *sipCpp = reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptValue_PropertyFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QScriptValue::PropertyFlags* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_QScriptValue_PropertyFlags, &a0, &a0State))
        {
            bool sipRes = 0;

#line 363 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QScriptValue::PropertyFlags::Int() == a0->operator QScriptValue::PropertyFlags::Int());
#else
        sipRes = (sipCpp->operator int() == a0->operator int());
#endif
#line 129 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptValuePropertyFlags.cpp"
            sipReleaseType(const_cast< ::QScriptValue::PropertyFlags *>(a0),sipType_QScriptValue_PropertyFlags,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtScript, eq_slot, sipType_QScriptValue_PropertyFlags, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___ixor__(PyObject *,PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___ixor__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QScriptValue_PropertyFlags)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QScriptValue::PropertyFlags *sipCpp = reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptValue_PropertyFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
#line 357 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
        *sipCpp = QScriptValue::PropertyFlags(*sipCpp ^ a0);
#line 168 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptValuePropertyFlags.cpp"

            Py_INCREF(sipSelf);
            return sipSelf;
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    PyErr_Clear();

    Py_INCREF(Py_NotImplemented);
    return Py_NotImplemented;
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___xor__(PyObject *,PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___xor__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QScriptValue::PropertyFlags* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QScriptValue_PropertyFlags, &a0, &a0State, &a1))
        {
             ::QScriptValue::PropertyFlags*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QScriptValue::PropertyFlags((*a0 ^ a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QScriptValue_PropertyFlags,a0State);

            return sipConvertFromNewType(sipRes,sipType_QScriptValue_PropertyFlags,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtScript, xor_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___ior__(PyObject *,PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___ior__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QScriptValue_PropertyFlags)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QScriptValue::PropertyFlags *sipCpp = reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptValue_PropertyFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
#line 351 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
        *sipCpp = QScriptValue::PropertyFlags(*sipCpp | a0);
#line 242 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptValuePropertyFlags.cpp"

            Py_INCREF(sipSelf);
            return sipSelf;
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    PyErr_Clear();

    Py_INCREF(Py_NotImplemented);
    return Py_NotImplemented;
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___or__(PyObject *,PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___or__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QScriptValue::PropertyFlags* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QScriptValue_PropertyFlags, &a0, &a0State, &a1))
        {
             ::QScriptValue::PropertyFlags*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QScriptValue::PropertyFlags((*a0 | a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QScriptValue_PropertyFlags,a0State);

            return sipConvertFromNewType(sipRes,sipType_QScriptValue_PropertyFlags,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtScript, or_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___iand__(PyObject *,PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___iand__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QScriptValue_PropertyFlags)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QScriptValue::PropertyFlags *sipCpp = reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptValue_PropertyFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp-> ::QScriptValue::PropertyFlags::operator&=(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(sipSelf);
            return sipSelf;
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    PyErr_Clear();

    Py_INCREF(Py_NotImplemented);
    return Py_NotImplemented;
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___and__(PyObject *,PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___and__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QScriptValue::PropertyFlags* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QScriptValue_PropertyFlags, &a0, &a0State, &a1))
        {
             ::QScriptValue::PropertyFlags*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QScriptValue::PropertyFlags((*a0 & a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QScriptValue_PropertyFlags,a0State);

            return sipConvertFromNewType(sipRes,sipType_QScriptValue_PropertyFlags,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtScript, and_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___invert__(PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___invert__(PyObject *sipSelf)
{
     ::QScriptValue::PropertyFlags *sipCpp = reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptValue_PropertyFlags));

    if (!sipCpp)
        return 0;


    {
        {
             ::QScriptValue::PropertyFlags*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QScriptValue::PropertyFlags(~(*sipCpp));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QScriptValue_PropertyFlags,NULL);
        }
    }

    return 0;
}


extern "C" {static PyObject *slot_QScriptValue_PropertyFlags___int__(PyObject *);}
static PyObject *slot_QScriptValue_PropertyFlags___int__(PyObject *sipSelf)
{
     ::QScriptValue::PropertyFlags *sipCpp = reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QScriptValue_PropertyFlags));

    if (!sipCpp)
        return 0;


    {
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = *sipCpp;
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    return 0;
}


/* Call the instance's destructor. */
extern "C" {static void release_QScriptValue_PropertyFlags(void *, int);}
static void release_QScriptValue_PropertyFlags(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void assign_QScriptValue_PropertyFlags(void *, SIP_SSIZE_T, const void *);}
static void assign_QScriptValue_PropertyFlags(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast< ::QScriptValue::PropertyFlags *>(sipDst)[sipDstIdx] = *reinterpret_cast<const  ::QScriptValue::PropertyFlags *>(sipSrc);
}


extern "C" {static void *array_QScriptValue_PropertyFlags(SIP_SSIZE_T);}
static void *array_QScriptValue_PropertyFlags(SIP_SSIZE_T sipNrElem)
{
    return new  ::QScriptValue::PropertyFlags[sipNrElem];
}


extern "C" {static void *copy_QScriptValue_PropertyFlags(const void *, SIP_SSIZE_T);}
static void *copy_QScriptValue_PropertyFlags(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new  ::QScriptValue::PropertyFlags(reinterpret_cast<const  ::QScriptValue::PropertyFlags *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_QScriptValue_PropertyFlags(sipSimpleWrapper *);}
static void dealloc_QScriptValue_PropertyFlags(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_QScriptValue_PropertyFlags(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_QScriptValue_PropertyFlags(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QScriptValue_PropertyFlags(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
     ::QScriptValue::PropertyFlags *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QScriptValue::PropertyFlags();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        int a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QScriptValue::PropertyFlags(a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const  ::QScriptValue::PropertyFlags* a0;
        int a0State = 0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J1", sipType_QScriptValue_PropertyFlags, &a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QScriptValue::PropertyFlags(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QScriptValue::PropertyFlags *>(a0),sipType_QScriptValue_PropertyFlags,a0State);

            return sipCpp;
        }
    }

    return NULL;
}


extern "C" {static int convertTo_QScriptValue_PropertyFlags(PyObject *, void **, int *, PyObject *);}
static int convertTo_QScriptValue_PropertyFlags(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
     ::QScriptValue::PropertyFlags **sipCppPtr = reinterpret_cast< ::QScriptValue::PropertyFlags **>(sipCppPtrV);

#line 390 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
// Allow an instance of the base enum whenever a QScriptValue::PropertyFlags is expected.

if (sipIsErr == NULL)
    return (PyObject_TypeCheck(sipPy, sipTypeAsPyTypeObject(sipType_QScriptValue_PropertyFlag)) ||
            sipCanConvertToType(sipPy, sipType_QScriptValue_PropertyFlags, SIP_NO_CONVERTORS));

if (PyObject_TypeCheck(sipPy, sipTypeAsPyTypeObject(sipType_QScriptValue_PropertyFlag)))
{
    *sipCppPtr = new QScriptValue::PropertyFlags(int(SIPLong_AsLong(sipPy)));

    return sipGetState(sipTransferObj);
}

*sipCppPtr = reinterpret_cast<QScriptValue::PropertyFlags *>(sipConvertToType(sipPy, sipType_QScriptValue_PropertyFlags, sipTransferObj, SIP_NO_CONVERTORS, 0, sipIsErr));

return 0;
#line 530 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtScript/sipQtScriptQScriptValuePropertyFlags.cpp"
}


/* Define this type's Python slots. */
static sipPySlotDef slots_QScriptValue_PropertyFlags[] = {
    {(void *)slot_QScriptValue_PropertyFlags___bool__, bool_slot},
    {(void *)slot_QScriptValue_PropertyFlags___ne__, ne_slot},
    {(void *)slot_QScriptValue_PropertyFlags___eq__, eq_slot},
    {(void *)slot_QScriptValue_PropertyFlags___ixor__, ixor_slot},
    {(void *)slot_QScriptValue_PropertyFlags___xor__, xor_slot},
    {(void *)slot_QScriptValue_PropertyFlags___ior__, ior_slot},
    {(void *)slot_QScriptValue_PropertyFlags___or__, or_slot},
    {(void *)slot_QScriptValue_PropertyFlags___iand__, iand_slot},
    {(void *)slot_QScriptValue_PropertyFlags___and__, and_slot},
    {(void *)slot_QScriptValue_PropertyFlags___invert__, invert_slot},
    {(void *)slot_QScriptValue_PropertyFlags___int__, int_slot},
    {0, (sipPySlotType)0}
};

PyDoc_STRVAR(doc_QScriptValue_PropertyFlags, "\1QScriptValue.PropertyFlags()\n"
    "QScriptValue.PropertyFlags(Union[QScriptValue.PropertyFlags, QScriptValue.PropertyFlag])\n"
    "QScriptValue.PropertyFlags(QScriptValue.PropertyFlags)");


static pyqt4ClassPluginDef plugin_QScriptValue_PropertyFlags = {
    0,
    1,
    0
};


sipClassTypeDef sipTypeDef_QtScript_QScriptValue_PropertyFlags = {
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_QScriptValue__PropertyFlags,
        {0},
        &plugin_QScriptValue_PropertyFlags
    },
    {
        sipNameNr_PropertyFlags,
        {21, 255, 0},
        0, 0,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QScriptValue_PropertyFlags,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
    slots_QScriptValue_PropertyFlags,
    init_type_QScriptValue_PropertyFlags,
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
    dealloc_QScriptValue_PropertyFlags,
    assign_QScriptValue_PropertyFlags,
    array_QScriptValue_PropertyFlags,
    copy_QScriptValue_PropertyFlags,
    release_QScriptValue_PropertyFlags,
    0,
    convertTo_QScriptValue_PropertyFlags,
    0,
    0,
    0,
    0,
    0
};
