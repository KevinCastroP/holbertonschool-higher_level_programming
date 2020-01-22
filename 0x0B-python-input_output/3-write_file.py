#!/usr/bin/python3
"""
Write to a file
function to write a string
to a text file and return the number of characters
"""


def write_file(filename="", text=""):
    """write into a file"""
    with open(filename, 'w', encoding='utf-8') as k:
        return(k.write(text))
