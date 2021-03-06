#!/usr/bin/python3
"""
Only sub class of
if the object is an instance of a class
that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """Evaluates if an object is a sub class instance of a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
