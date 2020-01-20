#!/usr/bin/python3
"""
Low memory cost
a class with no object attribute
creating  new instance attribute except if is first_name
"""


class LockedClass():
    __slots__ = ["first_name"]
