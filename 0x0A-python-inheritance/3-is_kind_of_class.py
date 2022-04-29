#!/usr/bin/python3
"""Check if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """check the instance of an object

    Args:
        obj (any): the object to be checked
        a_class (any): the class to be checked against
    """
    return isinstance(obj, a_class)
