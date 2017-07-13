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

#line 26 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qpaintdevice.sip"
#include <qpaintdevice.h>
#line 29 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQPaintDevice.cpp"

#line 52 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/sip/QtGui/qpaintengine.sip"
#include <qpaintengine.h>
#line 33 "/Users/max/dev/Copperfield_FX/tmp/PyQt4_gpl_mac-4.12.1/QtGui/sipQtGuiQPaintDevice.cpp"


class sipQPaintDevice : public  ::QPaintDevice
{
public:
    sipQPaintDevice();
    virtual ~sipQPaintDevice();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    int metric( ::QPaintDevice::PaintDeviceMetric) const;
     ::QPaintEngine* paintEngine() const;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipQPaintDevice(const sipQPaintDevice &);
    sipQPaintDevice &operator = (const sipQPaintDevice &);

    char sipPyMethods[2];
};

sipQPaintDevice::sipQPaintDevice():  ::QPaintDevice(), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQPaintDevice::~sipQPaintDevice()
{
    sipInstanceDestroyed(sipPySelf);
}

int sipQPaintDevice::metric( ::QPaintDevice::PaintDeviceMetric a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[0]),sipPySelf,NULL,sipName_metric);

    if (!sipMeth)
        return  ::QPaintDevice::metric(a0);

    extern int sipVH_QtGui_1(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *,  ::QPaintDevice::PaintDeviceMetric);

    return sipVH_QtGui_1(sipGILState, 0, sipPySelf, sipMeth, a0);
}

 ::QPaintEngine* sipQPaintDevice::paintEngine() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[1]),sipPySelf,sipName_QPaintDevice,sipName_paintEngine);

    if (!sipMeth)
        return 0;

    extern  ::QPaintEngine* sipVH_QtGui_0(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH_QtGui_0(sipGILState, 0, sipPySelf, sipMeth);
}


PyDoc_STRVAR(doc_QPaintDevice_paintEngine, "paintEngine(self) -> QPaintEngine");

extern "C" {static PyObject *meth_QPaintDevice_paintEngine(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_paintEngine(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    PyObject *sipOrigSelf = sipSelf;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
             ::QPaintEngine*sipRes;

            if (!sipOrigSelf)
            {
                sipAbstractMethod(sipName_QPaintDevice, sipName_paintEngine);
                return NULL;
            }

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->paintEngine();
            Py_END_ALLOW_THREADS

            return sipConvertFromType(sipRes,sipType_QPaintEngine,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_paintEngine, doc_QPaintDevice_paintEngine);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_width, "width(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_width(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_width(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->width();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_width, doc_QPaintDevice_width);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_height, "height(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_height(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_height(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->height();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_height, doc_QPaintDevice_height);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_widthMM, "widthMM(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_widthMM(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_widthMM(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->widthMM();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_widthMM, doc_QPaintDevice_widthMM);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_heightMM, "heightMM(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_heightMM(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_heightMM(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->heightMM();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_heightMM, doc_QPaintDevice_heightMM);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_logicalDpiX, "logicalDpiX(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_logicalDpiX(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_logicalDpiX(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->logicalDpiX();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_logicalDpiX, doc_QPaintDevice_logicalDpiX);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_logicalDpiY, "logicalDpiY(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_logicalDpiY(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_logicalDpiY(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->logicalDpiY();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_logicalDpiY, doc_QPaintDevice_logicalDpiY);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_physicalDpiX, "physicalDpiX(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_physicalDpiX(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_physicalDpiX(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->physicalDpiX();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_physicalDpiX, doc_QPaintDevice_physicalDpiX);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_physicalDpiY, "physicalDpiY(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_physicalDpiY(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_physicalDpiY(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->physicalDpiY();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_physicalDpiY, doc_QPaintDevice_physicalDpiY);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_numColors, "numColors(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_numColors(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_numColors(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->numColors();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_numColors, doc_QPaintDevice_numColors);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_depth, "depth(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_depth(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_depth(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->depth();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_depth, doc_QPaintDevice_depth);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_paintingActive, "paintingActive(self) -> bool");

extern "C" {static PyObject *meth_QPaintDevice_paintingActive(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_paintingActive(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->paintingActive();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_paintingActive, doc_QPaintDevice_paintingActive);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_colorCount, "colorCount(self) -> int");

extern "C" {static PyObject *meth_QPaintDevice_colorCount(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_colorCount(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QPaintDevice, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->colorCount();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_colorCount, doc_QPaintDevice_colorCount);

    return NULL;
}


PyDoc_STRVAR(doc_QPaintDevice_metric, "metric(self, QPaintDevice.PaintDeviceMetric) -> int");

extern "C" {static PyObject *meth_QPaintDevice_metric(PyObject *, PyObject *);}
static PyObject *meth_QPaintDevice_metric(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
         ::QPaintDevice::PaintDeviceMetric a0;
        const  ::QPaintDevice *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "pE", &sipSelf, sipType_QPaintDevice, &sipCpp, sipType_QPaintDevice_PaintDeviceMetric, &a0))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp-> ::QPaintDevice::metric(a0) : sipCpp->metric(a0));
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QPaintDevice, sipName_metric, doc_QPaintDevice_metric);

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QPaintDevice(void *, int);}
static void release_QPaintDevice(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipQPaintDevice *>(sipCppV);
    else
        delete reinterpret_cast< ::QPaintDevice *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QPaintDevice(sipSimpleWrapper *);}
static void dealloc_QPaintDevice(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipQPaintDevice *>(sipGetAddress(sipSelf))->sipPySelf = NULL;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_QPaintDevice(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_QPaintDevice(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QPaintDevice(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipQPaintDevice *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQPaintDevice();
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return NULL;
}


static PyMethodDef methods_QPaintDevice[] = {
    {SIP_MLNAME_CAST(sipName_colorCount), meth_QPaintDevice_colorCount, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_colorCount)},
    {SIP_MLNAME_CAST(sipName_depth), meth_QPaintDevice_depth, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_depth)},
    {SIP_MLNAME_CAST(sipName_height), meth_QPaintDevice_height, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_height)},
    {SIP_MLNAME_CAST(sipName_heightMM), meth_QPaintDevice_heightMM, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_heightMM)},
    {SIP_MLNAME_CAST(sipName_logicalDpiX), meth_QPaintDevice_logicalDpiX, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_logicalDpiX)},
    {SIP_MLNAME_CAST(sipName_logicalDpiY), meth_QPaintDevice_logicalDpiY, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_logicalDpiY)},
    {SIP_MLNAME_CAST(sipName_metric), meth_QPaintDevice_metric, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_metric)},
    {SIP_MLNAME_CAST(sipName_numColors), meth_QPaintDevice_numColors, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_numColors)},
    {SIP_MLNAME_CAST(sipName_paintEngine), meth_QPaintDevice_paintEngine, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_paintEngine)},
    {SIP_MLNAME_CAST(sipName_paintingActive), meth_QPaintDevice_paintingActive, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_paintingActive)},
    {SIP_MLNAME_CAST(sipName_physicalDpiX), meth_QPaintDevice_physicalDpiX, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_physicalDpiX)},
    {SIP_MLNAME_CAST(sipName_physicalDpiY), meth_QPaintDevice_physicalDpiY, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_physicalDpiY)},
    {SIP_MLNAME_CAST(sipName_width), meth_QPaintDevice_width, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_width)},
    {SIP_MLNAME_CAST(sipName_widthMM), meth_QPaintDevice_widthMM, METH_VARARGS, SIP_MLDOC_CAST(doc_QPaintDevice_widthMM)}
};

static sipEnumMemberDef enummembers_QPaintDevice[] = {
    {sipName_PdmDepth, static_cast<int>( ::QPaintDevice::PdmDepth), 366},
    {sipName_PdmDpiX, static_cast<int>( ::QPaintDevice::PdmDpiX), 366},
    {sipName_PdmDpiY, static_cast<int>( ::QPaintDevice::PdmDpiY), 366},
    {sipName_PdmHeight, static_cast<int>( ::QPaintDevice::PdmHeight), 366},
    {sipName_PdmHeightMM, static_cast<int>( ::QPaintDevice::PdmHeightMM), 366},
    {sipName_PdmNumColors, static_cast<int>( ::QPaintDevice::PdmNumColors), 366},
    {sipName_PdmPhysicalDpiX, static_cast<int>( ::QPaintDevice::PdmPhysicalDpiX), 366},
    {sipName_PdmPhysicalDpiY, static_cast<int>( ::QPaintDevice::PdmPhysicalDpiY), 366},
    {sipName_PdmWidth, static_cast<int>( ::QPaintDevice::PdmWidth), 366},
    {sipName_PdmWidthMM, static_cast<int>( ::QPaintDevice::PdmWidthMM), 366},
};

PyDoc_STRVAR(doc_QPaintDevice, "\1QPaintDevice()");


static pyqt4ClassPluginDef plugin_QPaintDevice = {
    0,
    0,
    0
};


sipClassTypeDef sipTypeDef_QtGui_QPaintDevice = {
    {
        -1,
        0,
        0,
        SIP_TYPE_ABSTRACT|SIP_TYPE_CLASS,
        sipNameNr_QPaintDevice,
        {0},
        &plugin_QPaintDevice
    },
    {
        sipNameNr_QPaintDevice,
        {0, 0, 1},
        14, methods_QPaintDevice,
        10, enummembers_QPaintDevice,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QPaintDevice,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
    0,
    init_type_QPaintDevice,
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
    dealloc_QPaintDevice,
    0,
    0,
    0,
    release_QPaintDevice,
    0,
    0,
    0,
    0,
    0,
    0,
    0
};
