"""Add Two Integers
both a and b must be integers or floats
if a or b is float, it will be casted to int
only first value can be give
The second is 98 by default
"""


def add_integer(a, b=98):
    """adds 2 integers

    Args:
        a (int/float): first number.
        b (int, optional): number to be added. Defaults to 98.
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
