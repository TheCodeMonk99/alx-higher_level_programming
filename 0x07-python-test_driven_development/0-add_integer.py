#!/usr/bin/python3
"""Defines integer additon"""


def add_integer(a, b=98):
    """ Sums a and b
    Args:
        a (int): first int
        b (int): second int
    Float: converts float to int
    Raises: TypeError: If either of a or b is non-interger and
    non-foat
    """
    if ((not isinstance(a, int)) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
