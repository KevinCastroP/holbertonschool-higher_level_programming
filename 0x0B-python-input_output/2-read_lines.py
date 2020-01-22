#!/usr/bin/python3
"""
Read n lines
function to print n lines
of a text file
"""


def read_lines(filename="", nb_lines=0):
    """number of lines"""
    count = 0
    with open(filename) as k:
        txt = k.readlines()
        if nb_lines <= 0 or nb_lines >= len(txt):
            for c in txt:
                print(c, end="")
        else:
            for c in range(nb_lines):
                print(txt[c], end="")
