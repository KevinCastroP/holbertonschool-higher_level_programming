#!/usr/bin/python3
"""
MyList inherits from list
list: father
"""


class MyList(list):
    """my user class"""

    def print_sorted(self):
        print(sorted(self))
