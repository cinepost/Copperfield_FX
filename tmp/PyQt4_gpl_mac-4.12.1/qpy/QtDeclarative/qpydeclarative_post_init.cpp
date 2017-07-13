// This is the initialisation support code for the QtDeclarative module.
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

#include "sipAPIQtDeclarative.h"

#include "qpydeclarative_chimera_helpers.h"
#include "qpydeclarativelistproperty.h"


// Perform any required initialisation.
void qpydeclarative_post_init(PyObject *module_dict)
{
    // Initialise the QPyDeclarativeListProperty type.
#if PY_MAJOR_VERSION >= 3
    qpydeclarative_QPyDeclarativeListProperty_Type.tp_base = &PyUnicode_Type;
#else
    qpydeclarative_QPyDeclarativeListProperty_Type.tp_base = &PyString_Type;
#endif

    if (PyType_Ready(&qpydeclarative_QPyDeclarativeListProperty_Type) < 0)
        Py_FatalError("PyQt4.QtDeclarative: Failed to initialise QPyDeclarativeListProperty type");

    // Create the only instance and add it to the module dictionary.
    PyObject *inst = PyObject_CallFunction(
            (PyObject *)&qpydeclarative_QPyDeclarativeListProperty_Type,
            const_cast<char *>("s"), "QDeclarativeListProperty<QObject>");

    if (!inst)
        Py_FatalError("PyQt4.QtDeclarative: Failed to create QPyDeclarativeListProperty instance");

    if (PyDict_SetItemString(module_dict, "QPyDeclarativeListProperty", inst) < 0)
        Py_FatalError("PyQt4.QtDeclarative: Failed to set QPyDeclarativeListProperty instance");

    // Get the Chimera helper registration functions.
    void (*register_from_qvariant)(FromQVariantFn);
    register_from_qvariant = (void (*)(FromQVariantFn))sipImportSymbol(
            "pyqt4_register_from_qvariant_convertor");
    Q_ASSERT(register_from_qvariant);
    register_from_qvariant(qpydeclarative_from_qvariant);

    void (*register_to_qvariant)(ToQVariantFn);
    register_to_qvariant = (void (*)(ToQVariantFn))sipImportSymbol(
            "pyqt4_register_to_qvariant_convertor");
    Q_ASSERT(register_to_qvariant);
    register_to_qvariant(qpydeclarative_to_qvariant);

    void (*register_to_qvariant_data)(ToQVariantDataFn);
    register_to_qvariant_data = (void (*)(ToQVariantDataFn))sipImportSymbol(
            "pyqt4_register_to_qvariant_data_convertor");
    Q_ASSERT(register_to_qvariant_data);
    register_to_qvariant_data(qpydeclarative_to_qvariant_data);
}
