#!/usr/bin/python3
"""
Exact same object
function to prove if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """prove object"""

    if type(obj) is a_class:
        return True

    else:
        return False
