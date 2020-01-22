#!/usr/bin/python3
"""
Only sub class of
if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """verify sub class"""

    for base in obj.__class__.__bases__:
        if type(obj) == str(a_class):
            return True
        for bas in base.__class__.__bases__:
            if type(obj) == str(a_class):
                return True
    return False
