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

#line 571 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qstyleoption.sip"
#include <qstyleoption.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionTabBarBase.cpp"

#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qrect.sip"
#include <qrect.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionTabBarBase.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qtabbar.sip"
#include <qtabbar.h>
#line 36 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionTabBarBase.cpp"
#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qwidget.sip"
#include <qwidget.h>
#line 39 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQStyleOptionTabBarBase.cpp"


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_QStyleOptionTabBarBase(void *, const sipTypeDef *);}
static void *cast_QStyleOptionTabBarBase(void *sipCppV, const sipTypeDef *targetType)
{
     ::QStyleOptionTabBarBase *sipCpp = reinterpret_cast< ::QStyleOptionTabBarBase *>(sipCppV);

    if (targetType == sipType_QStyleOption)
        return static_cast< ::QStyleOption *>(sipCpp);

    return sipCppV;
}


/* Call the instance's destructor. */
extern "C" {static void release_QStyleOptionTabBarBase(void *, int);}
static void release_QStyleOptionTabBarBase(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast< ::QStyleOptionTabBarBase *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void assign_QStyleOptionTabBarBase(void *, SIP_SSIZE_T, const void *);}
static void assign_QStyleOptionTabBarBase(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast< ::QStyleOptionTabBarBase *>(sipDst)[sipDstIdx] = *reinterpret_cast<const  ::QStyleOptionTabBarBase *>(sipSrc);
}


extern "C" {static void *array_QStyleOptionTabBarBase(SIP_SSIZE_T);}
static void *array_QStyleOptionTabBarBase(SIP_SSIZE_T sipNrElem)
{
    return new  ::QStyleOptionTabBarBase[sipNrElem];
}


extern "C" {static void *copy_QStyleOptionTabBarBase(const void *, SIP_SSIZE_T);}
static void *copy_QStyleOptionTabBarBase(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new  ::QStyleOptionTabBarBase(reinterpret_cast<const  ::QStyleOptionTabBarBase *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_QStyleOptionTabBarBase(sipSimpleWrapper *);}
static void dealloc_QStyleOptionTabBarBase(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_QStyleOptionTabBarBase(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_QStyleOptionTabBarBase(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QStyleOptionTabBarBase(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
     ::QStyleOptionTabBarBase *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QStyleOptionTabBarBase();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const  ::QStyleOptionTabBarBase* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J9", sipType_QStyleOptionTabBarBase, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new  ::QStyleOptionTabBarBase(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_QStyleOptionTabBarBase[] = {{500, 255, 1}};

static sipEnumMemberDef enummembers_QStyleOptionTabBarBase[] = {
    {sipName_Type, static_cast<int>( ::QStyleOptionTabBarBase::Type), 575},
    {sipName_Version, static_cast<int>( ::QStyleOptionTabBarBase::Version), 576},
};


extern "C" {static PyObject *varget_QStyleOptionTabBarBase_selectedTabRect(void *, PyObject *, PyObject *);}
static PyObject *varget_QStyleOptionTabBarBase_selectedTabRect(void *sipSelf, PyObject *, PyObject *)
{
     ::QRect*sipVal;
     ::QStyleOptionTabBarBase *sipCpp = reinterpret_cast< ::QStyleOptionTabBarBase *>(sipSelf);

    sipVal = &sipCpp->selectedTabRect;

    return sipConvertFromType(sipVal, sipType_QRect, NULL);
}


extern "C" {static int varset_QStyleOptionTabBarBase_selectedTabRect(void *, PyObject *, PyObject *);}
static int varset_QStyleOptionTabBarBase_selectedTabRect(void *sipSelf, PyObject *sipPy, PyObject *)
{
     ::QRect*sipVal;
     ::QStyleOptionTabBarBase *sipCpp = reinterpret_cast< ::QStyleOptionTabBarBase *>(sipSelf);

    int sipIsErr = 0;

    sipVal = reinterpret_cast< ::QRect *>(sipForceConvertToType(sipPy,sipType_QRect,NULL,SIP_NOT_NONE,NULL,&sipIsErr));

    if (sipIsErr)
        return -1;

    sipCpp->selectedTabRect = *sipVal;

    return 0;
}


extern "C" {static PyObject *varget_QStyleOptionTabBarBase_shape(void *, PyObject *, PyObject *);}
static PyObject *varget_QStyleOptionTabBarBase_shape(void *sipSelf, PyObject *, PyObject *)
{
     ::QTabBar::Shape sipVal;
     ::QStyleOptionTabBarBase *sipCpp = reinterpret_cast< ::QStyleOptionTabBarBase *>(sipSelf);

    sipVal = sipCpp->shape;

    return sipConvertFromEnum(sipVal, sipType_QTabBar_Shape);
}


extern "C" {static int varset_QStyleOptionTabBarBase_shape(void *, PyObject *, PyObject *);}
static int varset_QStyleOptionTabBarBase_shape(void *sipSelf, PyObject *sipPy, PyObject *)
{
     ::QTabBar::Shape sipVal;
     ::QStyleOptionTabBarBase *sipCpp = reinterpret_cast< ::QStyleOptionTabBarBase *>(sipSelf);

    sipVal = ( ::QTabBar::Shape)SIPLong_AsLong(sipPy);

    if (PyErr_Occurred() != NULL)
        return -1;

    sipCpp->shape = sipVal;

    return 0;
}


extern "C" {static PyObject *varget_QStyleOptionTabBarBase_tabBarRect(void *, PyObject *, PyObject *);}
static PyObject *varget_QStyleOptionTabBarBase_tabBarRect(void *sipSelf, PyObject *, PyObject *)
{
     ::QRect*sipVal;
     ::QStyleOptionTabBarBase *sipCpp = reinterpret_cast< ::QStyleOptionTabBarBase *>(sipSelf);

    sipVal = &sipCpp->tabBarRect;

    return sipConvertFromType(sipVal, sipType_QRect, NULL);
}


extern "C" {static int varset_QStyleOptionTabBarBase_tabBarRect(void *, PyObject *, PyObject *);}
static int varset_QStyleOptionTabBarBase_tabBarRect(void *sipSelf, PyObject *sipPy, PyObject *)
{
     ::QRect*sipVal;
     ::QStyleOptionTabBarBase *sipCpp = reinterpret_cast< ::QStyleOptionTabBarBase *>(sipSelf);

    int sipIsErr = 0;

    sipVal = reinterpret_cast< ::QRect *>(sipForceConvertToType(sipPy,sipType_QRect,NULL,SIP_NOT_NONE,NULL,&sipIsErr));

    if (sipIsErr)
        return -1;

    sipCpp->tabBarRect = *sipVal;

    return 0;
}

sipVariableDef variables_QStyleOptionTabBarBase[] = {
    {InstanceVariable, sipName_selectedTabRect, (PyMethodDef *)varget_QStyleOptionTabBarBase_selectedTabRect, (PyMethodDef *)varset_QStyleOptionTabBarBase_selectedTabRect, NULL, NULL},
    {InstanceVariable, sipName_shape, (PyMethodDef *)varget_QStyleOptionTabBarBase_shape, (PyMethodDef *)varset_QStyleOptionTabBarBase_shape, NULL, NULL},
    {InstanceVariable, sipName_tabBarRect, (PyMethodDef *)varget_QStyleOptionTabBarBase_tabBarRect, (PyMethodDef *)varset_QStyleOptionTabBarBase_tabBarRect, NULL, NULL},
};

PyDoc_STRVAR(doc_QStyleOptionTabBarBase, "\1QStyleOptionTabBarBase()\n"
    "QStyleOptionTabBarBase(QStyleOptionTabBarBase)");


static pyqt4ClassPluginDef plugin_QStyleOptionTabBarBase = {
    0,
    0,
    0
};


sipClassTypeDef sipTypeDef_QtGui_QStyleOptionTabBarBase = {
    {
        -1,
        0,
        0,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_QStyleOptionTabBarBase,
        {0},
        &plugin_QStyleOptionTabBarBase
    },
    {
        sipNameNr_QStyleOptionTabBarBase,
        {0, 0, 1},
        0, 0,
        2, enummembers_QStyleOptionTabBarBase,
        3, variables_QStyleOptionTabBarBase,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QStyleOptionTabBarBase,
    -1,
    -1,
    supers_QStyleOptionTabBarBase,
    0,
    init_type_QStyleOptionTabBarBase,
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
    dealloc_QStyleOptionTabBarBase,
    assign_QStyleOptionTabBarBase,
    array_QStyleOptionTabBarBase,
    copy_QStyleOptionTabBarBase,
    release_QStyleOptionTabBarBase,
    cast_QStyleOptionTabBarBase,
    0,
    0,
    0,
    0,
    0,
    0
};
