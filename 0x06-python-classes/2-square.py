#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """This defines and initializes a square"""

    def __init__(self, size=0):
        """Initializes a square of size

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
