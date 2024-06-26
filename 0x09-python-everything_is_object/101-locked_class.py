#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    instantiating new LockedClass attributes
    but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
