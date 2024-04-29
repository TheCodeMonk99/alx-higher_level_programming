#!/usr/bin/python3
"""Class that is base geometry"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Defines the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer
        Args:
            name (string)
            value (int)
        Raises:
            TypeError if name is not int and is not greater than o
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Class Rectangle inherited from BaseGeometry"""

    def __init__(self, width,height):
        """Defines the dimension of rectangle

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.___height = height
