#!/usr/bin/python3
"""
Square #2
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """init function"""
        super().integer_validator("size", size)
        self._Rectangle__width = size
        self._Rectangle__height = size
        self.__size = size

    def __str__(self):
        """str"""
        return "[Square] {}/{}".format(self.__size, self.__size)
