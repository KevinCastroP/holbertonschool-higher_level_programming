#!/usr/bin/python3
"""
add_integer - Function that sum two integers
a: integer
b: integer initializated to 98 by default
"""

def add_integer(a, b=98):
    """
        Add two integers
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
