// This implements the public API provided by PyQt to external packages.
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
#include <QHash>

#include "qpycore_chimera.h"
#include "qpycore_public_api.h"
#include "qpycore_pyqtboundsignal.h"


// Convert a Python argv list to a conventional C argc count and argv array.
char **pyqt4_from_argv_list(PyObject *argv_list, int &argc)
{
    argc = PyList_GET_SIZE(argv_list);

    // Allocate space for two copies of the argument pointers, plus the
    // terminating NULL.
    char **argv = new char *[2 * (argc + 1)];

    // Convert the list.
    for (int a = 0; a < argc; ++a)
    {
        PyObject *arg_obj = PyList_GET_ITEM(argv_list, a);
        char *arg;

        if (PyUnicode_Check(arg_obj))
        {
            QByteArray ba_arg = qpycore_PyObject_AsQString(arg_obj).toLocal8Bit();
            arg = qstrdup(ba_arg.constData());
        }
        else if (SIPBytes_Check(arg_obj))
        {
            arg = qstrdup(SIPBytes_AS_STRING(arg_obj));
        }
        else
        {
            arg = const_cast<char *>("invalid");
        }

        argv[a] = argv[a + argc + 1] = arg;
    }

    argv[argc + argc + 1] = argv[argc] = NULL;

    return argv;
}


// Get the receiver object and slot signature for a connection.
sipErrorState pyqt4_get_connection_parts(PyObject *slot, QObject *transmitter,
        const char *signal_signature, bool single_shot, QObject **receiver,
        QByteArray &slot_signature)
{ 
    static QHash<QByteArray, const Chimera::Signature *> cache;

    QByteArray key(signal_signature);
    const Chimera::Signature *parsed_signal_signature = cache.value(key);

    if (!parsed_signal_signature)
    {
        parsed_signal_signature = Chimera::parse(key, "a signal argument");

        if (!parsed_signal_signature)
            return sipErrorFail;

        cache.insert(key, parsed_signal_signature);
    }

    return qpycore_get_receiver_slot_signature(slot, transmitter,
            parsed_signal_signature, single_shot, receiver, slot_signature);
}


// Remove arguments from the Python argv list that have been removed from the
// C argv array.
void pyqt4_update_argv_list(PyObject *argv_list, int argc, char **argv)
{
    for (int a = 0, na = 0; a < argc; ++a)
    {
        // See if it was removed.
        if (argv[na] == argv[a + argc + 1])
            ++na;
        else
            PyList_SetSlice(argv_list, na, na + 1, 0);
    }
}
