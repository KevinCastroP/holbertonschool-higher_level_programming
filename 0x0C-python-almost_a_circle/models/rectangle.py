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

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """property"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """property"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
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
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """adding area to rectangle"""
        return self.__width * self.__height

    def display(self):
        """printing the rectangle with # symbol"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """string representation of rectangle"""
        my_id = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(my_id, x, y, w, h)
