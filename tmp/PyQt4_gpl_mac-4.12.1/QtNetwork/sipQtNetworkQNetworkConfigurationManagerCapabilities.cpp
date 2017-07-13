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

#include "sipAPIQtNetwork.h"

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkconfigmanager.sip"
#include <qnetworkconfigmanager.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQNetworkConfigurationManagerCapabilities.cpp"

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qnetworkconfigmanager.sip"
#include <qnetworkconfigmanager.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQNetworkConfigurationManagerCapabilities.cpp"


extern "C" {static int slot_QNetworkConfigurationManager_Capabilities___bool__(PyObject *);}
static int slot_QNetworkConfigurationManager_Capabilities___bool__(PyObject *sipSelf)
{
     ::QNetworkConfigurationManager::Capabilities *sipCpp = reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QNetworkConfigurationManager_Capabilities));

    if (!sipCpp)
        return -1;


    {
        {
            int sipRes = 0;

#line 381 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QNetworkConfigurationManager::Capabilities::Int() != 0);
#else
        sipRes = (sipCpp->operator int() != 0);
#endif
#line 55 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQNetworkConfigurationManagerCapabilities.cpp"

            return sipRes;
        }
    }

    return 0;
}


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___ne__(PyObject *,PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___ne__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QNetworkConfigurationManager::Capabilities *sipCpp = reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QNetworkConfigurationManager_Capabilities));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QNetworkConfigurationManager::Capabilities* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_QNetworkConfigurationManager_Capabilities, &a0, &a0State))
        {
            bool sipRes = 0;

#line 372 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QNetworkConfigurationManager::Capabilities::Int() != a0->operator QNetworkConfigurationManager::Capabilities::Int());
#else
        sipRes = (sipCpp->operator int() != a0->operator int());
#endif
#line 89 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQNetworkConfigurationManagerCapabilities.cpp"
            sipReleaseType(const_cast< ::QNetworkConfigurationManager::Capabilities *>(a0),sipType_QNetworkConfigurationManager_Capabilities,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtNetwork, ne_slot, sipType_QNetworkConfigurationManager_Capabilities, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___eq__(PyObject *,PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___eq__(PyObject *sipSelf,PyObject *sipArg)
{
     ::QNetworkConfigurationManager::Capabilities *sipCpp = reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QNetworkConfigurationManager_Capabilities));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const  ::QNetworkConfigurationManager::Capabilities* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_QNetworkConfigurationManager_Capabilities, &a0, &a0State))
        {
            bool sipRes = 0;

#line 363 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
#if QT_VERSION >= 0x050000
        sipRes = (sipCpp->operator QNetworkConfigurationManager::Capabilities::Int() == a0->operator QNetworkConfigurationManager::Capabilities::Int());
#else
        sipRes = (sipCpp->operator int() == a0->operator int());
#endif
#line 129 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQNetworkConfigurationManagerCapabilities.cpp"
            sipReleaseType(const_cast< ::QNetworkConfigurationManager::Capabilities *>(a0),sipType_QNetworkConfigurationManager_Capabilities,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtNetwork, eq_slot, sipType_QNetworkConfigurationManager_Capabilities, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___ixor__(PyObject *,PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___ixor__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QNetworkConfigurationManager_Capabilities)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QNetworkConfigurationManager::Capabilities *sipCpp = reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QNetworkConfigurationManager_Capabilities));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
#line 357 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
        *sipCpp = QNetworkConfigurationManager::Capabilities(*sipCpp ^ a0);
#line 168 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQNetworkConfigurationManagerCapabilities.cpp"

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


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___xor__(PyObject *,PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___xor__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QNetworkConfigurationManager::Capabilities* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QNetworkConfigurationManager_Capabilities, &a0, &a0State, &a1))
        {
             ::QNetworkConfigurationManager::Capabilities*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QNetworkConfigurationManager::Capabilities((*a0 ^ a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QNetworkConfigurationManager_Capabilities,a0State);

            return sipConvertFromNewType(sipRes,sipType_QNetworkConfigurationManager_Capabilities,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtNetwork, xor_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___ior__(PyObject *,PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___ior__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QNetworkConfigurationManager_Capabilities)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QNetworkConfigurationManager::Capabilities *sipCpp = reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QNetworkConfigurationManager_Capabilities));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
#line 351 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
        *sipCpp = QNetworkConfigurationManager::Capabilities(*sipCpp | a0);
#line 242 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQNetworkConfigurationManagerCapabilities.cpp"

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


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___or__(PyObject *,PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___or__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QNetworkConfigurationManager::Capabilities* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QNetworkConfigurationManager_Capabilities, &a0, &a0State, &a1))
        {
             ::QNetworkConfigurationManager::Capabilities*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QNetworkConfigurationManager::Capabilities((*a0 | a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QNetworkConfigurationManager_Capabilities,a0State);

            return sipConvertFromNewType(sipRes,sipType_QNetworkConfigurationManager_Capabilities,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtNetwork, or_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___iand__(PyObject *,PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___iand__(PyObject *sipSelf,PyObject *sipArg)
{
    if (!PyObject_TypeCheck(sipSelf, sipTypeAsPyTypeObject(sipType_QNetworkConfigurationManager_Capabilities)))
    {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }

     ::QNetworkConfigurationManager::Capabilities *sipCpp = reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QNetworkConfigurationManager_Capabilities));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp-> ::QNetworkConfigurationManager::Capabilities::operator&=(a0);
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


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___and__(PyObject *,PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___and__(PyObject *sipArg0,PyObject *sipArg1)
{
    PyObject *sipParseErr = NULL;

    {
         ::QNetworkConfigurationManager::Capabilities* a0;
        int a0State = 0;
        int a1;

        if (sipParsePair(&sipParseErr, sipArg0, sipArg1, "J1i", sipType_QNetworkConfigurationManager_Capabilities, &a0, &a0State, &a1))
        {
             ::QNetworkConfigurationManager::Capabilities*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QNetworkConfigurationManager::Capabilities((*a0 & a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QNetworkConfigurationManager_Capabilities,a0State);

            return sipConvertFromNewType(sipRes,sipType_QNetworkConfigurationManager_Capabilities,NULL);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtNetwork, and_slot, NULL, sipArg0, sipArg1);
}


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___invert__(PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___invert__(PyObject *sipSelf)
{
     ::QNetworkConfigurationManager::Capabilities *sipCpp = reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QNetworkConfigurationManager_Capabilities));

    if (!sipCpp)
        return 0;


    {
        {
             ::QNetworkConfigurationManager::Capabilities*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QNetworkConfigurationManager::Capabilities(~(*sipCpp));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QNetworkConfigurationManager_Capabilities,NULL);
        }
    }

    return 0;
}


extern "C" {static PyObject *slot_QNetworkConfigurationManager_Capabilities___int__(PyObject *);}
static PyObject *slot_QNetworkConfigurationManager_Capabilities___int__(PyObject *sipSelf)
{
     ::QNetworkConfigurationManager::Capabilities *sipCpp = reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QNetworkConfigurationManager_Capabilities));

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
extern "C" {static void release_QNetworkConfigurationManager_Capabilities(void *, int);}
static void release_QNetworkConfigurationManager_Capabilities(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void assign_QNetworkConfigurationManager_Capabilities(void *, SIP_SSIZE_T, const void *);}
static void assign_QNetworkConfigurationManager_Capabilities(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast< ::QNetworkConfigurationManager::Capabilities *>(sipDst)[sipDstIdx] = *reinterpret_cast<const  ::QNetworkConfigurationManager::Capabilities *>(sipSrc);
}


extern "C" {static void *array_QNetworkConfigurationManager_Capabilities(SIP_SSIZE_T);}
static void *array_QNetworkConfigurationManager_Capabilities(SIP_SSIZE_T sipNrElem)
{
    return new  ::QNetworkConfigurationManager::Capabilities[sipNrElem];
}


extern "C" {static void *copy_QNetworkConfigurationManager_Capabilities(const void *, SIP_SSIZE_T);}
static void *copy_QNetworkConfigurationManager_Capabilities(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new  ::QNetworkConfigurationManager::Capabilities(reinterpret_cast<const  ::QNetworkConfigurationManager::Capabilities *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_QNetworkConfigurationManager_Capabilities(sipSimpleWrapper *);}
static void dealloc_QNetworkConfigurationManager_Capabilities(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_QNetworkConfigurationManager_Capabilities(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_QNetworkConfigurationManager_Capabilities(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QNetworkConfigurationManager_Capabilities(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
     ::QNetworkConfigurationManager::Capabilities *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QNetworkConfigurationManager::Capabilities();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        int a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QNetworkConfigurationManager::Capabilities(a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const  ::QNetworkConfigurationManager::Capabilities* a0;
        int a0State = 0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J1", sipType_QNetworkConfigurationManager_Capabilities, &a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QNetworkConfigurationManager::Capabilities(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QNetworkConfigurationManager::Capabilities *>(a0),sipType_QNetworkConfigurationManager_Capabilities,a0State);

            return sipCpp;
        }
    }

    return NULL;
}


extern "C" {static int convertTo_QNetworkConfigurationManager_Capabilities(PyObject *, void **, int *, PyObject *);}
static int convertTo_QNetworkConfigurationManager_Capabilities(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
     ::QNetworkConfigurationManager::Capabilities **sipCppPtr = reinterpret_cast< ::QNetworkConfigurationManager::Capabilities **>(sipCppPtrV);

#line 390 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qglobal.sip"
// Allow an instance of the base enum whenever a QNetworkConfigurationManager::Capabilities is expected.

if (sipIsErr == NULL)
    return (PyObject_TypeCheck(sipPy, sipTypeAsPyTypeObject(sipType_QNetworkConfigurationManager_Capability)) ||
            sipCanConvertToType(sipPy, sipType_QNetworkConfigurationManager_Capabilities, SIP_NO_CONVERTORS));

if (PyObject_TypeCheck(sipPy, sipTypeAsPyTypeObject(sipType_QNetworkConfigurationManager_Capability)))
{
    *sipCppPtr = new QNetworkConfigurationManager::Capabilities(int(SIPLong_AsLong(sipPy)));

    return sipGetState(sipTransferObj);
}

*sipCppPtr = reinterpret_cast<QNetworkConfigurationManager::Capabilities *>(sipConvertToType(sipPy, sipType_QNetworkConfigurationManager_Capabilities, sipTransferObj, SIP_NO_CONVERTORS, 0, sipIsErr));

return 0;
#line 530 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQNetworkConfigurationManagerCapabilities.cpp"
}


/* Define this type's Python slots. */
static sipPySlotDef slots_QNetworkConfigurationManager_Capabilities[] = {
    {(void *)slot_QNetworkConfigurationManager_Capabilities___bool__, bool_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___ne__, ne_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___eq__, eq_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___ixor__, ixor_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___xor__, xor_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___ior__, ior_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___or__, or_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___iand__, iand_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___and__, and_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___invert__, invert_slot},
    {(void *)slot_QNetworkConfigurationManager_Capabilities___int__, int_slot},
    {0, (sipPySlotType)0}
};

PyDoc_STRVAR(doc_QNetworkConfigurationManager_Capabilities, "\1QNetworkConfigurationManager.Capabilities()\n"
    "QNetworkConfigurationManager.Capabilities(Union[QNetworkConfigurationManager.Capabilities, QNetworkConfigurationManager.Capability])\n"
    "QNetworkConfigurationManager.Capabilities(QNetworkConfigurationManager.Capabilities)");


static pyqt4ClassPluginDef plugin_QNetworkConfigurationManager_Capabilities = {
    0,
    1,
    0
};


sipClassTypeDef sipTypeDef_QtNetwork_QNetworkConfigurationManager_Capabilities = {
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_QNetworkConfigurationManager__Capabilities,
        {0},
        &plugin_QNetworkConfigurationManager_Capabilities
    },
    {
        sipNameNr_Capabilities,
        {54, 255, 0},
        0, 0,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QNetworkConfigurationManager_Capabilities,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
    slots_QNetworkConfigurationManager_Capabilities,
    init_type_QNetworkConfigurationManager_Capabilities,
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
    dealloc_QNetworkConfigurationManager_Capabilities,
    assign_QNetworkConfigurationManager_Capabilities,
    array_QNetworkConfigurationManager_Capabilities,
    copy_QNetworkConfigurationManager_Capabilities,
    release_QNetworkConfigurationManager_Capabilities,
    0,
    convertTo_QNetworkConfigurationManager_Capabilities,
    0,
    0,
    0,
    0,
    0
};
