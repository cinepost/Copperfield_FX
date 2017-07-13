// This contains the implementation of the PyQtProxy class.
//
// Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt4.
// 
// This file may be used under the terms of the GNU General Public License
// version 3.0 as published by the Free Software Foundation and appearing in
// the file LICENSE included in the packaging of this file.  Please review the
// following information to ensure the GNU General Public License version 3.0
// requirements will be met: http://www.gnu.org/copyleft/gpl.html.
// 
// If you do not wish to use this file under the terms of the GPL version 3.0
// then you may purchase a commercial license.  For more information contact
// info@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


#include <Python.h>

#include <QByteArray>
#include <QMetaObject>
#include <QMutex>
#include <QObject>

#include "qpycore_chimera.h"
#include "qpycore_qmetaobjectbuilder.h"
#include "qpycore_qtlib.h"
#include "qpycore_pyqtproxy.h"
#include "qpycore_pyqtpyobject.h"
#include "qpycore_sip.h"


// Proxy flags.  Note that SIP_SINGLE_SHOT is part of the same flag-space.
#define PROXY_OWNS_SLOT_SIG 0x10    // The proxy owns the slot signature.
#define PROXY_SLOT_INVOKED  0x20    // The proxied slot is executing.
#define PROXY_SLOT_DISABLED 0x40    // The proxy deleteLater() has been called
                                    // or should be called after the slot has
                                    // finished executing.
#define PROXY_NO_RCVR_CHECK 0x80    // The existence of the receiver C++ object
                                    // should not be checked.


// The last QObject sender.
QObject *PyQtProxy::last_sender = 0;


#if QT_VERSION < 0x050000

static const uint slot_meta_data[] = {
    // content:
    1,       // revision
    0,       // classname
    0,    0, // classinfo
    2,   10, // methods (number, offset in this array of first one)
    0,    0, // properties
    0,    0, // enums/sets

    // slots: signature, parameters, type, tag, flags
    21,   10,   10,   10, 0x0a,
    11,   10,   10,   10, 0x0a,

    0        // eod
};


static const char slot_meta_stringdata[] = {
    "PyQtProxy\0\0disable()\0unislot()\0"
};


const QMetaObject PyQtProxy::staticMetaObject = {
    {
        &QObject::staticMetaObject,
        slot_meta_stringdata,
        slot_meta_data,
        0
    }
};

#endif


// Create a universal proxy used as a signal.
PyQtProxy::PyQtProxy(QObject *qtx, const char *sig)
    : QObject(), type(PyQtProxy::ProxySignal), proxy_flags(0),
            signature(QMetaObject::normalizedSignature(sig)), meta_object(0)
{
    init(qtx, &proxy_signals, qtx);
}


// Create a universal proxy used as a slot.  Note that this will leak if there
// is no signal transmitter (ie. no parent) and not marked as single shot.
// There will be no meta-object if there was a problem creating the proxy.
PyQtProxy::PyQtProxy(sipWrapper *txObj, const char *sig, PyObject *rxObj,
        const char *slot, const char **member, int flags)
    : QObject(), type(PyQtProxy::ProxySlot),
            proxy_flags(PROXY_OWNS_SLOT_SIG | flags),
            signature(QMetaObject::normalizedSignature(sig)), meta_object(0)
{
    void *tx = 0;
    QObject *qtx = 0;

    // Parse the signature.
    SIP_BLOCK_THREADS

    real_slot.signature = Chimera::parse(signature, "a slot argument");

    if (real_slot.signature)
    {
        // Save the slot.
        if (qtlib_save_slot(&real_slot.sip_slot, rxObj, slot) < 0)
        {
            delete real_slot.signature;
            real_slot.signature = 0;
        }
        else
        {
            // See if there is a transmitter and that it is a QObject.
            if (txObj)
            {
                tx = sipGetCppPtr((sipSimpleWrapper *)txObj, 0);

                if (tx && PyObject_TypeCheck((PyObject *)txObj, sipTypeAsPyTypeObject(sipType_QObject)))
                    qtx = reinterpret_cast<QObject *>(tx);
            }
        }
    }

    SIP_UNBLOCK_THREADS

    if (real_slot.signature)
    {
        // Return the slot to connect to.
        *member = SLOT(unislot());

        init(qtx, &proxy_slots, tx);
    }
}


// Create a universal proxy used as a slot being connected to a bound signal.
// There will be no meta-object if there was a problem creating the proxy.
PyQtProxy::PyQtProxy(QObject *qtx, const Chimera::Signature *signal_signature,
        PyObject *rxObj, const char **member, int flags)
    : QObject(), type(PyQtProxy::ProxySlot), proxy_flags(flags),
        signature(signal_signature->signature)
{
    SIP_BLOCK_THREADS

    real_slot.signature = signal_signature;

    // Save the slot.
    if (qtlib_save_slot(&real_slot.sip_slot, rxObj, 0) < 0)
        real_slot.signature = 0;

    SIP_UNBLOCK_THREADS

    if (real_slot.signature)
    {
        // Return the slot to connect to.
        *member = SLOT(unislot());

        init(qtx, &proxy_slots, qtx);
    }
}


// Initialisation common to all ctors.
void PyQtProxy::init(QObject *qtx, PyQtProxy::ProxyHash *hash, void *key)
{
    // Create a new meta-object on the heap so that it looks like it has a
    // signal of the right name and signature.
#if QT_VERSION >= 0x050000
    QMetaObjectBuilder builder;

    builder.setClassName("PyQtProxy");
    builder.setSuperClass(&QObject::staticMetaObject);

    // Note that signals must be added before slots.
    if (type == ProxySignal)
        builder.addSignal(signature);
    else
        builder.addSlot("unislot()");

    builder.addSlot("disable()");

    meta_object = builder.toMetaObject();
#else
    if (type == ProxySignal)
    {
        QMetaObject *mo = new QMetaObject;
        mo->d.superdata = &QObject::staticMetaObject;
        mo->d.extradata = 0;

        // Calculate the size of the string meta-data as follows:
        // - "PyQtProxy" and its terminating '\0' (ie. 9 + 1 bytes),
        // - a '\0' used for any empty string,
        // - "disable()" and its terminating '\0' (ie. 9 + 1 bytes),
        // - the (non-existent) argument names (ie. use the empty string if
        //   there is less that two arguments, otherwise a comma between each
        //   argument and the terminating '\0'),
        // - the name and full signature, less the initial type character, plus
        //   the terminating '\0'.

        const size_t fixed_len = 9 + 1 + 1 + 9 + 1;
        const size_t empty_str = 9 + 1;

        int nr_commas = signature.count(',');

        size_t len = fixed_len
                    + (nr_commas >= 0 ? nr_commas + 1 : 0)
                    + signature.size() + 1;

        char *smd = new char[len];

        memcpy(smd, slot_meta_stringdata, fixed_len);

        uint i = fixed_len, args_pos;

        if (nr_commas > 0)
        {
            args_pos = i;

            for (int c = 0; c < nr_commas; ++c)
                smd[i++] = ',';

            smd[i++] = '\0';
        }
        else
        {
            args_pos = empty_str;
        }

        uint sig_pos = i;
        qstrcpy(&smd[i], signature.constData());

        mo->d.stringdata = smd;

        // Add the non-string data.
        uint *data = new uint[21];

        memcpy(data, slot_meta_data, 21 * sizeof (uint));

        // Replace the first method (ie. unislot()) with the new signal.
        data[10] = sig_pos;
        data[11] = args_pos;
        data[14] = 0x05;

        mo->d.data = data;

        meta_object = mo;
    }
    else
    {
        meta_object = &staticMetaObject;
    }
#endif

    hashed = true;
    saved_key = key;
    transmitter = qtx;

    // Add this one to the global hashes.
    mutex->lock();
    hash->insert(key, this);
    mutex->unlock();

    // Detect when the transmitter is destroyed.  (Note that we used to do this
    // by making the proxy a child of the transmitter.  This doesn't work as
    // expected because QWidget destroys its children before emitting the
    // destroyed signal.)  We use a queued connection in case the proxy is also
    // connected to the same signal and we want to make sure it has a chance
    // to invoke the slot before being destroyed.
    if (qtx)
        connect(qtx, SIGNAL(destroyed(QObject *)), SLOT(disable()),
                Qt::QueuedConnection);
}


// Destroy a universal proxy.
PyQtProxy::~PyQtProxy()
{
    Q_ASSERT((proxy_flags & PROXY_SLOT_INVOKED) == 0);

    if (hashed)
    {
        mutex->lock();

        switch (type)
        {
        case ProxySlot:
            {
                ProxyHash::iterator it(proxy_slots.find(saved_key));
                ProxyHash::iterator end(proxy_slots.end());

                while (it != end && it.key() == saved_key)
                {
                    if (it.value() == this)
                        it = proxy_slots.erase(it);
                    else
                        ++it;
                }

                break;
            }

        case ProxySignal:
            {
                ProxyHash::iterator it(proxy_signals.find(saved_key));
                ProxyHash::iterator end(proxy_signals.end());

                while (it != end && it.key() == saved_key)
                {
                    if (it.value() == this)
                        it = proxy_signals.erase(it);
                    else
                        ++it;
                }

                break;
            }
        }

        mutex->unlock();
    }

    if (type == ProxySlot && real_slot.signature)
    {
        // Qt can still be tidying up after Python has gone so make sure that
        // it hasn't.
        if (Py_IsInitialized())
        {
            SIP_BLOCK_THREADS
            qtlib_free_slot(&real_slot.sip_slot);
            SIP_UNBLOCK_THREADS
        }

        if (proxy_flags & PROXY_OWNS_SLOT_SIG)
            delete real_slot.signature;

        real_slot.signature = 0;
    }

    if (meta_object)
    {
#if QT_VERSION >= 0x050000
        free(const_cast<QMetaObject *>(meta_object));
#else
        if (meta_object != &staticMetaObject)
        {
            // The casts are needed for MSVC 6.
            delete[] const_cast<char *>(meta_object->d.stringdata);
            delete[] const_cast<uint *>(meta_object->d.data);
            delete meta_object;
        }
#endif
    }
}


// The static members of PyQtProxy.
QMutex *PyQtProxy::mutex;
PyQtProxy::ProxyHash PyQtProxy::proxy_slots;
PyQtProxy::ProxyHash PyQtProxy::proxy_signals;


const QMetaObject *PyQtProxy::metaObject() const
{
    return meta_object;
}


void *PyQtProxy::qt_metacast(const char *_clname)
{
    if (!_clname)
        return 0;

    if (qstrcmp(_clname, "PyQtProxy") == 0)
        return static_cast<void *>(const_cast<PyQtProxy *>(this));

    return QObject::qt_metacast(_clname);
}


int PyQtProxy::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);

    if (_id < 0)
        return _id;

    if (_c == QMetaObject::InvokeMetaMethod)
    {
        switch (_id)
        {
        case 0:
            if (type == ProxySignal)
                QMetaObject::activate(this, meta_object, _id, _a);
            else
                unislot(_a);
            break;

        case 1:
            disable();
            break;
        }

        _id -= 2;
    }

    return _id;
}


// This is the universal slot itself that dispatches to the real slot.
void PyQtProxy::unislot(void **qargs)
{
    // If we are marked as disabled (possible if a queued signal has been
    // disconnected but there is still a signal in the event queue) then just
    // ignore the call.
    if (proxy_flags & PROXY_SLOT_DISABLED)
        return;

    // sender() must be called without the GIL to avoid possible deadlocks
    // between the GIL and Qt's internal thread data mutex.
    QObject *new_last_sender = sender();

    SIP_BLOCK_THREADS

    QObject *saved_last_sender = last_sender;
    last_sender = new_last_sender;

    int no_receiver_check = (proxy_flags & PROXY_NO_RCVR_CHECK);
    PyObject *res;

    // See if the sender was a short-circuit signal. */
    if (last_sender && PyQtShortcircuitSignalProxy::shortcircuitSignal(last_sender))
    {
        // The Python arguments will be the only argument.
        PyObject *pyargs = reinterpret_cast<PyQt_PyObject *>(qargs[1])->pyobject;

        res = qtlib_invoke_slot(&real_slot.sip_slot, pyargs,
                no_receiver_check);
    }
    else
    {
        proxy_flags |= PROXY_SLOT_INVOKED;
        res = invokeSlot(real_slot, qargs, no_receiver_check);
        proxy_flags &= ~PROXY_SLOT_INVOKED;

        // Self destruct if we are a single shot or disabled.
        if (proxy_flags & (SIP_SINGLE_SHOT|PROXY_SLOT_DISABLED))
        {
            // See the comment in disable() for why we deleteLater().
            deleteLater();
        }
    }

    if (res)
        Py_DECREF(res);
    else
        PyErr_Print();

    last_sender = saved_last_sender;

    SIP_UNBLOCK_THREADS
}


// Disable the slot by destroying it if possible, or delaying its destruction
// until the proxied slot returns.
void PyQtProxy::disable()
{
    proxy_flags |= PROXY_SLOT_DISABLED;

    // Delete it if the slot isn't currently executing, otherwise it will be
    // done after the slot returns.  Note that we don't rely on deleteLater()
    // providing the necessary delay because the slot could process the event
    // loop and the proxy would be deleted too soon.
    if ((proxy_flags & PROXY_SLOT_INVOKED) == 0)
    {
        // Despite what the Qt documentation suggests, if there are outstanding
        // queued signals then we may crash so we always delete later when the
        // event queue will have been flushed.
        deleteLater();
    }
}


// Invoke a slot on behalf of C++.
PyObject *PyQtProxy::invokeSlot(const qpycore_slot &slot, void **qargs,
        int no_receiver_check)
{
    const QList<const Chimera *> &args = slot.signature->parsed_arguments;

    PyObject *argtup = PyTuple_New(args.size());

    if (!argtup)
        return 0;

    QList<const Chimera *>::const_iterator it = args.constBegin();

    for (int a = 0; it != args.constEnd(); ++a)
    {
        PyObject *arg = (*it)->toPyObject(*++qargs);

        if (!arg)
        {
            Py_DECREF(argtup);
            return 0;
        }

        PyTuple_SET_ITEM(argtup, a, arg);

        ++it;
    }

    // Dispatch to the real slot.
    PyObject *res = qtlib_invoke_slot(&slot.sip_slot, argtup,
            no_receiver_check);

    Py_DECREF(argtup);

    return res;
}


// Disable the check that the receiver C++ object exists before invoking a
// slot.
void PyQtProxy::disableReceiverCheck()
{
    proxy_flags |= PROXY_NO_RCVR_CHECK;
}


// Find a slot proxy connected to a transmitter.
PyQtProxy *PyQtProxy::findSlotProxy(void *tx, const char *sig, PyObject *rxObj,
        const char *slot, const char **member)
{
    PyQtProxy *proxy = 0;

    mutex->lock();

    ProxyHash::const_iterator it(proxy_slots.find(tx));
    ProxyHash::const_iterator end(proxy_slots.end());

    while (it != end && it.key() == tx)
    {
        PyQtProxy *up = it.value();

        if (up->signature == sig && qtlib_same_slot(&up->real_slot.sip_slot, rxObj, slot))
        {
            *member = SLOT(unislot());
            proxy = up;
            break;
        }

        ++it;
    }

    mutex->unlock();

    return proxy;
}


// Delete any slot proxies for a particular signal.
void PyQtProxy::deleteSlotProxies(void *tx, const char *sig)
{
    mutex->lock();

    ProxyHash::iterator it(proxy_slots.find(tx));
    ProxyHash::iterator end(proxy_slots.end());

    while (it != end && it.key() == tx)
    {
        PyQtProxy *up = it.value();

        if (up->signature == sig)
        {
            up->hashed = false;
            it = proxy_slots.erase(it);

            up->disable();
        }
        else
            ++it;
    }

    mutex->unlock();
}


#if SIP_VERSION >= 0x050000
// Clear the extra references of any slots connected to a transmitter.  This is
// called with the GIL.
int PyQtProxy::clearSlotProxies(const QObject *transmitter)
{
    ProxyHash::iterator it(
            proxy_slots.find(const_cast<QObject *>(transmitter)));
    ProxyHash::iterator end(proxy_slots.end());

    while (it != end && it.key() == transmitter)
    {
        sipSlot *slot = &it.value()->real_slot.sip_slot;

        if (slot->weakSlot == Py_True)
        {
            PyObject *xref = slot->pyobj;

            // Replace the slot with None.  We don't use NULL as this has
            // another meaning.
            Py_INCREF(Py_None);
            slot->pyobj = Py_None;

            Py_DECREF(xref);
        }

        ++it;
    }

    return 0;
}
#endif


// A thing wrapper available to the generated code.
int qpycore_clearSlotProxies(const QObject *transmitter)
{
#if SIP_VERSION >= 0x050000
    return PyQtProxy::clearSlotProxies(transmitter);
#else
    Q_UNUSED(transmitter);

    return 0;
#endif
}


#if SIP_VERSION >= 0x050000
// Visit the extra references of any slots connected to a transmitter.  This is
// called with the GIL.
int PyQtProxy::visitSlotProxies(const QObject *transmitter,
        visitproc visit, void *arg)
{
    int vret = 0;

    ProxyHash::iterator it(
            proxy_slots.find(const_cast<QObject *>(transmitter)));
    ProxyHash::iterator end(proxy_slots.end());

    while (it != end && it.key() == transmitter)
    {
        sipSlot *slot = &it.value()->real_slot.sip_slot;

        // See if the slot has an extra reference.
        if (slot->weakSlot == Py_True && slot->pyobj != Py_None)
        {
            if ((vret = visit(slot->pyobj, arg)) != 0)
                break;
        }

        ++it;
    }

    return vret;
}
#endif


// A thing wrapper available to the generated code.
int qpycore_visitSlotProxies(const QObject *transmitter, visitproc visit,
        void *arg)
{
#if SIP_VERSION >= 0x050000
    return PyQtProxy::visitSlotProxies(transmitter, visit, arg);
#else
    Q_UNUSED(transmitter);
    Q_UNUSED(visit);
    Q_UNUSED(arg);

    return 0;
#endif
}


// This is set if a PyQtShortcircuitSignalProxy has never been created.
bool PyQtShortcircuitSignalProxy::no_shortcircuit_signals = true;


// Create the short-circuit signal proxy.
PyQtShortcircuitSignalProxy::PyQtShortcircuitSignalProxy(QObject *parent)
    : QObject()
{
    no_shortcircuit_signals = false;

    // We can't just set the parent because we might be in a different thread.
    moveToThread(parent->thread());
    setParent(parent);
}


// Find an object's short-circuit signal proxy for a signature, if any.
PyQtShortcircuitSignalProxy *PyQtShortcircuitSignalProxy::find(QObject *tx,
        const char *sig)
{
    if (no_shortcircuit_signals)
        return 0;

    // Only check immediate children.
    const QObjectList &kids = tx->children();

    for (int i = 0; i < kids.size(); ++i)
    {
        PyQtShortcircuitSignalProxy *proxy = qobject_cast<PyQtShortcircuitSignalProxy *>(kids.at(i));

        if (proxy && proxy->objectName() == sig)
            return proxy;
    }

    return 0;
}


// Return true if an object is a PyQtShortcircuitSignalProxy instance.  This is
// done without calling qobject_cast() unless absolutely necessary in case the
// object has been deleted.
PyQtShortcircuitSignalProxy *PyQtShortcircuitSignalProxy::shortcircuitSignal(QObject *obj)
{
    if (no_shortcircuit_signals)
        return 0;

    return qobject_cast<PyQtShortcircuitSignalProxy *>(obj);
}
