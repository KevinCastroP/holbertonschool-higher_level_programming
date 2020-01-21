#!/usr/bin/python3
"""
Full Rectangle
define arguments of Rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """init function"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)