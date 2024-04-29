#!/usr/bin/python3
"""Class from list"""


class MyList(list):
    """This list is superb"""
    def __init__(self):
    """Initializes object"""
    super().__init__()    
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
