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

#line 28 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtNetwork/qhttp.sip"
#include <qhttp.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQHttpHeader.cpp"

#line 27 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qstring.sip"
#include <qstring.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQHttpHeader.cpp"
#line 27 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qstringlist.sip"
#include <qstringlist.h>
#line 36 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQHttpHeader.cpp"
#line 196 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qlist.sip"
#include <qlist.h>
#include <qpair.h>
#line 40 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQHttpHeader.cpp"
#line 68 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtCore/qstring.sip"
#include <qstring.h>
#line 43 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtNetwork/sipQtNetworkQHttpHeader.cpp"


class sipQHttpHeader : public  ::QHttpHeader
{
public:
    sipQHttpHeader();
    sipQHttpHeader(const  ::QHttpHeader&);
    sipQHttpHeader(const  ::QString&);
    virtual ~sipQHttpHeader();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    bool parseLine(const  ::QString&,int);
    int minorVersion() const;
    int majorVersion() const;
     ::QString toString() const;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipQHttpHeader(const sipQHttpHeader &);
    sipQHttpHeader &operator = (const sipQHttpHeader &);

    char sipPyMethods[4];
};

sipQHttpHeader::sipQHttpHeader():  ::QHttpHeader(), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQHttpHeader::sipQHttpHeader(const  ::QHttpHeader& a0):  ::QHttpHeader(a0), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQHttpHeader::sipQHttpHeader(const  ::QString& a0):  ::QHttpHeader(a0), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQHttpHeader::~sipQHttpHeader()
{
    sipInstanceDestroyed(sipPySelf);
}

bool sipQHttpHeader::parseLine(const  ::QString& a0,int a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[0],sipPySelf,NULL,sipName_parseLine);

    if (!sipMeth)
        return  ::QHttpHeader::parseLine(a0,a1);

    extern bool sipVH_QtNetwork_23(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const  ::QString&,int);

    return sipVH_QtNetwork_23(sipGILState, 0, sipPySelf, sipMeth, a0, a1);
}

int sipQHttpHeader::minorVersion() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[1]),sipPySelf,sipName_QHttpHeader,sipName_minorVersion);

    if (!sipMeth)
        return 0;

    extern int sipVH_QtNetwork_22(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtNetwork_22(sipGILState, 0, sipPySelf, sipMeth);
}

int sipQHttpHeader::majorVersion() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[2]),sipPySelf,sipName_QHttpHeader,sipName_majorVersion);

    if (!sipMeth)
        return 0;

    extern int sipVH_QtNetwork_22(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtNetwork_22(sipGILState, 0, sipPySelf, sipMeth);
}

 ::QString sipQHttpHeader::toString() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[3]),sipPySelf,NULL,sipName_toString);

    if (!sipMeth)
        return  ::QHttpHeader::toString();

    extern  ::QString sipVH_QtNetwork_21(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtNetwork_21(sipGILState, 0, sipPySelf, sipMeth);
}


PyDoc_STRVAR(doc_QHttpHeader_setValue, "setValue(self, str, str)");

extern "C" {static PyObject *meth_QHttpHeader_setValue(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_setValue(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QString* a0;
        int a0State = 0;
        const  ::QString* a1;
        int a1State = 0;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1J1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State, sipType_QString,&a1, &a1State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setValue(*a0,*a1);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);
            sipReleaseType(const_cast< ::QString *>(a1),sipType_QString,a1State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_setValue, doc_QHttpHeader_setValue);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_setValues, "setValues(self, Sequence[Tuple[Union[QString, QLatin1String, QChar, str], Union[QString, QLatin1String, QChar, str]]])");

extern "C" {static PyObject *meth_QHttpHeader_setValues(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_setValues(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QList<QPair<QString,QString> >* a0;
        int a0State = 0;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QList_0600QPair_0100QString_0100QString,&a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setValues(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QList<QPair<QString,QString> > *>(a0),sipType_QList_0600QPair_0100QString_0100QString,a0State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_setValues, doc_QHttpHeader_setValues);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_addValue, "addValue(self, str, str)");

extern "C" {static PyObject *meth_QHttpHeader_addValue(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_addValue(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QString* a0;
        int a0State = 0;
        const  ::QString* a1;
        int a1State = 0;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1J1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State, sipType_QString,&a1, &a1State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->addValue(*a0,*a1);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);
            sipReleaseType(const_cast< ::QString *>(a1),sipType_QString,a1State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_addValue, doc_QHttpHeader_addValue);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_values, "values(self) -> List[Tuple[QString, QString]]");

extern "C" {static PyObject *meth_QHttpHeader_values(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_values(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
            QList<QPair<QString,QString> >*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QList<QPair<QString,QString> >(sipCpp->values());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QList_0600QPair_0100QString_0100QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_values, doc_QHttpHeader_values);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_hasKey, "hasKey(self, str) -> bool");

extern "C" {static PyObject *meth_QHttpHeader_hasKey(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_hasKey(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QString* a0;
        int a0State = 0;
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->hasKey(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_hasKey, doc_QHttpHeader_hasKey);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_keys, "keys(self) -> List[str]");

extern "C" {static PyObject *meth_QHttpHeader_keys(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_keys(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
             ::QStringList*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QStringList(sipCpp->keys());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QStringList,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_keys, doc_QHttpHeader_keys);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_value, "value(self, str) -> str");

extern "C" {static PyObject *meth_QHttpHeader_value(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_value(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QString* a0;
        int a0State = 0;
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State))
        {
             ::QString*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QString(sipCpp->value(*a0));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_value, doc_QHttpHeader_value);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_allValues, "allValues(self, str) -> List[str]");

extern "C" {static PyObject *meth_QHttpHeader_allValues(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_allValues(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QString* a0;
        int a0State = 0;
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State))
        {
             ::QStringList*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QStringList(sipCpp->allValues(*a0));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);

            return sipConvertFromNewType(sipRes,sipType_QStringList,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_allValues, doc_QHttpHeader_allValues);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_removeValue, "removeValue(self, str)");

extern "C" {static PyObject *meth_QHttpHeader_removeValue(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_removeValue(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QString* a0;
        int a0State = 0;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->removeValue(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_removeValue, doc_QHttpHeader_removeValue);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_removeAllValues, "removeAllValues(self, str)");

extern "C" {static PyObject *meth_QHttpHeader_removeAllValues(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_removeAllValues(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QString* a0;
        int a0State = 0;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->removeAllValues(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_removeAllValues, doc_QHttpHeader_removeAllValues);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_hasContentLength, "hasContentLength(self) -> bool");

extern "C" {static PyObject *meth_QHttpHeader_hasContentLength(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_hasContentLength(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->hasContentLength();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_hasContentLength, doc_QHttpHeader_hasContentLength);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_contentLength, "contentLength(self) -> int");

extern "C" {static PyObject *meth_QHttpHeader_contentLength(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_contentLength(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
             ::uint sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->contentLength();
            Py_END_ALLOW_THREADS

            return PyLong_FromUnsignedLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_contentLength, doc_QHttpHeader_contentLength);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_setContentLength, "setContentLength(self, int)");

extern "C" {static PyObject *meth_QHttpHeader_setContentLength(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_setContentLength(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bi", &sipSelf, sipType_QHttpHeader, &sipCpp, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setContentLength(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_setContentLength, doc_QHttpHeader_setContentLength);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_hasContentType, "hasContentType(self) -> bool");

extern "C" {static PyObject *meth_QHttpHeader_hasContentType(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_hasContentType(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->hasContentType();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_hasContentType, doc_QHttpHeader_hasContentType);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_contentType, "contentType(self) -> str");

extern "C" {static PyObject *meth_QHttpHeader_contentType(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_contentType(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
             ::QString*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QString(sipCpp->contentType());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_contentType, doc_QHttpHeader_contentType);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_setContentType, "setContentType(self, str)");

extern "C" {static PyObject *meth_QHttpHeader_setContentType(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_setContentType(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QString* a0;
        int a0State = 0;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setContentType(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_setContentType, doc_QHttpHeader_setContentType);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_toString, "toString(self) -> str");

extern "C" {static PyObject *meth_QHttpHeader_toString(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_toString(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
             ::QString*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new  ::QString((sipSelfWasArg ? sipCpp-> ::QHttpHeader::toString() : sipCpp->toString()));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_toString, doc_QHttpHeader_toString);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_isValid, "isValid(self) -> bool");

extern "C" {static PyObject *meth_QHttpHeader_isValid(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_isValid(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->isValid();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_isValid, doc_QHttpHeader_isValid);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_majorVersion, "majorVersion(self) -> int");

extern "C" {static PyObject *meth_QHttpHeader_majorVersion(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_majorVersion(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    PyObject *sipOrigSelf = sipSelf;

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
            int sipRes;

            if (!sipOrigSelf)
            {
                sipAbstractMethod(sipName_QHttpHeader, sipName_majorVersion);
                return NULL;
            }

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->majorVersion();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_majorVersion, doc_QHttpHeader_majorVersion);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_minorVersion, "minorVersion(self) -> int");

extern "C" {static PyObject *meth_QHttpHeader_minorVersion(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_minorVersion(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    PyObject *sipOrigSelf = sipSelf;

    {
        const  ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QHttpHeader, &sipCpp))
        {
            int sipRes;

            if (!sipOrigSelf)
            {
                sipAbstractMethod(sipName_QHttpHeader, sipName_minorVersion);
                return NULL;
            }

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->minorVersion();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_minorVersion, doc_QHttpHeader_minorVersion);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_parseLine, "parseLine(self, str, int) -> bool");

extern "C" {static PyObject *meth_QHttpHeader_parseLine(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_parseLine(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const  ::QString* a0;
        int a0State = 0;
        int a1;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "pJ1i", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State, &a1))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp-> ::QHttpHeader::parseLine(*a0,a1) : sipCpp->parseLine(*a0,a1));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_parseLine, doc_QHttpHeader_parseLine);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_parse, "parse(self, str) -> bool");

extern "C" {static PyObject *meth_QHttpHeader_parse(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_parse(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QString* a0;
        int a0State = 0;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "pJ1", &sipSelf, sipType_QHttpHeader, &sipCpp, sipType_QString,&a0, &a0State))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->parse(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_parse, doc_QHttpHeader_parse);

    return NULL;
}


PyDoc_STRVAR(doc_QHttpHeader_setValid, "setValid(self, bool)");

extern "C" {static PyObject *meth_QHttpHeader_setValid(PyObject *, PyObject *);}
static PyObject *meth_QHttpHeader_setValid(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        bool a0;
         ::QHttpHeader *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "pb", &sipSelf, sipType_QHttpHeader, &sipCpp, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setValid(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QHttpHeader, sipName_setValid, doc_QHttpHeader_setValid);

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QHttpHeader(void *, int);}
static void release_QHttpHeader(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipQHttpHeader *>(sipCppV);
    else
        delete reinterpret_cast< ::QHttpHeader *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QHttpHeader(sipSimpleWrapper *);}
static void dealloc_QHttpHeader(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipQHttpHeader *>(sipGetAddress(sipSelf))->sipPySelf = NULL;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_QHttpHeader(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_QHttpHeader(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QHttpHeader(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipQHttpHeader *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQHttpHeader();
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    {
        const  ::QHttpHeader* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J9", sipType_QHttpHeader, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQHttpHeader(*a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    {
        const  ::QString* a0;
        int a0State = 0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J1", sipType_QString,&a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQHttpHeader(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast< ::QString *>(a0),sipType_QString,a0State);

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return NULL;
}


static PyMethodDef methods_QHttpHeader[] = {
    {SIP_MLNAME_CAST(sipName_addValue), meth_QHttpHeader_addValue, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_addValue)},
    {SIP_MLNAME_CAST(sipName_allValues), meth_QHttpHeader_allValues, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_allValues)},
    {SIP_MLNAME_CAST(sipName_contentLength), meth_QHttpHeader_contentLength, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_contentLength)},
    {SIP_MLNAME_CAST(sipName_contentType), meth_QHttpHeader_contentType, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_contentType)},
    {SIP_MLNAME_CAST(sipName_hasContentLength), meth_QHttpHeader_hasContentLength, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_hasContentLength)},
    {SIP_MLNAME_CAST(sipName_hasContentType), meth_QHttpHeader_hasContentType, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_hasContentType)},
    {SIP_MLNAME_CAST(sipName_hasKey), meth_QHttpHeader_hasKey, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_hasKey)},
    {SIP_MLNAME_CAST(sipName_isValid), meth_QHttpHeader_isValid, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_isValid)},
    {SIP_MLNAME_CAST(sipName_keys), meth_QHttpHeader_keys, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_keys)},
    {SIP_MLNAME_CAST(sipName_majorVersion), meth_QHttpHeader_majorVersion, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_majorVersion)},
    {SIP_MLNAME_CAST(sipName_minorVersion), meth_QHttpHeader_minorVersion, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_minorVersion)},
    {SIP_MLNAME_CAST(sipName_parse), meth_QHttpHeader_parse, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_parse)},
    {SIP_MLNAME_CAST(sipName_parseLine), meth_QHttpHeader_parseLine, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_parseLine)},
    {SIP_MLNAME_CAST(sipName_removeAllValues), meth_QHttpHeader_removeAllValues, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_removeAllValues)},
    {SIP_MLNAME_CAST(sipName_removeValue), meth_QHttpHeader_removeValue, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_removeValue)},
    {SIP_MLNAME_CAST(sipName_setContentLength), meth_QHttpHeader_setContentLength, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_setContentLength)},
    {SIP_MLNAME_CAST(sipName_setContentType), meth_QHttpHeader_setContentType, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_setContentType)},
    {SIP_MLNAME_CAST(sipName_setValid), meth_QHttpHeader_setValid, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_setValid)},
    {SIP_MLNAME_CAST(sipName_setValue), meth_QHttpHeader_setValue, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_setValue)},
    {SIP_MLNAME_CAST(sipName_setValues), meth_QHttpHeader_setValues, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_setValues)},
    {SIP_MLNAME_CAST(sipName_toString), meth_QHttpHeader_toString, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_toString)},
    {SIP_MLNAME_CAST(sipName_value), meth_QHttpHeader_value, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_value)},
    {SIP_MLNAME_CAST(sipName_values), meth_QHttpHeader_values, METH_VARARGS, SIP_MLDOC_CAST(doc_QHttpHeader_values)}
};

PyDoc_STRVAR(doc_QHttpHeader, "\1QHttpHeader()\n"
    "QHttpHeader(QHttpHeader)\n"
    "QHttpHeader(str)");


static pyqt4ClassPluginDef plugin_QHttpHeader = {
    0,
    0,
    0
};


sipClassTypeDef sipTypeDef_QtNetwork_QHttpHeader = {
    {
        -1,
        0,
        0,
        SIP_TYPE_ABSTRACT|SIP_TYPE_CLASS,
        sipNameNr_QHttpHeader,
        {0},
        &plugin_QHttpHeader
    },
    {
        sipNameNr_QHttpHeader,
        {0, 0, 1},
        23, methods_QHttpHeader,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QHttpHeader,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
    0,
    init_type_QHttpHeader,
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
    dealloc_QHttpHeader,
    0,
    0,
    0,
    release_QHttpHeader,
    0,
    0,
    0,
    0,
    0,
    0,
    0
};
