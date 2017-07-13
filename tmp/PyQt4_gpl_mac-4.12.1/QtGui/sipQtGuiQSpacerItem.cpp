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

#line 76 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qlayoutitem.sip"
#include <qlayoutitem.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQSpacerItem.cpp"

#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qsizepolicy.sip"
#include <qsizepolicy.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQSpacerItem.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qrect.sip"
#include <qrect.h>
#line 36 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQSpacerItem.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 39 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQSpacerItem.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qsize.sip"
#include <qsize.h>
#line 42 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQSpacerItem.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qsizepolicy.sip"
#include <qsizepolicy.h>
#line 45 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQSpacerItem.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 48 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQSpacerItem.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qlayout.sip"
#include <qlayout.h>
#line 51 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQSpacerItem.cpp"
#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qwidget.sip"
#include <qwidget.h>
#line 54 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQSpacerItem.cpp"


class sipQSpacerItem : public  ::QSpacerItem
{
public:
    sipQSpacerItem(int,int, ::QSizePolicy::Policy, ::QSizePolicy::Policy);
    sipQSpacerItem(const  ::QSpacerItem&);
    virtual ~sipQSpacerItem();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
     ::QSize sizeHint() const;
     ::QSize minimumSize() const;
     ::QSize maximumSize() const;
     ::Qt::Orientations expandingDirections() const;
    void setGeometry(const  ::QRect&);
     ::QRect geometry() const;
    bool isEmpty() const;
    bool hasHeightForWidth() const;
    int heightForWidth(int) const;
    int minimumHeightForWidth(int) const;
    void invalidate();
     ::QWidget* widget();
     ::QLayout* layout();
     ::QSpacerItem* spacerItem();

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipQSpacerItem(const sipQSpacerItem &);
    sipQSpacerItem &operator = (const sipQSpacerItem &);

    char sipPyMethods[14];
};

sipQSpacerItem::sipQSpacerItem(int a0,int a1, ::QSizePolicy::Policy a2, ::QSizePolicy::Policy a3):  ::QSpacerItem(a0,a1,a2,a3), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQSpacerItem::sipQSpacerItem(const  ::QSpacerItem& a0):  ::QSpacerItem(a0), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQSpacerItem::~sipQSpacerItem()
{
    sipInstanceDestroyed(sipPySelf);
}

 ::QSize sipQSpacerItem::sizeHint() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[0]),sipPySelf,NULL,sipName_sizeHint);

    if (!sipMeth)
        return  ::QSpacerItem::sizeHint();

    extern  ::QSize sipVH_QtGui_10(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_10(sipGILState, 0, sipPySelf, sipMeth);
}

 ::QSize sipQSpacerItem::minimumSize() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[1]),sipPySelf,NULL,sipName_minimumSize);

    if (!sipMeth)
        return  ::QSpacerItem::minimumSize();

    extern  ::QSize sipVH_QtGui_10(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_10(sipGILState, 0, sipPySelf, sipMeth);
}

 ::QSize sipQSpacerItem::maximumSize() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[2]),sipPySelf,NULL,sipName_maximumSize);

    if (!sipMeth)
        return  ::QSpacerItem::maximumSize();

    extern  ::QSize sipVH_QtGui_10(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_10(sipGILState, 0, sipPySelf, sipMeth);
}

 ::Qt::Orientations sipQSpacerItem::expandingDirections() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[3]),sipPySelf,NULL,sipName_expandingDirections);

    if (!sipMeth)
        return  ::QSpacerItem::expandingDirections();

    extern  ::Qt::Orientations sipVH_QtGui_104(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_104(sipGILState, 0, sipPySelf, sipMeth);
}

void sipQSpacerItem::setGeometry(const  ::QRect& a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[4],sipPySelf,NULL,sipName_setGeometry);

    if (!sipMeth)
    {
         ::QSpacerItem::setGeometry(a0);
        return;
    }

    extern void sipVH_QtGui_105(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const  ::QRect&);

    sipVH_QtGui_105(sipGILState, 0, sipPySelf, sipMeth, a0);
}

 ::QRect sipQSpacerItem::geometry() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[5]),sipPySelf,NULL,sipName_geometry);

    if (!sipMeth)
        return  ::QSpacerItem::geometry();

    extern  ::QRect sipVH_QtGui_106(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_106(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipQSpacerItem::isEmpty() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[6]),sipPySelf,NULL,sipName_isEmpty);

    if (!sipMeth)
        return  ::QSpacerItem::isEmpty();

    extern bool sipVH_QtGui_67(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_67(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipQSpacerItem::hasHeightForWidth() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[7]),sipPySelf,NULL,sipName_hasHeightForWidth);

    if (!sipMeth)
        return  ::QSpacerItem::hasHeightForWidth();

    extern bool sipVH_QtGui_67(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_67(sipGILState, 0, sipPySelf, sipMeth);
}

int sipQSpacerItem::heightForWidth(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[8]),sipPySelf,NULL,sipName_heightForWidth);

    if (!sipMeth)
        return  ::QSpacerItem::heightForWidth(a0);

    extern int sipVH_QtGui_11(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    return sipVH_QtGui_11(sipGILState, 0, sipPySelf, sipMeth, a0);
}

int sipQSpacerItem::minimumHeightForWidth(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[9]),sipPySelf,NULL,sipName_minimumHeightForWidth);

    if (!sipMeth)
        return  ::QSpacerItem::minimumHeightForWidth(a0);

    extern int sipVH_QtGui_11(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    return sipVH_QtGui_11(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQSpacerItem::invalidate()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[10],sipPySelf,NULL,sipName_invalidate);

    if (!sipMeth)
    {
         ::QSpacerItem::invalidate();
        return;
    }

    extern void sipVH_QtGui_34(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    sipVH_QtGui_34(sipGILState, 0, sipPySelf, sipMeth);
}

 ::QWidget* sipQSpacerItem::widget()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[11],sipPySelf,NULL,sipName_widget);

    if (!sipMeth)
        return  ::QSpacerItem::widget();

    extern  ::QWidget* sipVH_QtGui_107(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_107(sipGILState, 0, sipPySelf, sipMeth);
}

 ::QLayout* sipQSpacerItem::layout()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[12],sipPySelf,NULL,sipName_layout);

    if (!sipMeth)
        return  ::QSpacerItem::layout();

    extern  ::QLayout* sipVH_QtGui_108(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_108(sipGILState, 0, sipPySelf, sipMeth);
}

 ::QSpacerItem* sipQSpacerItem::spacerItem()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[13],sipPySelf,NULL,sipName_spacerItem);

    if (!sipMeth)
        return  ::QSpacerItem::spacerItem();

    extern  ::QSpacerItem* sipVH_QtGui_109(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_109(sipGILState, 0, sipPySelf, sipMeth);
}


PyDoc_STRVAR(doc_QSpacerItem_changeSize, "changeSize(self, int, int, hPolicy: QSizePolicy.Policy = QSizePolicy.Minimum, vPolicy: QSizePolicy.Policy = QSizePolicy.Minimum)");

extern "C" {static PyObject *meth_QSpacerItem_changeSize(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QSpacerItem_changeSize(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;
        int a1;
         ::QSizePolicy::Policy a2 = QSizePolicy::Minimum;
         ::QSizePolicy::Policy a3 = QSizePolicy::Minimum;
         ::QSpacerItem *sipCpp;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_hPolicy,
            sipName_vPolicy,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "Bii|EE", &sipSelf, sipType_QSpacerItem, &sipCpp, &a0, &a1, sipType_QSizePolicy_Policy, &a2, sipType_QSizePolicy_Policy, &a3))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->changeSize(a0,a1,a2,a3);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSpacerItem, sipName_changeSize, doc_QSpacerItem_changeSize);

    return NULL;
}


PyDoc_STRVAR(doc_QSpacerItem_sizeHint, "sizeHint(self) -> QSize");

extern "C" {static PyObject *meth_QSpacerItem_sizeHint(PyObject *, PyObject *);}
static PyObject *meth_QSpacerItem_sizeHint(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QSpacerItem *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSpacerItem, &sipCpp))
        {
             ::QSize*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QSize((sipSelfWasArg ? sipCpp-> ::QSpacerItem::sizeHint() : sipCpp->sizeHint()));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QSize,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSpacerItem, sipName_sizeHint, doc_QSpacerItem_sizeHint);

    return NULL;
}


PyDoc_STRVAR(doc_QSpacerItem_minimumSize, "minimumSize(self) -> QSize");

extern "C" {static PyObject *meth_QSpacerItem_minimumSize(PyObject *, PyObject *);}
static PyObject *meth_QSpacerItem_minimumSize(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QSpacerItem *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSpacerItem, &sipCpp))
        {
             ::QSize*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QSize((sipSelfWasArg ? sipCpp-> ::QSpacerItem::minimumSize() : sipCpp->minimumSize()));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QSize,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSpacerItem, sipName_minimumSize, doc_QSpacerItem_minimumSize);

    return NULL;
}


PyDoc_STRVAR(doc_QSpacerItem_maximumSize, "maximumSize(self) -> QSize");

extern "C" {static PyObject *meth_QSpacerItem_maximumSize(PyObject *, PyObject *);}
static PyObject *meth_QSpacerItem_maximumSize(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QSpacerItem *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSpacerItem, &sipCpp))
        {
             ::QSize*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QSize((sipSelfWasArg ? sipCpp-> ::QSpacerItem::maximumSize() : sipCpp->maximumSize()));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QSize,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSpacerItem, sipName_maximumSize, doc_QSpacerItem_maximumSize);

    return NULL;
}


PyDoc_STRVAR(doc_QSpacerItem_expandingDirections, "expandingDirections(self) -> Qt.Orientations");

extern "C" {static PyObject *meth_QSpacerItem_expandingDirections(PyObject *, PyObject *);}
static PyObject *meth_QSpacerItem_expandingDirections(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QSpacerItem *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSpacerItem, &sipCpp))
        {
             ::Qt::Orientations*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::Qt::Orientations((sipSelfWasArg ? sipCpp-> ::QSpacerItem::expandingDirections() : sipCpp->expandingDirections()));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_Qt_Orientations,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSpacerItem, sipName_expandingDirections, doc_QSpacerItem_expandingDirections);

    return NULL;
}


PyDoc_STRVAR(doc_QSpacerItem_isEmpty, "isEmpty(self) -> bool");

extern "C" {static PyObject *meth_QSpacerItem_isEmpty(PyObject *, PyObject *);}
static PyObject *meth_QSpacerItem_isEmpty(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QSpacerItem *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSpacerItem, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp-> ::QSpacerItem::isEmpty() : sipCpp->isEmpty());
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSpacerItem, sipName_isEmpty, doc_QSpacerItem_isEmpty);

    return NULL;
}


PyDoc_STRVAR(doc_QSpacerItem_setGeometry, "setGeometry(self, QRect)");

extern "C" {static PyObject *meth_QSpacerItem_setGeometry(PyObject *, PyObject *);}
static PyObject *meth_QSpacerItem_setGeometry(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QRect* a0;
         ::QSpacerItem *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ9", &sipSelf, sipType_QSpacerItem, &sipCpp, sipType_QRect, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp-> ::QSpacerItem::setGeometry(*a0) : sipCpp->setGeometry(*a0));
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSpacerItem, sipName_setGeometry, doc_QSpacerItem_setGeometry);

    return NULL;
}


PyDoc_STRVAR(doc_QSpacerItem_geometry, "geometry(self) -> QRect");

extern "C" {static PyObject *meth_QSpacerItem_geometry(PyObject *, PyObject *);}
static PyObject *meth_QSpacerItem_geometry(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QSpacerItem *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSpacerItem, &sipCpp))
        {
             ::QRect*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QRect((sipSelfWasArg ? sipCpp-> ::QSpacerItem::geometry() : sipCpp->geometry()));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QRect,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSpacerItem, sipName_geometry, doc_QSpacerItem_geometry);

    return NULL;
}


PyDoc_STRVAR(doc_QSpacerItem_spacerItem, "spacerItem(self) -> QSpacerItem");

extern "C" {static PyObject *meth_QSpacerItem_spacerItem(PyObject *, PyObject *);}
static PyObject *meth_QSpacerItem_spacerItem(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
         ::QSpacerItem *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSpacerItem, &sipCpp))
        {
             ::QSpacerItem*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp-> ::QSpacerItem::spacerItem() : sipCpp->spacerItem());
            Py_END_ALLOW_THREADS

            return sipConvertFromType(sipRes,sipType_QSpacerItem,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSpacerItem, sipName_spacerItem, doc_QSpacerItem_spacerItem);

    return NULL;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_QSpacerItem(void *, const sipTypeDef *);}
static void *cast_QSpacerItem(void *sipCppV, const sipTypeDef *targetType)
{
     ::QSpacerItem *sipCpp = reinterpret_cast< ::QSpacerItem *>(sipCppV);

    if (targetType == sipType_QLayoutItem)
        return static_cast< ::QLayoutItem *>(sipCpp);

    return sipCppV;
}


/* Call the instance's destructor. */
extern "C" {static void release_QSpacerItem(void *, int);}
static void release_QSpacerItem(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipQSpacerItem *>(sipCppV);
    else
        delete reinterpret_cast< ::QSpacerItem *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QSpacerItem(sipSimpleWrapper *);}
static void dealloc_QSpacerItem(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipQSpacerItem *>(sipGetAddress(sipSelf))->sipPySelf = NULL;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_QSpacerItem(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_QSpacerItem(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QSpacerItem(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipQSpacerItem *sipCpp = 0;

    {
        int a0;
        int a1;
         ::QSizePolicy::Policy a2 = QSizePolicy::Minimum;
         ::QSizePolicy::Policy a3 = QSizePolicy::Minimum;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_hPolicy,
            sipName_vPolicy,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "ii|EE", &a0, &a1, sipType_QSizePolicy_Policy, &a2, sipType_QSizePolicy_Policy, &a3))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQSpacerItem(a0,a1,a2,a3);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    {
        const  ::QSpacerItem* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J9", sipType_QSpacerItem, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQSpacerItem(*a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_QSpacerItem[] = {{276, 255, 1}};


static PyMethodDef methods_QSpacerItem[] = {
    {SIP_MLNAME_CAST(sipName_changeSize), (PyCFunction)meth_QSpacerItem_changeSize, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QSpacerItem_changeSize)},
    {SIP_MLNAME_CAST(sipName_expandingDirections), meth_QSpacerItem_expandingDirections, METH_VARARGS, SIP_MLDOC_CAST(doc_QSpacerItem_expandingDirections)},
    {SIP_MLNAME_CAST(sipName_geometry), meth_QSpacerItem_geometry, METH_VARARGS, SIP_MLDOC_CAST(doc_QSpacerItem_geometry)},
    {SIP_MLNAME_CAST(sipName_isEmpty), meth_QSpacerItem_isEmpty, METH_VARARGS, SIP_MLDOC_CAST(doc_QSpacerItem_isEmpty)},
    {SIP_MLNAME_CAST(sipName_maximumSize), meth_QSpacerItem_maximumSize, METH_VARARGS, SIP_MLDOC_CAST(doc_QSpacerItem_maximumSize)},
    {SIP_MLNAME_CAST(sipName_minimumSize), meth_QSpacerItem_minimumSize, METH_VARARGS, SIP_MLDOC_CAST(doc_QSpacerItem_minimumSize)},
    {SIP_MLNAME_CAST(sipName_setGeometry), meth_QSpacerItem_setGeometry, METH_VARARGS, SIP_MLDOC_CAST(doc_QSpacerItem_setGeometry)},
    {SIP_MLNAME_CAST(sipName_sizeHint), meth_QSpacerItem_sizeHint, METH_VARARGS, SIP_MLDOC_CAST(doc_QSpacerItem_sizeHint)},
    {SIP_MLNAME_CAST(sipName_spacerItem), meth_QSpacerItem_spacerItem, METH_VARARGS, SIP_MLDOC_CAST(doc_QSpacerItem_spacerItem)}
};

PyDoc_STRVAR(doc_QSpacerItem, "\1QSpacerItem(int, int, hPolicy: QSizePolicy.Policy = QSizePolicy.Minimum, vPolicy: QSizePolicy.Policy = QSizePolicy.Minimum)\n"
    "QSpacerItem(QSpacerItem)");


static pyqt4ClassPluginDef plugin_QSpacerItem = {
    0,
    0,
    0
};


sipClassTypeDef sipTypeDef_QtGui_QSpacerItem = {
    {
        -1,
        0,
        0,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_QSpacerItem,
        {0},
        &plugin_QSpacerItem
    },
    {
        sipNameNr_QSpacerItem,
        {0, 0, 1},
        9, methods_QSpacerItem,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QSpacerItem,
    -1,
    -1,
    supers_QSpacerItem,
    0,
    init_type_QSpacerItem,
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
    dealloc_QSpacerItem,
    0,
    0,
    0,
    release_QSpacerItem,
    cast_QSpacerItem,
    0,
    0,
    0,
    0,
    0,
    0
};
