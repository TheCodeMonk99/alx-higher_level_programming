#!/usr/bin/python3
"""Determines a string to JSON function"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of obj"""
    return json.dumps(my_obj)
