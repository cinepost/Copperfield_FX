// This is the initialisation support code for the QtCore module.
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

#include "qpycore_chimera.h"
#include "qpycore_public_api.h"
#include "qpycore_qobject_helpers.h"
#include "qpycore_sip.h"
#include "qpycore_types.h"


// Perform any required initialisation.
void qpycore_init()
{
    // Initialise the meta-type.
    qpycore_pyqtWrapperType_Type.tp_base = sipWrapperType_Type;

    if (PyType_Ready(&qpycore_pyqtWrapperType_Type) < 0)
        Py_FatalError("PyQt4.QtCore: Failed to initialise pyqtWrapperType type");

    // Register the meta-type.
    if (sipRegisterPyType((PyTypeObject *)&qpycore_pyqtWrapperType_Type) < 0)
        Py_FatalError("PyQt4.QtCore: Failed to register pyqtWrapperType type");

    // Export the private helpers.
    sipExportSymbol("qtcore_qt_metaobject",
            (void *)qpycore_qobject_metaobject);
    sipExportSymbol("qtcore_qt_metacall", (void *)qpycore_qobject_qt_metacall);
    sipExportSymbol("qtcore_qt_metacast", (void *)qpycore_qobject_qt_metacast);
    sipExportSymbol("qpycore_qobject_sender", (void *)qpycore_qobject_sender);
    sipExportSymbol("qpycore_qobject_receivers",
            (void *)qpycore_qobject_receivers);

    // Export the public API.
    sipExportSymbol("pyqt4_from_argv_list", (void *)pyqt4_from_argv_list);
    sipExportSymbol("pyqt4_from_qvariant_by_type",
            (void *)pyqt4_from_qvariant_by_type);
    sipExportSymbol("pyqt4_get_connection_parts",
            (void *)pyqt4_get_connection_parts);
    sipExportSymbol("pyqt4_get_pyqtsignal_parts",
            (void *)pyqt4_get_pyqtsignal_parts);
    sipExportSymbol("pyqt4_get_pyqtslot_parts",
            (void *)pyqt4_get_pyqtslot_parts);
    sipExportSymbol("pyqt4_get_signal", (void *)pyqt4_get_signal);
    sipExportSymbol("pyqt4_get_slot", (void *)pyqt4_get_slot);
    sipExportSymbol("pyqt4_register_from_qvariant_convertor",
            (void *)Chimera::registerToPyObject);
    sipExportSymbol("pyqt4_register_to_qvariant_convertor",
            (void *)Chimera::registerToQVariant);
    sipExportSymbol("pyqt4_register_to_qvariant_data_convertor",
            (void *)Chimera::registerToQVariantData);
    sipExportSymbol("pyqt4_update_argv_list", (void *)pyqt4_update_argv_list);
}
