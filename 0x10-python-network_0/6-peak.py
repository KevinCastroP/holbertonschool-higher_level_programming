#!/usr/bin/python3
"""
Find the peak of a list
"""


def find_peak(list_of_integers):
    """Function to find the max integer"""
    _list = list_of_integers
    empty = None
    if _list == []:
        return(empty)
    else:
        return(max(_list))
