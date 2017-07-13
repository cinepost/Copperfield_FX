// This contains the definition of the PyQtProxy class.
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


#ifndef _QPYCORE_PYQTPROXY_H
#define _QPYCORE_PYQTPROXY_H


#include <Python.h>

#include <QByteArray>
#include <QMultiHash>
#include <QList>
#include <QMetaObject>
#include <QMutex>
#include <QObject>

#include "qpycore_chimera.h"
#include "qpycore_namespace.h"
#include "qpycore_sip.h"
#include "qpycore_types.h"


// In case we are using SIP v5.
#if !defined(SIP_SINGLE_SHOT)
#define SIP_SINGLE_SHOT     0x01
#endif


class PyQt_PyObject;


// This class is used as a signal on behalf of Python signals and as a slot on
// behalf of Python callables.  It is derived from QObject but is not run
// through moc.  Instead the normal moc-generated methods are handwritten in
// order to implement a universal signal or slot.  This requires some knowledge
// of the internal implementation of signals and slots but it is likely that
// they will only change between major Qt versions.
class PyQtProxy : public QObject
{
public:
    // The different roles a proxy can fulfill.  It might have been better to
    // implement each as a sub-class.
    enum ProxyType {
        ProxySlot,
        ProxySignal,
    };

    PyQtProxy(QObject *qtx, const char *sig);
    PyQtProxy(sipWrapper *txObj, const char *sig, PyObject *rxObj,
            const char *slot, const char **member, int flags);
    PyQtProxy(QObject *qtx, const Chimera::Signature *signal_signature,
            PyObject *rxObj, const char **member, int flags);
    ~PyQtProxy();

    static const QMetaObject staticMetaObject;
    virtual const QMetaObject *metaObject() const;
    virtual void *qt_metacast(const char *);
    virtual int qt_metacall(QMetaObject::Call, int, void **);

    void unislot(void **qargs);
    static PyObject *invokeSlot(const qpycore_slot &slot, void **qargs,
            int no_receiver_check = 0);
    void disable();

    int getReceivers(const char *signal) const {return receivers(signal);}

    static void deleteSlotProxies(void *tx, const char *sig);

    static PyQtProxy *findSlotProxy(void *tx, const char *sig, PyObject *rxObj,
            const char *slot, const char **member);

    void disableReceiverCheck();

#if SIP_VERSION >= 0x050000
    static int clearSlotProxies(const QObject *transmitter);
    static int visitSlotProxies(const QObject *transmitter, visitproc visit,
            void *arg);
#endif

    // The type of a proxy hash.
    typedef QMultiHash<void *, PyQtProxy *> ProxyHash;

    // Each proxy type is held in a different hash.
    static ProxyHash proxy_slots;
    static ProxyHash proxy_signals;

    // The mutex around the proxies hashes.
    static QMutex *mutex;

    // The proxy type.
    ProxyType type;

    // The proxy flags.
    int proxy_flags;

    // The normalised signature.
    QByteArray signature;

    // Set if the proxy is in a hash.
    bool hashed;

    // The QObject transmitter we are proxying for (if any).
    QObject *transmitter;

    // The slot we are proxying for.  (Only used when type is ProxySlot.)
    qpycore_slot real_slot;

    // The last QObject sender.
    static QObject *last_sender;

private:
    void init(QObject *qtx, ProxyHash *hash, void *key);
    void remove();

    // This object's key in the relevant hash.
    void *saved_key;

    // The meta-object.
    const QMetaObject *meta_object;

    PyQtProxy(const PyQtProxy &);
    PyQtProxy &operator=(const PyQtProxy &);
};


// This acts as a proxy for short-circuit signals.  The parent is the object we
// are proxying for.  The object name is the name of the signal.
class PyQtShortcircuitSignalProxy : public QObject
{
    Q_OBJECT

public:
    PyQtShortcircuitSignalProxy(QObject *parent);

    int getReceivers(const char *signal) const {return receivers(signal);}

    void emit_signal(const PyQt_PyObject &args) {emit pysignal(args);}

    static PyQtShortcircuitSignalProxy *find(QObject *tx, const char *sig);
    static PyQtShortcircuitSignalProxy *shortcircuitSignal(QObject *obj);

signals:
    void pysignal(const PyQt_PyObject &);

private:
    static bool no_shortcircuit_signals;
};


#endif
