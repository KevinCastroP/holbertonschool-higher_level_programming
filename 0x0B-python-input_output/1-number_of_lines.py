#!/usr/bin/python3
"""
Number of lines
function to print the number of lines
of a text file
"""


def number_of_lines(filename=""):
    """number of lines"""
    count = 0
    with open(filename) as k:
        for line in k:
            count += 1
        return count
