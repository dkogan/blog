#include <Python.h>
#include <stdio.h>

#include "c_library.h"

static PyObject* f_py(PyObject* self __attribute__((unused)),
                      PyObject* args __attribute__((unused)))
{
    printf("in f() python wrapper. About to call C library\n");
    f();
    Py_RETURN_NONE;
}


PyMODINIT_FUNC initc_library(void)
{
    static PyMethodDef methods[] =
        { {"f", (PyCFunction)f_py, METH_NOARGS, "Python bindings to f() in c_library\n"},
          {}
        };


    PyImport_AddModule("c_library");
    Py_InitModule3("c_library", methods,
                   "Python bindings to c_library");
}
