#!/usr/bin/python2

r'''A module written in python'''

import c_library

def g():
    r'''some function'''
    print "in my written-in-python module g(). Calling c_library.f()"
    c_library.f()

