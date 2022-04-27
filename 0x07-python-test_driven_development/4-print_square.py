#!/usr/bin/python3
"""Print a square with the character #
the size of the square must be an int
and size must be positive
size should not be float
"""


def print_square(size):
    """prints a square with the character #

    Args:
        size (int): size of square to be printed
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        print()

    for _ in range(1, size + 1):
        [print('#', end='') for _ in range(1, size + 1)]
        print()
