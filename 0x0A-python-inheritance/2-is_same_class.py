#!/usr/bin/python3
"""Check if an object is exactly an instance of the specified class
Return True if it is, False if not
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class ; otherwise False

    Args:
        obj (any): the object to be checked
        a_class (any): the class to be checked against
    """
    return type(obj) is a_class
