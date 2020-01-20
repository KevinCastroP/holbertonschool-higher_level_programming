#!/usr/bin/python3
def magic_string(a=[0]):
    a[0] = a[0] + 1
    return "Holberton" + (", Holberton" * (a[0] - 1))
