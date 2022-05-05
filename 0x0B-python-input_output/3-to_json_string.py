#!/usr/bin/python3
"""Return the JSON representation of an object (string)"""
json = __import__('json')


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj (any): data to be converted to JSON object
    """
    return json.dumps(my_obj)
