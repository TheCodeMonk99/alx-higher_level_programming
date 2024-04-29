#!/usr/bin/python3
"""Checks if obj is instance or subclass of class"""


def is_kind_of_class(obj, a_class):
    """Finds if obj is an instance of class
    Args:
        obj (class): instance of class
        a_class (class): the class in question
    Returns:
        True if it is part of instance
        False if not instance or subclass
    """
    if (isinstance(obj, a_class) or issubclass(obj, a_class)):
        return True
    else:
        return False
