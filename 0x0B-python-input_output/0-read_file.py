#!/usr/bin/python3
"""
Read ile
function to read a text file
and printed
"""


def read_file(filename=""):
    """method to read a file text"""
    with open(filename, encoding='utf-8') as k:
        print (k.read(), end="")