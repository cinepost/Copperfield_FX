// This is the initialisation support code for the QtDBus module.
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

#include "sipAPIQtDBus.h"

#include "qpydbus_chimera_helpers.h"


// Perform any required initialisation.
void qpydbus_post_init()
{
    // Get the Chimera helper registration function.
    void (*register_from_qvariant)(FromQVariantFn);
    register_from_qvariant = (void (*)(FromQVariantFn))sipImportSymbol(
            "pyqt4_register_from_qvariant_convertor");
    Q_ASSERT(register_from_qvariant);
    register_from_qvariant(qpydbus_from_qvariant);
}
