#!/usr/bin/python3
"""
Class that defines a rectangle
"""


class Rectangle:
    """Class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, x):
        if not isinstance(x, int):
            raise TypeError("width must be an integer")
        if x < 0:
            raise ValueError("width must be >= 0")
        self.__width = x

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, y):
        if not isinstance(y, int):
            raise TypeError("height must be an integer")
        if y < 0:
            raise ValueError("height must be >= 0")
        self.__height = y

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        aux = ""
        if self.__width == 0 or self.__height == 0:
            return aux
        for y in range(self.__height):
            for x in range(self.__width):
                aux = aux + str(self.print_symbol)
            if (y + 1) < self.__height:
                aux = aux + "\n"
        return aux

    def __repr__(self):
        command = "Rectangle(" + str(self.__width)
        command = command + ", " + str(self.__height)
        command = command + ")"
        return command

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
