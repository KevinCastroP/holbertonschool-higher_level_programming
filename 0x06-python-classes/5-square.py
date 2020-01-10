#!/usr/bin/python3
class Square():
    """Printing a square"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """# of square area"""
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

    def my_print(self):
        """printing square"""
        for count1 in range(self.__size):
            for count2 in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
            print()
