"""Return the list of available attributes and methods of an object
obj is the object to return the list for
"""


def lookup(obj):
    """Returns a list object

    Args:
        obj (any): the object to return the list for
    """
    return dir(obj)
