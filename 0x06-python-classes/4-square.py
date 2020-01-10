#!/usr/bin/python3
class Square:
    """Access and update private attribute"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """# of the area"""
        return self.__size ** 2

    @property
    def size(self):
        """print the square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter the square area"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
