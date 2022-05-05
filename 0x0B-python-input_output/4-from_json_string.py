#!/usr/bin/python3
"""returns an object (Python data structure) represented by a JSON string"""
json = __import__('json')


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (json): string to be converted to python object.
    """
    return json.loads(my_str)
