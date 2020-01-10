#!/usr/bin/python3
class Square:
    """Square with size."""

    def __init__(self, size = None):
        if size is not None:
            self.__size = size
