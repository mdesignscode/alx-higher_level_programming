#!/usr/bin/python3
"""checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """checks the inheritance of an object

    Args:
        obj (any): the object to be checked
        a_class (any): the class to be checked against
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
