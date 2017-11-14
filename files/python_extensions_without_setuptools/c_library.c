#include <stdio.h>

#include "c_library.h"


// This is a C library. We can call it from C or use the python bindings
void f(void)
{
    printf("in f() written in C\n");
}
