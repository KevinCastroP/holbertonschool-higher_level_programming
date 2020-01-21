#!/usr/bin/python3
"""
new class Rectangle
with weidth and height
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
