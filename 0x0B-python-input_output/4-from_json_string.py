#!/usr/bin/python3
"""From JSON to obj"""
import json


def from_json_string(my_str):
    """Converts JSON string to obj"""
    return json.loads(my_str)
