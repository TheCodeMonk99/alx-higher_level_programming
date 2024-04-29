#!/usr/bin/python3
"""Checks whether instance is part of a class"""


def is_same_class(obj, a_class):
    """Defines whether object is part of class
       Args:
            Obj
    """
    if type(obj) == a_class:
        return True
    else:
        return False
