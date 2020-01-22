#!/usr/bin/python3
"""
Append to a file
function to append a string
at the end of a text file
"""


def append_write(filename="", text=""):
    """function to append"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
