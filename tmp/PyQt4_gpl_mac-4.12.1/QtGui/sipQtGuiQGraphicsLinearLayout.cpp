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

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qgraphicslinearlayout.sip"
#include <qgraphicslinearlayout.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qgraphicslayoutitem.sip"
#include <qgraphicslayoutitem.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 36 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"
#line 103 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qsize.sip"
#include <qsize.h>
#line 39 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"
#line 159 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qrect.sip"
#include <qrect.h>
#line 42 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 45 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 48 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"
#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qgraphicsitem.sip"
#include <qgraphicsitem.h>
#line 51 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qsizepolicy.sip"
#include <qsizepolicy.h>
#line 54 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"


class sipQGraphicsLinearLayout : public  ::QGraphicsLinearLayout
{
public:
    sipQGraphicsLinearLayout( ::QGraphicsLayoutItem*);
    sipQGraphicsLinearLayout( ::Qt::Orientation, ::QGraphicsLayoutItem*);
    virtual ~sipQGraphicsLinearLayout();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
     ::QSizeF sizeHint( ::Qt::SizeHint,const  ::QSizeF&) const;
    void updateGeometry();
    void getContentsMargins( ::qreal*, ::qreal*, ::qreal*, ::qreal*) const;
    void setGeometry(const  ::QRectF&);
    void invalidate();
    void widgetEvent( ::QEvent*);
    int count() const;
     ::QGraphicsLayoutItem* itemAt(int) const;
    void removeAt(int);

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipQGraphicsLinearLayout(const sipQGraphicsLinearLayout &);
    sipQGraphicsLinearLayout &operator = (const sipQGraphicsLinearLayout &);

    char sipPyMethods[9];
};

sipQGraphicsLinearLayout::sipQGraphicsLinearLayout( ::QGraphicsLayoutItem*a0):  ::QGraphicsLinearLayout(a0), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQGraphicsLinearLayout::sipQGraphicsLinearLayout( ::Qt::Orientation a0, ::QGraphicsLayoutItem*a1):  ::QGraphicsLinearLayout(a0,a1), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQGraphicsLinearLayout::~sipQGraphicsLinearLayout()
{
    sipInstanceDestroyed(sipPySelf);
}

 ::QSizeF sipQGraphicsLinearLayout::sizeHint( ::Qt::SizeHint a0,const  ::QSizeF& a1) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[0]),sipPySelf,NULL,sipName_sizeHint);

    if (!sipMeth)
        return  ::QGraphicsLinearLayout::sizeHint(a0,a1);

    extern  ::QSizeF sipVH_QtGui_149(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *,  ::Qt::SizeHint,const  ::QSizeF&);

    return sipVH_QtGui_149(sipGILState, 0, sipPySelf, sipMeth, a0, a1);
}

void sipQGraphicsLinearLayout::updateGeometry()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[1],sipPySelf,NULL,sipName_updateGeometry);

    if (!sipMeth)
    {
         ::QGraphicsLinearLayout::updateGeometry();
        return;
    }

    extern void sipVH_QtGui_34(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    sipVH_QtGui_34(sipGILState, 0, sipPySelf, sipMeth);
}

void sipQGraphicsLinearLayout::getContentsMargins( ::qreal*a0, ::qreal*a1, ::qreal*a2, ::qreal*a3) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[2]),sipPySelf,NULL,sipName_getContentsMargins);

    if (!sipMeth)
    {
         ::QGraphicsLinearLayout::getContentsMargins(a0,a1,a2,a3);
        return;
    }

    extern void sipVH_QtGui_148(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *,  ::qreal*, ::qreal*, ::qreal*, ::qreal*);

    sipVH_QtGui_148(sipGILState, 0, sipPySelf, sipMeth, a0, a1, a2, a3);
}

void sipQGraphicsLinearLayout::setGeometry(const  ::QRectF& a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[3],sipPySelf,NULL,sipName_setGeometry);

    if (!sipMeth)
    {
         ::QGraphicsLinearLayout::setGeometry(a0);
        return;
    }

    extern void sipVH_QtGui_147(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const  ::QRectF&);

    sipVH_QtGui_147(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQGraphicsLinearLayout::invalidate()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[4],sipPySelf,NULL,sipName_invalidate);

    if (!sipMeth)
    {
         ::QGraphicsLinearLayout::invalidate();
        return;
    }

    extern void sipVH_QtGui_34(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    sipVH_QtGui_34(sipGILState, 0, sipPySelf, sipMeth);
}

void sipQGraphicsLinearLayout::widgetEvent( ::QEvent*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[5],sipPySelf,NULL,sipName_widgetEvent);

    if (!sipMeth)
    {
         ::QGraphicsLinearLayout::widgetEvent(a0);
        return;
    }

    extern void sipVH_QtGui_3(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *,  ::QEvent*);

    sipVH_QtGui_3(sipGILState, 0, sipPySelf, sipMeth, a0);
}

int sipQGraphicsLinearLayout::count() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[6]),sipPySelf,NULL,sipName_count);

    if (!sipMeth)
        return  ::QGraphicsLinearLayout::count();

    extern int sipVH_QtGui_8(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_8(sipGILState, 0, sipPySelf, sipMeth);
}

 ::QGraphicsLayoutItem* sipQGraphicsLinearLayout::itemAt(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[7]),sipPySelf,NULL,sipName_itemAt);

    if (!sipMeth)
        return  ::QGraphicsLinearLayout::itemAt(a0);

    extern  ::QGraphicsLayoutItem* sipVH_QtGui_150(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    return sipVH_QtGui_150(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQGraphicsLinearLayout::removeAt(int a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[8],sipPySelf,NULL,sipName_removeAt);

    if (!sipMeth)
    {
         ::QGraphicsLinearLayout::removeAt(a0);
        return;
    }

    extern void sipVH_QtGui_54(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    sipVH_QtGui_54(sipGILState, 0, sipPySelf, sipMeth, a0);
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_setOrientation, "setOrientation(self, Qt.Orientation)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_setOrientation(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_setOrientation(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::Qt::Orientation a0;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BE", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, sipType_Qt_Orientation, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setOrientation(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_setOrientation, doc_QGraphicsLinearLayout_setOrientation);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_orientation, "orientation(self) -> Qt.Orientation");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_orientation(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_orientation(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp))
        {
             ::Qt::Orientation sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->orientation();
            Py_END_ALLOW_THREADS

            return sipConvertFromEnum(sipRes,sipType_Qt_Orientation);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_orientation, doc_QGraphicsLinearLayout_orientation);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_addItem, "addItem(self, QGraphicsLayoutItem)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_addItem(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_addItem(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::QGraphicsLayoutItem* a0;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ:", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, sipType_QGraphicsLayoutItem, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->addItem(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_addItem, doc_QGraphicsLinearLayout_addItem);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_addStretch, "addStretch(self, stretch: int = 1)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_addStretch(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_addStretch(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
        int a0 = 1;
         ::QGraphicsLinearLayout *sipCpp;

        static const char *sipKwdList[] = {
            sipName_stretch,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "B|i", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->addStretch(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_addStretch, doc_QGraphicsLinearLayout_addStretch);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_insertItem, "insertItem(self, int, QGraphicsLayoutItem)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_insertItem(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_insertItem(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;
         ::QGraphicsLayoutItem* a1;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BiJ:", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, &a0, sipType_QGraphicsLayoutItem, &a1))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->insertItem(a0,a1);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_insertItem, doc_QGraphicsLinearLayout_insertItem);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_insertStretch, "insertStretch(self, int, stretch: int = 1)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_insertStretch(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_insertStretch(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;
        int a1 = 1;
         ::QGraphicsLinearLayout *sipCpp;

        static const char *sipKwdList[] = {
            NULL,
            sipName_stretch,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "Bi|i", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, &a0, &a1))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->insertStretch(a0,a1);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_insertStretch, doc_QGraphicsLinearLayout_insertStretch);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_removeItem, "removeItem(self, QGraphicsLayoutItem)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_removeItem(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_removeItem(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::QGraphicsLayoutItem* a0;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ<", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, sipType_QGraphicsLayoutItem, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->removeItem(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_removeItem, doc_QGraphicsLinearLayout_removeItem);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_removeAt, "removeAt(self, int)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_removeAt(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_removeAt(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        int a0;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bi", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, &a0))
        {
#line 44 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qgraphicslinearlayout.sip"
        // The ownership of any existing item must be passed back to Python.
        QGraphicsLayoutItem *itm;
        
        if (a0 < sipCpp->count())
            itm = sipCpp->itemAt(a0);
        else
            itm = 0;
        
        Py_BEGIN_ALLOW_THREADS
        sipSelfWasArg ? sipCpp->QGraphicsLinearLayout::removeAt(a0)
                      : sipCpp->removeAt(a0);
        Py_END_ALLOW_THREADS
        
        // The Qt documentation isn't quite correct as ownership isn't always passed
        // back to the caller.
        if (itm && !itm->parentLayoutItem())
        {
            PyObject *itmo = sipGetPyObject(itm, sipType_QGraphicsLayoutItem);
        
            if (itmo)
                sipTransferBack(itmo);
        }
#line 517 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQGraphicsLinearLayout.cpp"

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_removeAt, doc_QGraphicsLinearLayout_removeAt);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_setSpacing, "setSpacing(self, float)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_setSpacing(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_setSpacing(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::qreal a0;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bd", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setSpacing(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_setSpacing, doc_QGraphicsLinearLayout_setSpacing);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_spacing, "spacing(self) -> float");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_spacing(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_spacing(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp))
        {
             ::qreal sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->spacing();
            Py_END_ALLOW_THREADS

            return PyFloat_FromDouble(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_spacing, doc_QGraphicsLinearLayout_spacing);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_setItemSpacing, "setItemSpacing(self, int, float)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_setItemSpacing(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_setItemSpacing(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;
         ::qreal a1;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bid", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, &a0, &a1))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setItemSpacing(a0,a1);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_setItemSpacing, doc_QGraphicsLinearLayout_setItemSpacing);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_itemSpacing, "itemSpacing(self, int) -> float");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_itemSpacing(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_itemSpacing(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;
        const  ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bi", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, &a0))
        {
             ::qreal sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->itemSpacing(a0);
            Py_END_ALLOW_THREADS

            return PyFloat_FromDouble(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_itemSpacing, doc_QGraphicsLinearLayout_itemSpacing);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_setStretchFactor, "setStretchFactor(self, QGraphicsLayoutItem, int)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_setStretchFactor(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_setStretchFactor(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::QGraphicsLayoutItem* a0;
        int a1;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ8i", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, sipType_QGraphicsLayoutItem, &a0, &a1))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setStretchFactor(a0,a1);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_setStretchFactor, doc_QGraphicsLinearLayout_setStretchFactor);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_stretchFactor, "stretchFactor(self, QGraphicsLayoutItem) -> int");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_stretchFactor(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_stretchFactor(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::QGraphicsLayoutItem* a0;
        const  ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ8", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, sipType_QGraphicsLayoutItem, &a0))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->stretchFactor(a0);
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_stretchFactor, doc_QGraphicsLinearLayout_stretchFactor);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_setAlignment, "setAlignment(self, QGraphicsLayoutItem, Union[Qt.Alignment, Qt.AlignmentFlag])");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_setAlignment(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_setAlignment(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::QGraphicsLayoutItem* a0;
         ::Qt::Alignment* a1;
        int a1State = 0;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ8J1", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, sipType_QGraphicsLayoutItem, &a0, sipType_Qt_Alignment, &a1, &a1State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setAlignment(a0,*a1);
            Py_END_ALLOW_THREADS
            sipReleaseType(a1,sipType_Qt_Alignment,a1State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_setAlignment, doc_QGraphicsLinearLayout_setAlignment);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_alignment, "alignment(self, QGraphicsLayoutItem) -> Qt.Alignment");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_alignment(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_alignment(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::QGraphicsLayoutItem* a0;
        const  ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ8", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, sipType_QGraphicsLayoutItem, &a0))
        {
             ::Qt::Alignment*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::Qt::Alignment(sipCpp->alignment(a0));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_Qt_Alignment,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_alignment, doc_QGraphicsLinearLayout_alignment);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_setGeometry, "setGeometry(self, QRectF)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_setGeometry(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_setGeometry(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QRectF* a0;
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ9", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, sipType_QRectF, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp-> ::QGraphicsLinearLayout::setGeometry(*a0) : sipCpp->setGeometry(*a0));
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_setGeometry, doc_QGraphicsLinearLayout_setGeometry);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_count, "count(self) -> int");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_count(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_count(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp-> ::QGraphicsLinearLayout::count() : sipCpp->count());
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_count, doc_QGraphicsLinearLayout_count);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_itemAt, "itemAt(self, int) -> QGraphicsLayoutItem");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_itemAt(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_itemAt(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        int a0;
        const  ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bi", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, &a0))
        {
             ::QGraphicsLayoutItem*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp-> ::QGraphicsLinearLayout::itemAt(a0) : sipCpp->itemAt(a0));
            Py_END_ALLOW_THREADS

            return sipConvertFromType(sipRes,sipType_QGraphicsLayoutItem,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_itemAt, doc_QGraphicsLinearLayout_itemAt);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_invalidate, "invalidate(self)");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_invalidate(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_invalidate(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
         ::QGraphicsLinearLayout *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp))
        {
            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp-> ::QGraphicsLinearLayout::invalidate() : sipCpp->invalidate());
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_invalidate, doc_QGraphicsLinearLayout_invalidate);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsLinearLayout_sizeHint, "sizeHint(self, Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF");

extern "C" {static PyObject *meth_QGraphicsLinearLayout_sizeHint(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QGraphicsLinearLayout_sizeHint(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
         ::Qt::SizeHint a0;
        const  ::QSizeF& a1def = QSizeF();
        const  ::QSizeF* a1 = &a1def;
        const  ::QGraphicsLinearLayout *sipCpp;

        static const char *sipKwdList[] = {
            NULL,
            sipName_constraint,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "BE|J9", &sipSelf, sipType_QGraphicsLinearLayout, &sipCpp, sipType_Qt_SizeHint, &a0, sipType_QSizeF, &a1))
        {
             ::QSizeF*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QSizeF((sipSelfWasArg ? sipCpp-> ::QGraphicsLinearLayout::sizeHint(a0,*a1) : sipCpp->sizeHint(a0,*a1)));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QSizeF,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsLinearLayout, sipName_sizeHint, doc_QGraphicsLinearLayout_sizeHint);

    return NULL;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_QGraphicsLinearLayout(void *, const sipTypeDef *);}
static void *cast_QGraphicsLinearLayout(void *sipCppV, const sipTypeDef *targetType)
{
     ::QGraphicsLinearLayout *sipCpp = reinterpret_cast< ::QGraphicsLinearLayout *>(sipCppV);

    if (targetType == sipType_QGraphicsLayout)
        return static_cast< ::QGraphicsLayout *>(sipCpp);

    if (targetType == sipType_QGraphicsLayoutItem)
        return static_cast< ::QGraphicsLayoutItem *>(sipCpp);

    return sipCppV;
}


/* Call the instance's destructor. */
extern "C" {static void release_QGraphicsLinearLayout(void *, int);}
static void release_QGraphicsLinearLayout(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipQGraphicsLinearLayout *>(sipCppV);
    else
        delete reinterpret_cast< ::QGraphicsLinearLayout *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QGraphicsLinearLayout(sipSimpleWrapper *);}
static void dealloc_QGraphicsLinearLayout(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipQGraphicsLinearLayout *>(sipGetAddress(sipSelf))->sipPySelf = NULL;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_QGraphicsLinearLayout(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_QGraphicsLinearLayout(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QGraphicsLinearLayout(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **sipOwner, PyObject **sipParseErr)
{
    sipQGraphicsLinearLayout *sipCpp = 0;

    {
         ::QGraphicsLayoutItem* a0 = 0;

        static const char *sipKwdList[] = {
            sipName_parent,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|JH", sipType_QGraphicsLayoutItem, &a0, sipOwner))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQGraphicsLinearLayout(a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    {
         ::Qt::Orientation a0;
         ::QGraphicsLayoutItem* a1 = 0;

        static const char *sipKwdList[] = {
            NULL,
            sipName_parent,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "E|JH", sipType_Qt_Orientation, &a0, sipType_QGraphicsLayoutItem, &a1, sipOwner))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQGraphicsLinearLayout(a0,a1);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_QGraphicsLinearLayout[] = {{178, 255, 1}};


static PyMethodDef methods_QGraphicsLinearLayout[] = {
    {SIP_MLNAME_CAST(sipName_addItem), meth_QGraphicsLinearLayout_addItem, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_addItem)},
    {SIP_MLNAME_CAST(sipName_addStretch), (PyCFunction)meth_QGraphicsLinearLayout_addStretch, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_addStretch)},
    {SIP_MLNAME_CAST(sipName_alignment), meth_QGraphicsLinearLayout_alignment, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_alignment)},
    {SIP_MLNAME_CAST(sipName_count), meth_QGraphicsLinearLayout_count, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_count)},
    {SIP_MLNAME_CAST(sipName_insertItem), meth_QGraphicsLinearLayout_insertItem, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_insertItem)},
    {SIP_MLNAME_CAST(sipName_insertStretch), (PyCFunction)meth_QGraphicsLinearLayout_insertStretch, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_insertStretch)},
    {SIP_MLNAME_CAST(sipName_invalidate), meth_QGraphicsLinearLayout_invalidate, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_invalidate)},
    {SIP_MLNAME_CAST(sipName_itemAt), meth_QGraphicsLinearLayout_itemAt, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_itemAt)},
    {SIP_MLNAME_CAST(sipName_itemSpacing), meth_QGraphicsLinearLayout_itemSpacing, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_itemSpacing)},
    {SIP_MLNAME_CAST(sipName_orientation), meth_QGraphicsLinearLayout_orientation, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_orientation)},
    {SIP_MLNAME_CAST(sipName_removeAt), meth_QGraphicsLinearLayout_removeAt, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_removeAt)},
    {SIP_MLNAME_CAST(sipName_removeItem), meth_QGraphicsLinearLayout_removeItem, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_removeItem)},
    {SIP_MLNAME_CAST(sipName_setAlignment), meth_QGraphicsLinearLayout_setAlignment, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_setAlignment)},
    {SIP_MLNAME_CAST(sipName_setGeometry), meth_QGraphicsLinearLayout_setGeometry, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_setGeometry)},
    {SIP_MLNAME_CAST(sipName_setItemSpacing), meth_QGraphicsLinearLayout_setItemSpacing, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_setItemSpacing)},
    {SIP_MLNAME_CAST(sipName_setOrientation), meth_QGraphicsLinearLayout_setOrientation, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_setOrientation)},
    {SIP_MLNAME_CAST(sipName_setSpacing), meth_QGraphicsLinearLayout_setSpacing, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_setSpacing)},
    {SIP_MLNAME_CAST(sipName_setStretchFactor), meth_QGraphicsLinearLayout_setStretchFactor, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_setStretchFactor)},
    {SIP_MLNAME_CAST(sipName_sizeHint), (PyCFunction)meth_QGraphicsLinearLayout_sizeHint, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_sizeHint)},
    {SIP_MLNAME_CAST(sipName_spacing), meth_QGraphicsLinearLayout_spacing, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_spacing)},
    {SIP_MLNAME_CAST(sipName_stretchFactor), meth_QGraphicsLinearLayout_stretchFactor, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsLinearLayout_stretchFactor)}
};

PyDoc_STRVAR(doc_QGraphicsLinearLayout, "\1QGraphicsLinearLayout(parent: QGraphicsLayoutItem = None)\n"
    "QGraphicsLinearLayout(Qt.Orientation, parent: QGraphicsLayoutItem = None)");


static pyqt4ClassPluginDef plugin_QGraphicsLinearLayout = {
    0,
    0,
    0
};


sipClassTypeDef sipTypeDef_QtGui_QGraphicsLinearLayout = {
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_QGraphicsLinearLayout,
        {0},
        &plugin_QGraphicsLinearLayout
    },
    {
        sipNameNr_QGraphicsLinearLayout,
        {0, 0, 1},
        21, methods_QGraphicsLinearLayout,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QGraphicsLinearLayout,
    -1,
    -1,
    supers_QGraphicsLinearLayout,
    0,
    init_type_QGraphicsLinearLayout,
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
    dealloc_QGraphicsLinearLayout,
    0,
    0,
    0,
    release_QGraphicsLinearLayout,
    cast_QGraphicsLinearLayout,
    0,
    0,
    0,
    0,
    0,
    0
};
