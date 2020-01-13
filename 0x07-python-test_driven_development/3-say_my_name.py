#!/usr/bin/python3
"""
say_my_name - print name and last name
first_name: first name
last_name: last name
"""
def say_my_name(first_name, last_name=""):
    """
    Method to say hello
    """
    error1 = "first_name must be a string"
    error2 = "last_name must be a string"
    if not (isinstance(first_name, str)):
        raise TypeError(error1)
    if not (isinstance(last_name, str)):
        raise TypeError(error2)
    print("My name is {} {}".format(first_name, last_name))
