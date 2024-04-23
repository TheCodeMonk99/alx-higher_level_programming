#!/usr/bin/python3

"""This class defines a square"""


class Square:
    """This defines and initializes a square"""

    def __init__(self, size=0):
        """Initializes a square of size

        Args:
            size (int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets size
        Args:
            value (int): size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """This calculates the area of the square"""
    def area(self):
        """Calculate area
        Args:
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
