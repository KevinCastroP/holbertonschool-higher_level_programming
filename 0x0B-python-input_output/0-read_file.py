#!/usr/bin/python3
"""
Read file
function to read a text file
and printed
"""


def read_file(filename=""):
    """method to read a file text"""
    with open(filename, 'r', encoding='utf-8') as k:
        print(k.read(), end="")
        k.close()
