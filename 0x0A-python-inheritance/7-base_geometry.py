#!/usr/bin/python3
"""Validate the given value"""


class BaseGeometry:
    """Definition of BaseGeometry"""

    def area(self):
        """raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): name associated with value
            value (int): value to be checked
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 1:
            raise ValueError('{} must be greater than 0'.format(name))
