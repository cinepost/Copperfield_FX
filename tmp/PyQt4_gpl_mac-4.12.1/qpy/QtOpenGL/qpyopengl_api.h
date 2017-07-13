// This defines the API provided by this library.  It must not be explicitly
// included by the library itself.
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


#ifndef _QPYOPENGL_API_H
#define _QPYOPENGL_API_H


#include <QtGlobal>

#if QT_VERSION >= 0x040600

#include <qgl.h>


// Support for shader arrays.
const GLfloat *qpyopengl_attribute_array(PyObject *values, PyObject *shader,
        PyObject *key, int *tsize, sipErrorState *estate);
const void *qpyopengl_uniform_value_array(PyObject *values, PyObject *shader,
        PyObject *key, const sipTypeDef **array_type, int *array_len,
        int *tsize, sipErrorState *estate);


#endif

#endif
