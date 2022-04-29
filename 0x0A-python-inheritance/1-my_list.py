#!/usr/bin/python3
"""a class MyList that inherits from the class list
the class has a Public instance method
that prints the list, but sorted (ascending sort)
all the elements of the list should be of type int
"""


class MyList(list):
    """inherits from the class list

    Args:
        list (list): the class to inherit from
    """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """
        return sorted(self)
