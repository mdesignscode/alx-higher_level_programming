#!/usr/bin/python3
"""Definition of BaseGeometry"""


class BaseGeometry:
    """a class that has a function that raises an Exception"""

    def area(self):
        """raises an Exception"""
        raise Exception('area() is not implemented')
