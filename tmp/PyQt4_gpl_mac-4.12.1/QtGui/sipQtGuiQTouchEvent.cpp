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

#line 926 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qevent.sip"
#include <qevent.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQTouchEvent.cpp"

#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQTouchEvent.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 36 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQTouchEvent.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 39 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQTouchEvent.cpp"
#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qlist.sip"
#include <qlist.h>
#line 42 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQTouchEvent.cpp"
#line 926 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qevent.sip"
#include <qevent.h>
#line 933 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qevent.sip"
#include <qevent.h>
#line 47 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQTouchEvent.cpp"
#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qwidget.sip"
#include <qwidget.h>
#line 50 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQTouchEvent.cpp"


class sipQTouchEvent : public  ::QTouchEvent
{
public:
    sipQTouchEvent( ::QEvent::Type, ::QTouchEvent::DeviceType, ::Qt::KeyboardModifiers, ::Qt::TouchPointStates,const QList< ::QTouchEvent::TouchPoint>&);
    sipQTouchEvent(const  ::QTouchEvent&);
    ~sipQTouchEvent();

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipQTouchEvent(const sipQTouchEvent &);
    sipQTouchEvent &operator = (const sipQTouchEvent &);
};

sipQTouchEvent::sipQTouchEvent( ::QEvent::Type a0, ::QTouchEvent::DeviceType a1, ::Qt::KeyboardModifiers a2, ::Qt::TouchPointStates a3,const QList< ::QTouchEvent::TouchPoint>& a4):  ::QTouchEvent(a0,a1,a2,a3,a4), sipPySelf(0)
{
}

sipQTouchEvent::sipQTouchEvent(const  ::QTouchEvent& a0):  ::QTouchEvent(a0), sipPySelf(0)
{
}

sipQTouchEvent::~sipQTouchEvent()
{
    sipInstanceDestroyed(sipPySelf);
}


PyDoc_STRVAR(doc_QTouchEvent_widget, "widget(self) -> QWidget");

extern "C" {static PyObject *meth_QTouchEvent_widget(PyObject *, PyObject *);}
static PyObject *meth_QTouchEvent_widget(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QTouchEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QTouchEvent, &sipCpp))
        {
             ::QWidget*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->widget();
            Py_END_ALLOW_THREADS

            return sipConvertFromType(sipRes,sipType_QWidget,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QTouchEvent, sipName_widget, doc_QTouchEvent_widget);

    return NULL;
}


PyDoc_STRVAR(doc_QTouchEvent_deviceType, "deviceType(self) -> QTouchEvent.DeviceType");

extern "C" {static PyObject *meth_QTouchEvent_deviceType(PyObject *, PyObject *);}
static PyObject *meth_QTouchEvent_deviceType(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QTouchEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QTouchEvent, &sipCpp))
        {
             ::QTouchEvent::DeviceType sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->deviceType();
            Py_END_ALLOW_THREADS

            return sipConvertFromEnum(sipRes,sipType_QTouchEvent_DeviceType);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QTouchEvent, sipName_deviceType, doc_QTouchEvent_deviceType);

    return NULL;
}


PyDoc_STRVAR(doc_QTouchEvent_touchPointStates, "touchPointStates(self) -> Qt.TouchPointStates");

extern "C" {static PyObject *meth_QTouchEvent_touchPointStates(PyObject *, PyObject *);}
static PyObject *meth_QTouchEvent_touchPointStates(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QTouchEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QTouchEvent, &sipCpp))
        {
             ::Qt::TouchPointStates*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::Qt::TouchPointStates(sipCpp->touchPointStates());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_Qt_TouchPointStates,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QTouchEvent, sipName_touchPointStates, doc_QTouchEvent_touchPointStates);

    return NULL;
}


PyDoc_STRVAR(doc_QTouchEvent_touchPoints, "touchPoints(self) -> List[QTouchEvent.TouchPoint]");

extern "C" {static PyObject *meth_QTouchEvent_touchPoints(PyObject *, PyObject *);}
static PyObject *meth_QTouchEvent_touchPoints(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QTouchEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QTouchEvent, &sipCpp))
        {
            QList< ::QTouchEvent::TouchPoint>*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QList< ::QTouchEvent::TouchPoint>(sipCpp->touchPoints());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QList_0100QTouchEvent_TouchPoint,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QTouchEvent, sipName_touchPoints, doc_QTouchEvent_touchPoints);

    return NULL;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_QTouchEvent(void *, const sipTypeDef *);}
static void *cast_QTouchEvent(void *sipCppV, const sipTypeDef *targetType)
{
     ::QTouchEvent *sipCpp = reinterpret_cast< ::QTouchEvent *>(sipCppV);

    if (targetType == sipType_QInputEvent)
        return static_cast< ::QInputEvent *>(sipCpp);

    if (targetType == sipType_QEvent)
        return static_cast< ::QEvent *>(sipCpp);

    return sipCppV;
}


/* Call the instance's destructor. */
extern "C" {static void release_QTouchEvent(void *, int);}
static void release_QTouchEvent(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipQTouchEvent *>(sipCppV);
    else
        delete reinterpret_cast< ::QTouchEvent *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QTouchEvent(sipSimpleWrapper *);}
static void dealloc_QTouchEvent(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipQTouchEvent *>(sipGetAddress(sipSelf))->sipPySelf = NULL;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_QTouchEvent(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_QTouchEvent(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QTouchEvent(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipQTouchEvent *sipCpp = 0;

    {
         ::QEvent::Type a0;
         ::QTouchEvent::DeviceType a1 = QTouchEvent::TouchScreen;
         ::Qt::KeyboardModifiers a2def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
         ::Qt::TouchPointStates a3def = 0;
         ::Qt::TouchPointStates* a3 = &a3def;
        int a3State = 0;
        const QList< ::QTouchEvent::TouchPoint>& a4def = QList<QTouchEvent::TouchPoint>();
        const QList< ::QTouchEvent::TouchPoint>* a4 = &a4def;
        int a4State = 0;

        static const char *sipKwdList[] = {
            NULL,
            sipName_deviceType,
            sipName_modifiers,
            sipName_touchPointStates,
            sipName_touchPoints,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "E|EJ1J1J1", sipType_QEvent_Type, &a0, sipType_QTouchEvent_DeviceType, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, sipType_Qt_TouchPointStates, &a3, &a3State, sipType_QList_0100QTouchEvent_TouchPoint,&a4, &a4State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQTouchEvent(a0,a1,*a2,*a3,*a4);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);
            sipReleaseType(a3,sipType_Qt_TouchPointStates,a3State);
            sipReleaseType(const_cast<QList< ::QTouchEvent::TouchPoint> *>(a4),sipType_QList_0100QTouchEvent_TouchPoint,a4State);

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    {
        const  ::QTouchEvent* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J9", sipType_QTouchEvent, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQTouchEvent(*a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_QTouchEvent[] = {{251, 255, 1}};


static PyMethodDef methods_QTouchEvent[] = {
    {SIP_MLNAME_CAST(sipName_deviceType), meth_QTouchEvent_deviceType, METH_VARARGS, SIP_MLDOC_CAST(doc_QTouchEvent_deviceType)},
    {SIP_MLNAME_CAST(sipName_touchPointStates), meth_QTouchEvent_touchPointStates, METH_VARARGS, SIP_MLDOC_CAST(doc_QTouchEvent_touchPointStates)},
    {SIP_MLNAME_CAST(sipName_touchPoints), meth_QTouchEvent_touchPoints, METH_VARARGS, SIP_MLDOC_CAST(doc_QTouchEvent_touchPoints)},
    {SIP_MLNAME_CAST(sipName_widget), meth_QTouchEvent_widget, METH_VARARGS, SIP_MLDOC_CAST(doc_QTouchEvent_widget)}
};

static sipEnumMemberDef enummembers_QTouchEvent[] = {
    {sipName_TouchPad, static_cast<int>( ::QTouchEvent::TouchPad), 721},
    {sipName_TouchScreen, static_cast<int>( ::QTouchEvent::TouchScreen), 721},
};

PyDoc_STRVAR(doc_QTouchEvent, "\1QTouchEvent(QEvent.Type, deviceType: QTouchEvent.DeviceType = QTouchEvent.TouchScreen, modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, touchPointStates: Union[Qt.TouchPointStates, Qt.TouchPointState] = 0, touchPoints: object = QList&lt;QTouchEvent.TouchPoint&gt;())\n"
    "QTouchEvent(QTouchEvent)");


static pyqt4ClassPluginDef plugin_QTouchEvent = {
    0,
    0,
    0
};


sipClassTypeDef sipTypeDef_QtGui_QTouchEvent = {
    {
        -1,
        0,
        0,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_QTouchEvent,
        {0},
        &plugin_QTouchEvent
    },
    {
        sipNameNr_QTouchEvent,
        {0, 0, 1},
        4, methods_QTouchEvent,
        2, enummembers_QTouchEvent,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QTouchEvent,
    -1,
    -1,
    supers_QTouchEvent,
    0,
    init_type_QTouchEvent,
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
    dealloc_QTouchEvent,
    0,
    0,
    0,
    release_QTouchEvent,
    cast_QTouchEvent,
    0,
    0,
    0,
    0,
    0,
    0
};
