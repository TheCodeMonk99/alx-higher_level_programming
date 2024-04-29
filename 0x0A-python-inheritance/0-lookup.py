#!/usr/bin/python3
"""This returns a list of all attributes, methods, and properties
   an object"""


def lookup(obj):
    """Returns a list of all attributes
    Args:
        obj (obj): Object in question
    """
    return dir(obj)
