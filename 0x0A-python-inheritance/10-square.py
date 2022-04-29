#!/usr/bin/python3
"""Definition of Square"""
import 9-rectangle.py


class Square(Rectangle):
    """definition of square

    Args:
        Rectangle (class): class to inherit from
    """

    def __init__(self, size):
        """initialization of square

        Args:
            size (int): size of square
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return the area of square"""
        return self.__size ** 2
