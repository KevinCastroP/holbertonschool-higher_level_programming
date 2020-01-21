#!/usr/bin/python3
"""
Only sub class of
if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """verify sub class"""

    return isinstance(obj, a_class) and not type(obj) == a_class
