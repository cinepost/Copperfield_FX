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

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qdiriterator.sip"
#include <qdiriterator.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQDirIteratorIteratorFlags.cpp"

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qdiriterator.sip"
#include <qdiriterator.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQDirIteratorIteratorFlags.cpp"


extern "C" {static int slot_QDirIterator_IteratorFlags___bool__(PyObject *);}
static int slot_QDirIterator_IteratorFlags___bool__(PyObject *sipSelf)
{
     ::QDirIterator::IteratorFlags *sipCpp = reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QDirIterator_IteratorFlags));

    if (!sipCpp)
        return -1;


    {
        {
            int sipRes = 0;

#line 381 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QDirIterator::IteratorFlags::Int() != 0);
#else
        sipRes = (sipCpp->operator int() != 0);
#endif
#line 55 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQDirIteratorIteratorFlags.cpp"

            return sipRes;
        }
    }

    return 0;
}


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___ne__(PyObject *,PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___ne__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QDirIterator::IteratorFlags *sipCpp = reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QDirIterator_IteratorFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QDirIterator::IteratorFlags* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_QDirIterator_IteratorFlags, &a0, &a0State))
        {
            bool sipRes = 0;

#line 372 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QDirIterator::IteratorFlags::Int() != a0->operator QDirIterator::IteratorFlags::Int());
#else
        sipRes = (sipCpp->operator int() != a0->operator int());
#endif
#line 89 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQDirIteratorIteratorFlags.cpp"
            sipReleaseType(const_cast< ::QDirIterator::IteratorFlags *>(a0),sipType_QDirIterator_IteratorFlags,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtCore, ne_slot, sipType_QDirIterator_IteratorFlags, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___eq__(PyObject *,PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___eq__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QDirIterator::IteratorFlags *sipCpp = reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QDirIterator_IteratorFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QDirIterator::IteratorFlags* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_QDirIterator_IteratorFlags, &a0, &a0State))
        {
            bool sipRes = 0;

#line 363 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QDirIterator::IteratorFlags::Int() == a0->operator QDirIterator::IteratorFlags::Int());
#else
        sipRes = (sipCpp->operator int() == a0->operator int());
#endif
#line 129 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQDirIteratorIteratorFlags.cpp"
            sipReleaseType(const_cast< ::QDirIterator::IteratorFlags *>(a0),sipType_QDirIterator_IteratorFlags,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtCore, eq_slot, sipType_QDirIterator_IteratorFlags, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___ixor__(PyObject *,PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___ixor__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QDirIterator_IteratorFlags)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QDirIterator::IteratorFlags *sipCpp = reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QDirIterator_IteratorFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
#line 357 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
        *sipCpp = QDirIterator::IteratorFlags(*sipCpp ^ a0);
#line 168 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQDirIteratorIteratorFlags.cpp"

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


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___xor__(PyObject *,PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___xor__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QDirIterator::IteratorFlags* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QDirIterator_IteratorFlags, &a0, &a0State, &a1))
        {
             ::QDirIterator::IteratorFlags*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QDirIterator::IteratorFlags((*a0 ^ a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QDirIterator_IteratorFlags,a0State);

            return sipConvertFromNewType(sipRes,sipType_QDirIterator_IteratorFlags,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtCore, xor_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___ior__(PyObject *,PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___ior__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QDirIterator_IteratorFlags)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QDirIterator::IteratorFlags *sipCpp = reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QDirIterator_IteratorFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
#line 351 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
        *sipCpp = QDirIterator::IteratorFlags(*sipCpp | a0);
#line 242 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQDirIteratorIteratorFlags.cpp"

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


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___or__(PyObject *,PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___or__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QDirIterator::IteratorFlags* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QDirIterator_IteratorFlags, &a0, &a0State, &a1))
        {
             ::QDirIterator::IteratorFlags*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QDirIterator::IteratorFlags((*a0 | a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QDirIterator_IteratorFlags,a0State);

            return sipConvertFromNewType(sipRes,sipType_QDirIterator_IteratorFlags,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtCore, or_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___iand__(PyObject *,PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___iand__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QDirIterator_IteratorFlags)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QDirIterator::IteratorFlags *sipCpp = reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QDirIterator_IteratorFlags));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp-> ::QDirIterator::IteratorFlags::operator&=(a0);
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


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___and__(PyObject *,PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___and__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QDirIterator::IteratorFlags* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QDirIterator_IteratorFlags, &a0, &a0State, &a1))
        {
             ::QDirIterator::IteratorFlags*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QDirIterator::IteratorFlags((*a0 & a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QDirIterator_IteratorFlags,a0State);

            return sipConvertFromNewType(sipRes,sipType_QDirIterator_IteratorFlags,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtCore, and_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___invert__(PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___invert__(PyObject *sipSelf)
{
     ::QDirIterator::IteratorFlags *sipCpp = reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QDirIterator_IteratorFlags));

    if (!sipCpp)
        return 0;


    {
        {
             ::QDirIterator::IteratorFlags*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QDirIterator::IteratorFlags(~(*sipCpp));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QDirIterator_IteratorFlags,NULL);
        }
    }

    return 0;
}


extern "C" {static PyObject *slot_QDirIterator_IteratorFlags___int__(PyObject *);}
static PyObject *slot_QDirIterator_IteratorFlags___int__(PyObject *sipSelf)
{
     ::QDirIterator::IteratorFlags *sipCpp = reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QDirIterator_IteratorFlags));

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
extern "C" {static void release_QDirIterator_IteratorFlags(void *, int);}
static void release_QDirIterator_IteratorFlags(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void assign_QDirIterator_IteratorFlags(void *, SIP_SSIZE_T, const void *);}
static void assign_QDirIterator_IteratorFlags(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast< ::QDirIterator::IteratorFlags *>(sipDst)[sipDstIdx] = *reinterpret_cast<const  ::QDirIterator::IteratorFlags *>(sipSrc);
}


extern "C" {static void *array_QDirIterator_IteratorFlags(SIP_SSIZE_T);}
static void *array_QDirIterator_IteratorFlags(SIP_SSIZE_T sipNrElem)
{
    return new  ::QDirIterator::IteratorFlags[sipNrElem];
}


extern "C" {static void *copy_QDirIterator_IteratorFlags(const void *, SIP_SSIZE_T);}
static void *copy_QDirIterator_IteratorFlags(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new  ::QDirIterator::IteratorFlags(reinterpret_cast<const  ::QDirIterator::IteratorFlags *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_QDirIterator_IteratorFlags(sipSimpleWrapper *);}
static void dealloc_QDirIterator_IteratorFlags(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_QDirIterator_IteratorFlags(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_QDirIterator_IteratorFlags(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QDirIterator_IteratorFlags(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
     ::QDirIterator::IteratorFlags *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QDirIterator::IteratorFlags();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        int a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QDirIterator::IteratorFlags(a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const  ::QDirIterator::IteratorFlags* a0;
        int a0State = 0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J1", sipType_QDirIterator_IteratorFlags, &a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QDirIterator::IteratorFlags(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QDirIterator::IteratorFlags *>(a0),sipType_QDirIterator_IteratorFlags,a0State);

            return sipCpp;
        }
    }

    return NULL;
}


extern "C" {static int convertTo_QDirIterator_IteratorFlags(PyObject *, void **, int *, PyObject *);}
static int convertTo_QDirIterator_IteratorFlags(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
     ::QDirIterator::IteratorFlags **sipCppPtr = reinterpret_cast< ::QDirIterator::IteratorFlags **>(sipCppPtrV);

#line 390 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
// Allow an instance of the base enum whenever a QDirIterator::IteratorFlags is expected.

if (sipIsErr == NULL)
    return (PyObject_TypeCheck(sipPy, sipTypeAsPyTypeObject(sipType_QDirIterator_IteratorFlag)) ||
            sipCanConvertToType(sipPy, sipType_QDirIterator_IteratorFlags, SIP_NO_CONVERTORS));

if (PyObject_TypeCheck(sipPy, sipTypeAsPyTypeObject(sipType_QDirIterator_IteratorFlag)))
{
    *sipCppPtr = new QDirIterator::IteratorFlags(int(SIPLong_AsLong(sipPy)));

    return sipGetState(sipTransferObj);
}

*sipCppPtr = reinterpret_cast<QDirIterator::IteratorFlags *>(sipConvertToType(sipPy, sipType_QDirIterator_IteratorFlags, sipTransferObj, SIP_NO_CONVERTORS, 0, sipIsErr));

return 0;
#line 530 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtCore/sipQtCoreQDirIteratorIteratorFlags.cpp"
}


/* Define this type's Python slots. */
static sipPySlotDef slots_QDirIterator_IteratorFlags[] = {
    {(void *)slot_QDirIterator_IteratorFlags___bool__, bool_slot},
    {(void *)slot_QDirIterator_IteratorFlags___ne__, ne_slot},
    {(void *)slot_QDirIterator_IteratorFlags___eq__, eq_slot},
    {(void *)slot_QDirIterator_IteratorFlags___ixor__, ixor_slot},
    {(void *)slot_QDirIterator_IteratorFlags___xor__, xor_slot},
    {(void *)slot_QDirIterator_IteratorFlags___ior__, ior_slot},
    {(void *)slot_QDirIterator_IteratorFlags___or__, or_slot},
    {(void *)slot_QDirIterator_IteratorFlags___iand__, iand_slot},
    {(void *)slot_QDirIterator_IteratorFlags___and__, and_slot},
    {(void *)slot_QDirIterator_IteratorFlags___invert__, invert_slot},
    {(void *)slot_QDirIterator_IteratorFlags___int__, int_slot},
    {0, (sipPySlotType)0}
};

PyDoc_STRVAR(doc_QDirIterator_IteratorFlags, "\1QDirIterator.IteratorFlags()\n"
    "QDirIterator.IteratorFlags(Union[QDirIterator.IteratorFlags, QDirIterator.IteratorFlag])\n"
    "QDirIterator.IteratorFlags(QDirIterator.IteratorFlags)");


static pyqt4ClassPluginDef plugin_QDirIterator_IteratorFlags = {
    0,
    1,
    0
};


sipClassTypeDef sipTypeDef_QtCore_QDirIterator_IteratorFlags = {
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_QDirIterator__IteratorFlags,
        {0},
        &plugin_QDirIterator_IteratorFlags
    },
    {
        sipNameNr_IteratorFlags,
        {50, 255, 0},
        0, 0,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QDirIterator_IteratorFlags,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
    slots_QDirIterator_IteratorFlags,
    init_type_QDirIterator_IteratorFlags,
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
    dealloc_QDirIterator_IteratorFlags,
    assign_QDirIterator_IteratorFlags,
    array_QDirIterator_IteratorFlags,
    copy_QDirIterator_IteratorFlags,
    release_QDirIterator_IteratorFlags,
    0,
    convertTo_QDirIterator_IteratorFlags,
    0,
    0,
    0,
    0,
    0
};
