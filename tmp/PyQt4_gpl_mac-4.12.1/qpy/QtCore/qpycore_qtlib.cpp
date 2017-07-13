// This implements the support for old-style signals and slots.
//
// @BS_LICENCE@


#include <Python.h>

#include <QObject>

#include "qpycore_pyqtproxy.h"
#include "qpycore_qtlib.h"
#include "qpycore_sip.h"
#include "qpycore_sip_helpers.h"


/* This is how Qt "types" signals and slots. */
#define isQtSlot(s)     (*(s) == '1')
#define isQtSignal(s)   (*(s) == '2')


static sipErrorState QObjectFromPy(PyObject *obj, QObject **qobjp);
static QObject *resolveSignal(QObject *qtx, const char **sig);
static PyObject *getWeakRef(PyObject *obj);
static char *sipStrdup(const char *);
static void saveMethod(sipPyMethod *pm, PyObject *meth);


// Invoke a single slot (Qt or Python) and return the result.  Optionally check
// that any receiver C++ object still exist.
PyObject *qtlib_invoke_slot(const sipSlot *slot, PyObject *sigargs,
        int no_receiver_check)
{
    PyObject *sfunc, *sref;

    // Get the object to call, resolving any weak references.
    if (slot->weakSlot == Py_True)
    {
         // The slot is guaranteed to be Ok because it has an extra reference
         // or is None.
        sref = slot->pyobj;
    }
    else if (!slot->weakSlot)
    {
        sref = 0;
    }
    else
    {
        sref = PyWeakref_GetObject(slot->weakSlot);

        if (!sref)
            return 0;
    }

    if (sref == Py_None)
    {
        // If the real object has gone then we pretend everything is Ok.  This
        // mimics the Qt behaviour of not caring if a receiving object has been
        // deleted.
        Py_INCREF(Py_None);
        return Py_None;
    }

    Py_XINCREF(sref);

    if (!slot->pyobj)
    {
        PyObject *self = (sref ? sref : slot->meth.mself);

        // If the receiver wraps a C++ object then ignore the call if it no
        // longer exists.
        if (!no_receiver_check &&
            PyObject_TypeCheck(self, sipSimpleWrapper_Type) &&
            !sipGetAddress((sipSimpleWrapper *)self))
        {
            Py_XDECREF(sref);

            Py_INCREF(Py_None);
            return Py_None;
        }

#if PY_MAJOR_VERSION >= 3
        sfunc = PyMethod_New(slot->meth.mfunc, self);
#else
        sfunc = PyMethod_New(slot->meth.mfunc, self, slot->meth.mclass);
#endif

        if (!sfunc)
        {
            Py_XDECREF(sref);
            return 0;
        }
    }
    else if (slot->name)
    {
        char *mname = slot->name + 1;
        PyObject *self = (sref ? sref : slot->pyobj);

        sfunc = PyObject_GetAttrString(self, mname);

        if (!sfunc || !PyCFunction_Check(sfunc))
        {
            // Note that in earlier versions of SIP this error would be
            // detected when the slot was connected.
            PyErr_Format(PyExc_NameError, "Invalid slot %s", mname);

            Py_XDECREF(sfunc);
            Py_XDECREF(sref);
            return 0;
        }
    }
    else
    {
        sfunc = slot->pyobj;
        Py_INCREF(sfunc);
    }

    // We make repeated attempts to call a slot.  If we work out that it failed
    // because of an immediate type error we try again with one less argument.
    // We keep going until we run out of arguments to drop.  This emulates the
    // Qt ability of the slot to accept fewer arguments than a signal provides.
    PyObject *sa = sigargs;
    Py_INCREF(sa);

    PyObject *oxtype, *oxvalue, *oxtb;

    oxtype = oxvalue = oxtb = 0;

    for (;;)
    {
        PyObject *resobj = PyEval_CallObject(sfunc, sa);

        if (resobj)
        {
            Py_DECREF(sfunc);
            Py_XDECREF(sref);

            // Remove any previous exception.
            if (sa != sigargs)
            {
                Py_XDECREF(oxtype);
                Py_XDECREF(oxvalue);
                Py_XDECREF(oxtb);
                PyErr_Clear();
            }

            Py_DECREF(sa);

            return resobj;
        }

        // Get the exception.
        PyObject *xtype, *xvalue, *xtb;

        PyErr_Fetch(&xtype, &xvalue, &xtb);

        // See if it is unacceptable.  An acceptable failure is a type error
        // with no traceback - so long as we can still reduce the number of
        // arguments and try again.
        if (!PyErr_GivenExceptionMatches(xtype, PyExc_TypeError) || xtb ||
            PyTuple_GET_SIZE(sa) == 0)
        {
            // If there is a traceback then we must have called the slot and
            // the exception was later on - so report the exception as is.
            if (xtb)
            {
                if (sa != sigargs)
                {
                    Py_XDECREF(oxtype);
                    Py_XDECREF(oxvalue);
                    Py_XDECREF(oxtb);
                }

                PyErr_Restore(xtype, xvalue, xtb);
            }
            else if (sa == sigargs)
            {
                PyErr_Restore(xtype, xvalue, xtb);
            }
            else
            {
                // Discard the latest exception and restore the original one.
                Py_XDECREF(xtype);
                Py_XDECREF(xvalue);
                Py_XDECREF(xtb);

                PyErr_Restore(oxtype, oxvalue, oxtb);
            }

            break;
        }

        // If this is the first attempt, save the exception.
        if (sa == sigargs)
        {
            oxtype = xtype;
            oxvalue = xvalue;
            oxtb = xtb;
        }
        else
        {
            Py_XDECREF(xtype);
            Py_XDECREF(xvalue);
            Py_XDECREF(xtb);
        }

        // Create the new argument tuple.
        PyObject *nsa = PyTuple_GetSlice(sa, 0, PyTuple_GET_SIZE(sa) - 1);

        if (!nsa)
        {
            // Tidy up.
            Py_XDECREF(oxtype);
            Py_XDECREF(oxvalue);
            Py_XDECREF(oxtb);

            break;
        }

        Py_DECREF(sa);
        sa = nsa;
    }

    Py_DECREF(sfunc);
    Py_XDECREF(sref);

    Py_DECREF(sa);

    return 0;
}


// Compare two slots to see if they are the same.
bool qtlib_same_slot(const sipSlot *sp, PyObject *rxObj, const char *slot)
{
    // See if they are signals or Qt slots, ie. they have a name.
    if (slot)
    {
        if (!sp->name || sp->name[0] == '\0')
            return false;

        return (qstrcmp(sp->name, slot) == 0 && sp->pyobj == rxObj);
    }

    // See if they are pure Python methods.
    if (PyMethod_Check(rxObj))
    {
        if (sp->pyobj)
            return false;

        return (sp->meth.mfunc == PyMethod_GET_FUNCTION(rxObj)
                && sp->meth.mself == PyMethod_GET_SELF(rxObj)
#if PY_MAJOR_VERSION < 3
                && sp->meth.mclass == PyMethod_GET_CLASS(rxObj)
#endif
                );
    }

    // See if they are wrapped C++ methods.
    if (PyCFunction_Check(rxObj))
    {
        if (!sp->name || sp->name[0] != '\0')
            return false;

        return (sp->pyobj == PyCFunction_GET_SELF(rxObj) &&
                qstrcmp(&sp->name[1], ((PyCFunctionObject *)rxObj)->m_ml->ml_name) == 0);
    }

    // The objects must be the same.
    return (sp->pyobj == rxObj);
}


// Implement QObject.connect().
PyObject *qpycore_qobject_connect(sipErrorState *estate, QObject *qtx,
        PyObject *txObj, PyObject *sigObj, PyObject *rxObj, PyObject *slotObj,
        int type)
{
    bool res;

    const char *sig = pyqt4_get_signal(sigObj);
    if (!sig)
    {
        *estate = sipBadCallableArg(1, sigObj);
        return 0;
    }

    const char *slot;
    QObject *qrx;

    if (slotObj)
    {
        slot = pyqt4_get_slot(slotObj);
        if (!slot)
        {
            *estate = sipBadCallableArg(3, slotObj);
            return 0;
        }

        if ((*estate = QObjectFromPy(rxObj, &qrx)) != sipErrorNone)
        {
            if (*estate == sipErrorContinue)
                *estate = sipBadCallableArg(2, rxObj);

            return 0;
        }

        if (isQtSignal(slot))
            qrx = resolveSignal(qrx, &slot);
    }
    else
    {
        qrx = qpycore_create_universal_slot((sipWrapper *)txObj, sig, rxObj, 0,
                &slot, 0);

        if (!qrx)
        {
            *estate = sipErrorFail;
            return 0;
        }

#if SIP_VERSION < 0x050000
        sipSetPossibleProxy((sipSimpleWrapper *)txObj);
#endif
    }

    qtx = resolveSignal(qtx, &sig);

    Py_BEGIN_ALLOW_THREADS
    res = QObject::connect(qtx, sig, qrx, slot, (Qt::ConnectionType)type);
    Py_END_ALLOW_THREADS

    return PyBool_FromLong(res);
}


// Implement QObject.disconnect().
PyObject *qpycore_qobject_disconnect(sipErrorState *estate, QObject *qtx,
        PyObject *sigObj, PyObject *rxObj, PyObject *slotObj)
{
    bool res;

    const char *sig = pyqt4_get_signal(sigObj);
    if (!sig)
    {
        *estate = sipBadCallableArg(1, sigObj);
        return 0;
    }

    const char *slot;
    QObject *qrx;

    if (slotObj)
    {
        slot = pyqt4_get_slot(slotObj);
        if (!slot)
        {
            *estate = sipBadCallableArg(3, slotObj);
            return 0;
        }

        if ((*estate = QObjectFromPy(rxObj, &qrx)) != sipErrorNone)
        {
            if (*estate == sipErrorContinue)
                *estate = sipBadCallableArg(2, rxObj);

            return 0;
        }

        if (isQtSignal(slot))
            qrx = qpycore_find_signal(qrx, &slot);
    }
    else
    {
        qrx = PyQtProxy::findSlotProxy(qtx, sig, rxObj, 0, &slot);
    }

    qtx = qpycore_find_signal(qtx, &sig);

    Py_BEGIN_ALLOW_THREADS

    res = QObject::disconnect(qtx, sig, qrx, slot);

    // Delete it if it is a universal slot as this will be it's only
    // connection.  If the slot is actually a universal signal then it should
    // leave it in place.
    PyQtProxy::mutex->lock();

    PyQtProxy::ProxyHash::const_iterator it(PyQtProxy::proxy_slots.begin());

    while (it != PyQtProxy::proxy_slots.end())
    {
        PyQtProxy *up = it.value();

        if (up == qrx)
        {
            // If we are disconnecting within the slot that is connected then
            // disable() will make sure the proxy isn't deleted until the slot
            // returns.
            up->disable();
            break;
        }

        ++it;
    }

    PyQtProxy::mutex->unlock();

    Py_END_ALLOW_THREADS

    return PyBool_FromLong(res);
}


// Free the resources of a slot.
void qtlib_free_slot(sipSlot *slot)
{
    if (slot->name)
    {
        sipFree(slot->name);
    }
    else if (slot->weakSlot == Py_True)
    {
        Py_DECREF(slot->pyobj);
    }

    // Remove any weak reference.
    Py_XDECREF(slot->weakSlot);
}


// Initialise a slot, returning 0 if there was no error.  If the signal was a
// Qt signal, then the slot may be a Python signal or a Python slot.  If the
// signal was a Python signal, then the slot may be anything.
int qtlib_save_slot(sipSlot *sp, PyObject *rxObj, const char *slot)
{
    sp->weakSlot = 0;

    if (!slot)
    {
        sp->name = 0;

        if (PyMethod_Check(rxObj))
        {
            // Python creates methods on the fly.  We could increment the
            // reference count to keep it alive, but that would keep "self"
            // alive as well and would probably be a circular reference.
            // Instead we remember the component parts and hope they are still
            // valid when we re-create the method when we need it.
            saveMethod(&sp->meth, rxObj);

            // Notice if the class instance disappears.
            sp->weakSlot = getWeakRef(sp->meth.mself);

            // This acts a flag to say that the slot is a method.
            sp->pyobj = 0;
        }
        else
        {
            PyObject *self;

            // We know that it is another type of callable, ie. a
            // function/builtin.

            if (PyCFunction_Check(rxObj) &&
                (self = PyCFunction_GET_SELF(rxObj)) != NULL &&
                PyObject_TypeCheck(self, sipSimpleWrapper_Type))
            {
                // It is a wrapped C++ class method.  We can't keep a copy
                // because they are generated on the fly and we can't take a
                // reference as that may keep the instance (ie. self) alive.
                // We therefore treat it as if the user had specified the slot
                // at "obj, SLOT('meth()')" rather than "obj.meth" (see below).

                const char *meth;

                // Get the method name.
                meth = ((PyCFunctionObject *)rxObj)->m_ml->ml_name;

                if ((sp->name = (char *)sipMalloc(strlen(meth) + 2)) == NULL)
                    return -1;

                // Copy the name and set the marker that it needs converting to
                // a built-in method.
                sp->name[0] = '\0';
                strcpy(&sp->name[1], meth);

                sp->pyobj = self;
                sp->weakSlot = getWeakRef(self);
            }
            else
            {
                // Give the slot an extra reference to keep it alive and
                // remember we have done so by treating weakSlot specially.
                Py_INCREF(rxObj);
                sp->pyobj = rxObj;

                Py_INCREF(Py_True);
                sp->weakSlot = Py_True;
            }
        }
    }
    else if ((sp->name = sipStrdup(slot)) == NULL)
    {
        return -1;
    }
    else if (isQtSlot(slot))
    {
        // The user has decided to connect a Python signal to a Qt slot and
        // specified the slot as "obj, SLOT('meth()')" rather than "obj.meth".

        char *tail;

        // Remove any arguments.
        if ((tail = strchr(sp->name,'(')) != NULL)
            *tail = '\0';

        // A bit of a hack to indicate that this needs converting to a built-in
        // method.
        sp->name[0] = '\0';

        // Notice if the class instance disappears.
        sp->weakSlot = getWeakRef(rxObj);

        sp->pyobj = rxObj;
    }
    else
        // It's a Qt signal.
        sp->pyobj = rxObj;

    return 0;
}


// Check that a Python object was returned by SIGNAL(), or is a signal object,
// and return the string.
const char *pyqt4_get_signal(PyObject *sig_obj)
{
    const char *sig = pyqt4_get_pyqtsignal_parts(sig_obj, 0);

    if (!sig && SIPBytes_Check(sig_obj))
    {
        sig = SIPBytes_AS_STRING(sig_obj);

        if (!isQtSignal(sig))
            sig = 0;
    }

    return sig;
}


// Check that a Python object was returned by SLOT() or SIGNAL() and return the
// string.
const char *pyqt4_get_slot(PyObject *slot_obj)
{
    if (SIPBytes_Check(slot_obj))
    {
        const char *slot = SIPBytes_AS_STRING(slot_obj);

        if (isQtSlot(slot) || isQtSignal(slot))
            return slot;
    }

    return 0;
}


// Check that a Python object wraps a QObject and return it.
static sipErrorState QObjectFromPy(PyObject *obj, QObject **qobjp)
{
    // We check the type first to allow type errors to continue to the next
    // overload.
    if (!PyObject_TypeCheck(obj, sipTypeAsPyTypeObject(sipType_QObject)))
        return sipErrorContinue;

    void *cpp = sipGetCppPtr((sipSimpleWrapper *)obj, sipType_QObject);

    if (!cpp)
        return sipErrorFail;

    *qobjp = reinterpret_cast<QObject *>(cpp);

    return sipErrorNone;
}


// Return a usable signal, creating a new universal signal if needed.
static QObject *resolveSignal(QObject *qtx, const char **sig)
{
    QObject *new_qtx = qpycore_find_signal(qtx, sig);

    if (!new_qtx)
        new_qtx = qpycore_create_universal_signal(qtx, sig);

    return new_qtx;
}


// Return a weak reference to the given object.
static PyObject *getWeakRef(PyObject *obj)
{
    PyObject *wr = PyWeakref_NewRef(obj, NULL);

    if (!wr)
        PyErr_Clear();

    return wr;
}


// Implement strdup() using sipMalloc().
static char *sipStrdup(const char *s)
{
    char *d;

    if ((d = (char *)sipMalloc(strlen(s) + 1)) != NULL)
        strcpy(d,s);

    return d;
}


// Save the components of a Python method.
static void saveMethod(sipPyMethod *pm, PyObject *meth)
{
    pm->mfunc = PyMethod_GET_FUNCTION(meth);
    pm->mself = PyMethod_GET_SELF(meth);
#if PY_MAJOR_VERSION < 3
    pm->mclass = PyMethod_GET_CLASS(meth);
#endif
}
