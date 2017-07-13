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

#line 1900 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qstyleoption.sip"
#include <qstyleoption.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionViewItemV2ViewItemFeatures.cpp"

#line 1900 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qstyleoption.sip"
#include <qstyleoption.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionViewItemV2ViewItemFeatures.cpp"


extern "C" {static int slot_QStyleOptionViewItemV2_ViewItemFeatures___bool__(PyObject *);}
static int slot_QStyleOptionViewItemV2_ViewItemFeatures___bool__(PyObject *sipSelf)
{
     ::QStyleOptionViewItemV2::ViewItemFeatures *sipCpp = reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QStyleOptionViewItemV2_ViewItemFeatures));

    if (!sipCpp)
        return -1;


    {
        {
            int sipRes = 0;

#line 381 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QStyleOptionViewItemV2::ViewItemFeatures::Int() != 0);
#else
        sipRes = (sipCpp->operator int() != 0);
#endif
#line 55 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionViewItemV2ViewItemFeatures.cpp"

            return sipRes;
        }
    }

    return 0;
}


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___ne__(PyObject *,PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___ne__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QStyleOptionViewItemV2::ViewItemFeatures *sipCpp = reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QStyleOptionViewItemV2_ViewItemFeatures));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QStyleOptionViewItemV2::ViewItemFeatures* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_QStyleOptionViewItemV2_ViewItemFeatures, &a0, &a0State))
        {
            bool sipRes = 0;

#line 372 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QStyleOptionViewItemV2::ViewItemFeatures::Int() != a0->operator QStyleOptionViewItemV2::ViewItemFeatures::Int());
#else
        sipRes = (sipCpp->operator int() != a0->operator int());
#endif
#line 89 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionViewItemV2ViewItemFeatures.cpp"
            sipReleaseType(const_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(a0),sipType_QStyleOptionViewItemV2_ViewItemFeatures,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtGui, ne_slot, sipType_QStyleOptionViewItemV2_ViewItemFeatures, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___eq__(PyObject *,PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___eq__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QStyleOptionViewItemV2::ViewItemFeatures *sipCpp = reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QStyleOptionViewItemV2_ViewItemFeatures));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QStyleOptionViewItemV2::ViewItemFeatures* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_QStyleOptionViewItemV2_ViewItemFeatures, &a0, &a0State))
        {
            bool sipRes = 0;

#line 363 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QStyleOptionViewItemV2::ViewItemFeatures::Int() == a0->operator QStyleOptionViewItemV2::ViewItemFeatures::Int());
#else
        sipRes = (sipCpp->operator int() == a0->operator int());
#endif
#line 129 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionViewItemV2ViewItemFeatures.cpp"
            sipReleaseType(const_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(a0),sipType_QStyleOptionViewItemV2_ViewItemFeatures,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtGui, eq_slot, sipType_QStyleOptionViewItemV2_ViewItemFeatures, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___ixor__(PyObject *,PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___ixor__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QStyleOptionViewItemV2_ViewItemFeatures)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QStyleOptionViewItemV2::ViewItemFeatures *sipCpp = reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QStyleOptionViewItemV2_ViewItemFeatures));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
#line 357 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
        *sipCpp = QStyleOptionViewItemV2::ViewItemFeatures(*sipCpp ^ a0);
#line 168 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionViewItemV2ViewItemFeatures.cpp"

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


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___xor__(PyObject *,PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___xor__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QStyleOptionViewItemV2::ViewItemFeatures* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QStyleOptionViewItemV2_ViewItemFeatures, &a0, &a0State, &a1))
        {
             ::QStyleOptionViewItemV2::ViewItemFeatures*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QStyleOptionViewItemV2::ViewItemFeatures((*a0 ^ a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QStyleOptionViewItemV2_ViewItemFeatures,a0State);

            return sipConvertFromNewType(sipRes,sipType_QStyleOptionViewItemV2_ViewItemFeatures,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtGui, xor_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___ior__(PyObject *,PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___ior__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QStyleOptionViewItemV2_ViewItemFeatures)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QStyleOptionViewItemV2::ViewItemFeatures *sipCpp = reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QStyleOptionViewItemV2_ViewItemFeatures));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
#line 351 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
        *sipCpp = QStyleOptionViewItemV2::ViewItemFeatures(*sipCpp | a0);
#line 242 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionViewItemV2ViewItemFeatures.cpp"

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


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___or__(PyObject *,PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___or__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QStyleOptionViewItemV2::ViewItemFeatures* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QStyleOptionViewItemV2_ViewItemFeatures, &a0, &a0State, &a1))
        {
             ::QStyleOptionViewItemV2::ViewItemFeatures*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QStyleOptionViewItemV2::ViewItemFeatures((*a0 | a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QStyleOptionViewItemV2_ViewItemFeatures,a0State);

            return sipConvertFromNewType(sipRes,sipType_QStyleOptionViewItemV2_ViewItemFeatures,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtGui, or_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___iand__(PyObject *,PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___iand__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QStyleOptionViewItemV2_ViewItemFeatures)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QStyleOptionViewItemV2::ViewItemFeatures *sipCpp = reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QStyleOptionViewItemV2_ViewItemFeatures));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp-> ::QStyleOptionViewItemV2::ViewItemFeatures::operator&=(a0);
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


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___and__(PyObject *,PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___and__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QStyleOptionViewItemV2::ViewItemFeatures* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QStyleOptionViewItemV2_ViewItemFeatures, &a0, &a0State, &a1))
        {
             ::QStyleOptionViewItemV2::ViewItemFeatures*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QStyleOptionViewItemV2::ViewItemFeatures((*a0 & a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QStyleOptionViewItemV2_ViewItemFeatures,a0State);

            return sipConvertFromNewType(sipRes,sipType_QStyleOptionViewItemV2_ViewItemFeatures,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtGui, and_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___invert__(PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___invert__(PyObject *sipSelf)
{
     ::QStyleOptionViewItemV2::ViewItemFeatures *sipCpp = reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QStyleOptionViewItemV2_ViewItemFeatures));

    if (!sipCpp)
        return 0;


    {
        {
             ::QStyleOptionViewItemV2::ViewItemFeatures*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QStyleOptionViewItemV2::ViewItemFeatures(~(*sipCpp));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QStyleOptionViewItemV2_ViewItemFeatures,NULL);
        }
    }

    return 0;
}


extern "C" {static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___int__(PyObject *);}
static PyObject *slot_QStyleOptionViewItemV2_ViewItemFeatures___int__(PyObject *sipSelf)
{
     ::QStyleOptionViewItemV2::ViewItemFeatures *sipCpp = reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QStyleOptionViewItemV2_ViewItemFeatures));

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
extern "C" {static void release_QStyleOptionViewItemV2_ViewItemFeatures(void *, int);}
static void release_QStyleOptionViewItemV2_ViewItemFeatures(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void assign_QStyleOptionViewItemV2_ViewItemFeatures(void *, SIP_SSIZE_T, const void *);}
static void assign_QStyleOptionViewItemV2_ViewItemFeatures(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipDst)[sipDstIdx] = *reinterpret_cast<const  ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipSrc);
}


extern "C" {static void *array_QStyleOptionViewItemV2_ViewItemFeatures(SIP_SSIZE_T);}
static void *array_QStyleOptionViewItemV2_ViewItemFeatures(SIP_SSIZE_T sipNrElem)
{
    return new  ::QStyleOptionViewItemV2::ViewItemFeatures[sipNrElem];
}


extern "C" {static void *copy_QStyleOptionViewItemV2_ViewItemFeatures(const void *, SIP_SSIZE_T);}
static void *copy_QStyleOptionViewItemV2_ViewItemFeatures(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new  ::QStyleOptionViewItemV2::ViewItemFeatures(reinterpret_cast<const  ::QStyleOptionViewItemV2::ViewItemFeatures *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_QStyleOptionViewItemV2_ViewItemFeatures(sipSimpleWrapper *);}
static void dealloc_QStyleOptionViewItemV2_ViewItemFeatures(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_QStyleOptionViewItemV2_ViewItemFeatures(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_QStyleOptionViewItemV2_ViewItemFeatures(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QStyleOptionViewItemV2_ViewItemFeatures(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
     ::QStyleOptionViewItemV2::ViewItemFeatures *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QStyleOptionViewItemV2::ViewItemFeatures();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        int a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QStyleOptionViewItemV2::ViewItemFeatures(a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const  ::QStyleOptionViewItemV2::ViewItemFeatures* a0;
        int a0State = 0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J1", sipType_QStyleOptionViewItemV2_ViewItemFeatures, &a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QStyleOptionViewItemV2::ViewItemFeatures(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QStyleOptionViewItemV2::ViewItemFeatures *>(a0),sipType_QStyleOptionViewItemV2_ViewItemFeatures,a0State);

            return sipCpp;
        }
    }

    return NULL;
}


extern "C" {static int convertTo_QStyleOptionViewItemV2_ViewItemFeatures(PyObject *, void **, int *, PyObject *);}
static int convertTo_QStyleOptionViewItemV2_ViewItemFeatures(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
     ::QStyleOptionViewItemV2::ViewItemFeatures **sipCppPtr = reinterpret_cast< ::QStyleOptionViewItemV2::ViewItemFeatures **>(sipCppPtrV);

#line 390 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
// Allow an instance of the base enum whenever a QStyleOptionViewItemV2::ViewItemFeatures is expected.

if (sipIsErr == NULL)
    return (PyObject_TypeCheck(sipPy, sipTypeAsPyTypeObject(sipType_QStyleOptionViewItemV2_ViewItemFeature)) ||
            sipCanConvertToType(sipPy, sipType_QStyleOptionViewItemV2_ViewItemFeatures, SIP_NO_CONVERTORS));

if (PyObject_TypeCheck(sipPy, sipTypeAsPyTypeObject(sipType_QStyleOptionViewItemV2_ViewItemFeature)))
{
    *sipCppPtr = new QStyleOptionViewItemV2::ViewItemFeatures(int(SIPLong_AsLong(sipPy)));

    return sipGetState(sipTransferObj);
}

*sipCppPtr = reinterpret_cast<QStyleOptionViewItemV2::ViewItemFeatures *>(sipConvertToType(sipPy, sipType_QStyleOptionViewItemV2_ViewItemFeatures, sipTransferObj, SIP_NO_CONVERTORS, 0, sipIsErr));

return 0;
#line 530 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionViewItemV2ViewItemFeatures.cpp"
}


/* Define this type's Python slots. */
static sipPySlotDef slots_QStyleOptionViewItemV2_ViewItemFeatures[] = {
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___bool__, bool_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___ne__, ne_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___eq__, eq_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___ixor__, ixor_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___xor__, xor_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___ior__, ior_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___or__, or_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___iand__, iand_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___and__, and_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___invert__, invert_slot},
    {(void *)slot_QStyleOptionViewItemV2_ViewItemFeatures___int__, int_slot},
    {0, (sipPySlotType)0}
};

PyDoc_STRVAR(doc_QStyleOptionViewItemV2_ViewItemFeatures, "\1QStyleOptionViewItemV2.ViewItemFeatures()\n"
    "QStyleOptionViewItemV2.ViewItemFeatures(Union[QStyleOptionViewItemV2.ViewItemFeatures, QStyleOptionViewItemV2.ViewItemFeature])\n"
    "QStyleOptionViewItemV2.ViewItemFeatures(QStyleOptionViewItemV2.ViewItemFeatures)");


static pyqt4ClassPluginDef plugin_QStyleOptionViewItemV2_ViewItemFeatures = {
    0,
    1,
    0
};


sipClassTypeDef sipTypeDef_QtGui_QStyleOptionViewItemV2_ViewItemFeatures = {
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_QStyleOptionViewItemV2__ViewItemFeatures,
        {0},
        &plugin_QStyleOptionViewItemV2_ViewItemFeatures
    },
    {
        sipNameNr_ViewItemFeatures,
        {613, 255, 0},
        0, 0,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QStyleOptionViewItemV2_ViewItemFeatures,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
    slots_QStyleOptionViewItemV2_ViewItemFeatures,
    init_type_QStyleOptionViewItemV2_ViewItemFeatures,
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
    dealloc_QStyleOptionViewItemV2_ViewItemFeatures,
    assign_QStyleOptionViewItemV2_ViewItemFeatures,
    array_QStyleOptionViewItemV2_ViewItemFeatures,
    copy_QStyleOptionViewItemV2_ViewItemFeatures,
    release_QStyleOptionViewItemV2_ViewItemFeatures,
    0,
    convertTo_QStyleOptionViewItemV2_ViewItemFeatures,
    0,
    0,
    0,
    0,
    0
};
