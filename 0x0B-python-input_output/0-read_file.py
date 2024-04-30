#!/usr/bin/python3
"""This is a module that deals with input output"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it
    to standard output
    Args:
        filename: the name of the file
    """
    with open(filename, 'r', encoding="utf8") as f:
        for line in f:
            print(line, end='')
