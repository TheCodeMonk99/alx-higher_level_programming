#!/usr/bin/python3

"""This class has squares"""


class Square:
    """This defines the square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the object
        Args:
            size (int): size of square
            position (tuple): position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be => 0")
        self.__size = value

    @property
    def position(self):
        """Returns position of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
