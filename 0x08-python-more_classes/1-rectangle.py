#!/usr/bin/python3
"""
Class that defines a rectangle
"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, a):
        if not isinstance(a, int):
            raise TypeError("width must be an integer")
        if a < 0:
            raise ValueError("width must be >= 0")
        self.__width = a

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, b):
        if not isinstance(b, int):
            raise TypeError("height must be an integer")
        if b < 0:
            raise ValueError("height must be >= 0")
        self.__height = b
