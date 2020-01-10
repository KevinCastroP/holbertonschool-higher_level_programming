#!/usr/bin/python3
class Square():
    """Coordinates of a square"""
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

    def my_print(self):
        """printing square"""
        if self.__size > 0:
            for count1 in range(self.__position[1]):
                print()
            for count2 in range(self.__size):
                for count3 in range(self.__position[0]):
                    print(" ", end='')
                for count4 in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()

    @property
    def position(self):
        """print the tuple position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter value size"""
        if len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = (value[0], value[1])
                else:
                    raise TypeError("position must be a tuple of 2 positive integers")
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """initializtion"""
        self.__size = size
        self.__position = position
