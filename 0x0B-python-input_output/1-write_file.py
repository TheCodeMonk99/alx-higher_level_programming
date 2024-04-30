#!/usr/bin/python3
"""This function writes a string to a file
   creates a file if none
   overwrites the content of file if none
"""


def write_file(filename="", text=""):
    """writes to a file/overwrites it
    Args:
        filename: filename
        text: string to print
    """
    with open(filename, 'w', encoding="utf8") as f:
        nb_characters = f.write(text)
        return nb_characters
