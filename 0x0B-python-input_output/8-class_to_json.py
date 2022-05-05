#!/usr/bin/python3
"""Return the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj (any): is an instance of a Class
    """
    return obj.__dict__
