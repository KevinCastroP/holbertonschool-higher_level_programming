#!/usr/bin/python3
"""
print_square - prints a square with #
size: size of the square
"""

def print_square(size):
    """
    Method to print a square
    """
    error1 = "size must be an integer"
    error2 = "size must be >= 0"
    if not (isinstance(size, int)):
        raise TypeError(error1)
    if size < 0:
        raise ValueError(error2)
    if not (isinstance(size, float)) and size < 0:
        raise TypeError(error1)
    for count1 in range(size):
        for count2 in range(size):
            print("#", end='')
        print()
    if size == 0:
        print()
