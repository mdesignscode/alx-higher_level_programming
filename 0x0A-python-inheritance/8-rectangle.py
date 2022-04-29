#!/usr/bin/python3
"""definition of rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """definition of rectangle

    Args:
        BaseGeometry (class): base class to inherit from
    """

    def __init__(self, width, height):
        """initialization of rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
