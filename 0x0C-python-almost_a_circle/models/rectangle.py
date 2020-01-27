#!/usr/bin/python3
"""
first class Rectangle
"""
from models.base import Base
import json


class Rectangle(Base):
    """first rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """property"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter"""
            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            self.__width = width

        @property
        def height(self):
            """property"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter"""
            if type(height) != int:
                raise TypeError("height must be an integer")
            elif height <= 0:
                raise ValueError("height must be > 0")
            self.__height = height

        @property
        def x(self):
            """property"""
            return self.__X

        @x.setter
        def x(self, x):
            """setter"""
            if type(x) != int:
                raise TypeError("x must be an integer")
            elif x < 0:
                raise ValueError("x must be >= 0")
            self.__x = x

        @property
        def y(self):
            """property"""
            return self.__y

        @y.setter
        def y(self, y):
            """setter"""
            if type(y) != int:
                raise TypeError("y must be an integer")
            elif y < 0:
                raise ValueError("y must be >= 0")
            self.__y = y
