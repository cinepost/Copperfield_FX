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

#include "sipAPIQtTest.h"

#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtTest/qtestcase.sip"
#include <qtestcase.h>
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtTest/qtestkeyboard.sip"
#include <qtestkeyboard.h>
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtTest/qtestmouse.sip"
#include <qtestmouse.h>
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtTest/qtestsystem.sip"
#include <qtestsystem.h>
#line 35 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtTest/sipQtTestQTest.cpp"

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qwidget.sip"
#include <qwidget.h>
#line 39 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtTest/sipQtTestQTest.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 42 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtTest/sipQtTestQTest.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 45 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtTest/sipQtTestQTest.cpp"
#line 27 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qstring.sip"
#include <qstring.h>
#line 48 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtTest/sipQtTestQTest.cpp"
#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qpoint.sip"
#include <qpoint.h>
#line 51 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtTest/sipQtTestQTest.cpp"


PyDoc_STRVAR(doc_QTest_qWaitForWindowShown, "qWaitForWindowShown(QWidget) -> bool");

extern "C" {static PyObject *meth_QTest_qWaitForWindowShown(PyObject *, PyObject *);}
static PyObject *meth_QTest_qWaitForWindowShown(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;

        if (sipParseArgs(&sipParseErr, sipArgs, "J8", sipType_QWidget, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes =  ::QTest::qWaitForWindowShown(a0);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_qWaitForWindowShown, doc_QTest_qWaitForWindowShown);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_qWait, "qWait(int)");

extern "C" {static PyObject *meth_QTest_qWait(PyObject *, PyObject *);}
static PyObject *meth_QTest_qWait(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArgs, "i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::qWait(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_qWait, doc_QTest_qWait);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_mouseEvent, "mouseEvent(QTest.MouseAction, QWidget, Qt.MouseButton, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], QPoint, delay: int = -1)");

extern "C" {static PyObject *meth_QTest_mouseEvent(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_mouseEvent(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QTest::MouseAction a0;
         ::QWidget* a1;
         ::Qt::MouseButton a2;
         ::Qt::KeyboardModifiers* a3;
        int a3State = 0;
         ::QPoint* a4;
        int a5 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "EJ8EJ1J9|i", sipType_QTest_MouseAction, &a0, sipType_QWidget, &a1, sipType_Qt_MouseButton, &a2, sipType_Qt_KeyboardModifiers, &a3, &a3State, sipType_QPoint, &a4, &a5))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::mouseEvent(a0,a1,a2,*a3,*a4,a5);
            Py_END_ALLOW_THREADS
            sipReleaseType(a3,sipType_Qt_KeyboardModifiers,a3State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_mouseEvent, doc_QTest_mouseEvent);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_mouseRelease, "mouseRelease(QWidget, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = 0, pos: QPoint = QPoint(), delay: int = -1)");

extern "C" {static PyObject *meth_QTest_mouseRelease(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_mouseRelease(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;
         ::Qt::MouseButton a1;
         ::Qt::KeyboardModifiers a2def = 0;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
         ::QPoint a3def = QPoint();
         ::QPoint* a3 = &a3def;
        int a4 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_pos,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8E|J1J9i", sipType_QWidget, &a0, sipType_Qt_MouseButton, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, sipType_QPoint, &a3, &a4))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::mouseRelease(a0,a1,*a2,*a3,a4);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_mouseRelease, doc_QTest_mouseRelease);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_mousePress, "mousePress(QWidget, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = 0, pos: QPoint = QPoint(), delay: int = -1)");

extern "C" {static PyObject *meth_QTest_mousePress(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_mousePress(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;
         ::Qt::MouseButton a1;
         ::Qt::KeyboardModifiers a2def = 0;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
         ::QPoint a3def = QPoint();
         ::QPoint* a3 = &a3def;
        int a4 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_pos,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8E|J1J9i", sipType_QWidget, &a0, sipType_Qt_MouseButton, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, sipType_QPoint, &a3, &a4))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::mousePress(a0,a1,*a2,*a3,a4);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_mousePress, doc_QTest_mousePress);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_mouseMove, "mouseMove(QWidget, pos: QPoint = QPoint(), delay: int = -1)");

extern "C" {static PyObject *meth_QTest_mouseMove(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_mouseMove(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;
         ::QPoint a1def = QPoint();
         ::QPoint* a1 = &a1def;
        int a2 = -1;

        static const char *sipKwdList[] = {
            NULL,
            sipName_pos,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8|J9i", sipType_QWidget, &a0, sipType_QPoint, &a1, &a2))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::mouseMove(a0,*a1,a2);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_mouseMove, doc_QTest_mouseMove);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_mouseDClick, "mouseDClick(QWidget, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = 0, pos: QPoint = QPoint(), delay: int = -1)");

extern "C" {static PyObject *meth_QTest_mouseDClick(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_mouseDClick(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;
         ::Qt::MouseButton a1;
         ::Qt::KeyboardModifiers a2def = 0;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
         ::QPoint a3def = QPoint();
         ::QPoint* a3 = &a3def;
        int a4 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_pos,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8E|J1J9i", sipType_QWidget, &a0, sipType_Qt_MouseButton, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, sipType_QPoint, &a3, &a4))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::mouseDClick(a0,a1,*a2,*a3,a4);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_mouseDClick, doc_QTest_mouseDClick);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_mouseClick, "mouseClick(QWidget, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = 0, pos: QPoint = QPoint(), delay: int = -1)");

extern "C" {static PyObject *meth_QTest_mouseClick(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_mouseClick(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;
         ::Qt::MouseButton a1;
         ::Qt::KeyboardModifiers a2def = 0;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
         ::QPoint a3def = QPoint();
         ::QPoint* a3 = &a3def;
        int a4 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_pos,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8E|J1J9i", sipType_QWidget, &a0, sipType_Qt_MouseButton, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, sipType_QPoint, &a3, &a4))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::mouseClick(a0,a1,*a2,*a3,a4);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_mouseClick, doc_QTest_mouseClick);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_keyRelease, "keyRelease(QWidget, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)\n"
    "keyRelease(QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)");

extern "C" {static PyObject *meth_QTest_keyRelease(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_keyRelease(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;
         ::Qt::Key a1;
         ::Qt::KeyboardModifiers a2def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
        int a3 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8E|J1i", sipType_QWidget, &a0, sipType_Qt_Key, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, &a3))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::keyRelease(a0,a1,*a2,a3);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    {
         ::QWidget* a0;
        char a1;
         ::Qt::KeyboardModifiers a2def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
        int a3 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8c|J1i", sipType_QWidget, &a0, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, &a3))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::keyRelease(a0,a1,*a2,a3);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_keyRelease, doc_QTest_keyRelease);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_keyPress, "keyPress(QWidget, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)\n"
    "keyPress(QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)");

extern "C" {static PyObject *meth_QTest_keyPress(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_keyPress(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;
         ::Qt::Key a1;
         ::Qt::KeyboardModifiers a2def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
        int a3 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8E|J1i", sipType_QWidget, &a0, sipType_Qt_Key, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, &a3))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::keyPress(a0,a1,*a2,a3);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    {
         ::QWidget* a0;
        char a1;
         ::Qt::KeyboardModifiers a2def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
        int a3 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8c|J1i", sipType_QWidget, &a0, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, &a3))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::keyPress(a0,a1,*a2,a3);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_keyPress, doc_QTest_keyPress);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_keyEvent, "keyEvent(QTest.KeyAction, QWidget, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)\n"
    "keyEvent(QTest.KeyAction, QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)");

extern "C" {static PyObject *meth_QTest_keyEvent(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_keyEvent(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QTest::KeyAction a0;
         ::QWidget* a1;
         ::Qt::Key a2;
         ::Qt::KeyboardModifiers a3def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a3 = &a3def;
        int a3State = 0;
        int a4 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            NULL,
            sipName_modifier,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "EJ8E|J1i", sipType_QTest_KeyAction, &a0, sipType_QWidget, &a1, sipType_Qt_Key, &a2, sipType_Qt_KeyboardModifiers, &a3, &a3State, &a4))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::keyEvent(a0,a1,a2,*a3,a4);
            Py_END_ALLOW_THREADS
            sipReleaseType(a3,sipType_Qt_KeyboardModifiers,a3State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    {
         ::QTest::KeyAction a0;
         ::QWidget* a1;
        char a2;
         ::Qt::KeyboardModifiers a3def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a3 = &a3def;
        int a3State = 0;
        int a4 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            NULL,
            sipName_modifier,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "EJ8c|J1i", sipType_QTest_KeyAction, &a0, sipType_QWidget, &a1, &a2, sipType_Qt_KeyboardModifiers, &a3, &a3State, &a4))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::keyEvent(a0,a1,a2,*a3,a4);
            Py_END_ALLOW_THREADS
            sipReleaseType(a3,sipType_Qt_KeyboardModifiers,a3State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_keyEvent, doc_QTest_keyEvent);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_keyClicks, "keyClicks(QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)");

extern "C" {static PyObject *meth_QTest_keyClicks(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_keyClicks(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;
        const  ::QString* a1;
        int a1State = 0;
         ::Qt::KeyboardModifiers a2def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
        int a3 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8J1|J1i", sipType_QWidget, &a0, sipType_QString,&a1, &a1State, sipType_Qt_KeyboardModifiers, &a2, &a2State, &a3))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::keyClicks(a0,*a1,*a2,a3);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a1),sipType_QString,a1State);
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_keyClicks, doc_QTest_keyClicks);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_keyClick, "keyClick(QWidget, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)\n"
    "keyClick(QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)");

extern "C" {static PyObject *meth_QTest_keyClick(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_QTest_keyClick(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = NULL;

    {
         ::QWidget* a0;
         ::Qt::Key a1;
         ::Qt::KeyboardModifiers a2def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
        int a3 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8E|J1i", sipType_QWidget, &a0, sipType_Qt_Key, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, &a3))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::keyClick(a0,a1,*a2,a3);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    {
         ::QWidget* a0;
        char a1;
         ::Qt::KeyboardModifiers a2def = Qt::NoModifier;
         ::Qt::KeyboardModifiers* a2 = &a2def;
        int a2State = 0;
        int a3 = -1;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_modifier,
            sipName_delay,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, NULL, "J8c|J1i", sipType_QWidget, &a0, &a1, sipType_Qt_KeyboardModifiers, &a2, &a2State, &a3))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::keyClick(a0,a1,*a2,a3);
            Py_END_ALLOW_THREADS
            sipReleaseType(a2,sipType_Qt_KeyboardModifiers,a2State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_keyClick, doc_QTest_keyClick);

    return NULL;
}


PyDoc_STRVAR(doc_QTest_qSleep, "qSleep(int)");

extern "C" {static PyObject *meth_QTest_qSleep(PyObject *, PyObject *);}
static PyObject *meth_QTest_qSleep(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;

        if (sipParseArgs(&sipParseErr, sipArgs, "i", &a0))
        {
            Py_BEGIN_ALLOW_THREADS
             ::QTest::qSleep(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoFunction(sipParseErr, sipName_qSleep, doc_QTest_qSleep);

    return NULL;
}


static PyMethodDef methods_QTest[] = {
    {SIP_MLNAME_CAST(sipName_keyClick), (PyCFunction)meth_QTest_keyClick, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_keyClick)},
    {SIP_MLNAME_CAST(sipName_keyClicks), (PyCFunction)meth_QTest_keyClicks, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_keyClicks)},
    {SIP_MLNAME_CAST(sipName_keyEvent), (PyCFunction)meth_QTest_keyEvent, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_keyEvent)},
    {SIP_MLNAME_CAST(sipName_keyPress), (PyCFunction)meth_QTest_keyPress, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_keyPress)},
    {SIP_MLNAME_CAST(sipName_keyRelease), (PyCFunction)meth_QTest_keyRelease, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_keyRelease)},
    {SIP_MLNAME_CAST(sipName_mouseClick), (PyCFunction)meth_QTest_mouseClick, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_mouseClick)},
    {SIP_MLNAME_CAST(sipName_mouseDClick), (PyCFunction)meth_QTest_mouseDClick, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_mouseDClick)},
    {SIP_MLNAME_CAST(sipName_mouseEvent), (PyCFunction)meth_QTest_mouseEvent, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_mouseEvent)},
    {SIP_MLNAME_CAST(sipName_mouseMove), (PyCFunction)meth_QTest_mouseMove, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_mouseMove)},
    {SIP_MLNAME_CAST(sipName_mousePress), (PyCFunction)meth_QTest_mousePress, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_mousePress)},
    {SIP_MLNAME_CAST(sipName_mouseRelease), (PyCFunction)meth_QTest_mouseRelease, METH_VARARGS|METH_KEYWORDS, SIP_MLDOC_CAST(doc_QTest_mouseRelease)},
    {SIP_MLNAME_CAST(sipName_qSleep), meth_QTest_qSleep, METH_VARARGS, SIP_MLDOC_CAST(doc_QTest_qSleep)},
    {SIP_MLNAME_CAST(sipName_qWait), meth_QTest_qWait, METH_VARARGS, SIP_MLDOC_CAST(doc_QTest_qWait)},
    {SIP_MLNAME_CAST(sipName_qWaitForWindowShown), meth_QTest_qWaitForWindowShown, METH_VARARGS, SIP_MLDOC_CAST(doc_QTest_qWaitForWindowShown)}
};

static sipEnumMemberDef enummembers_QTest[] = {
    {sipName_Click, static_cast<int>( ::QTest::Click), 1},
    {sipName_MouseClick, static_cast<int>( ::QTest::MouseClick), 2},
    {sipName_MouseDClick, static_cast<int>( ::QTest::MouseDClick), 2},
    {sipName_MouseMove, static_cast<int>( ::QTest::MouseMove), 2},
    {sipName_MousePress, static_cast<int>( ::QTest::MousePress), 2},
    {sipName_MouseRelease, static_cast<int>( ::QTest::MouseRelease), 2},
    {sipName_Press, static_cast<int>( ::QTest::Press), 1},
    {sipName_Release, static_cast<int>( ::QTest::Release), 1},
};


static pyqt4ClassPluginDef plugin_QTest = {
    0,
    0,
    0
};


sipClassTypeDef sipTypeDef_QtTest_QTest = {
    {
        -1,
        0,
        0,
        SIP_TYPE_NAMESPACE,
        sipNameNr_QTest,
        {0},
        &plugin_QTest
    },
    {
        sipNameNr_QTest,
        {0, 0, 1},
        14, methods_QTest,
        8, enummembers_QTest,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    0,
    -1,
    -1,
    0,
    0,
    0,
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
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
};
