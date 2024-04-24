#!/usr/bin/python3
"""This defines rectangles"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """This initializes the rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
