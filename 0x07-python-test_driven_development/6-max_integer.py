#!/usr/bin/python3
"""This funcition find max integer in list"""


def max_integer(list=[]):
    """Function to find max int in list
        if the list is empty it returns None
    """
    if len(list) == 0:
        return None
    max_int = list[0]
    next_int = 1
    while next_int < len(list):
        if list[next_int] > max_int:
            max_int = list[next_int]
        next_int += 1
    return max_int
