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

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self) -> str:
        """return the string [Rectangle] <width>/<height>"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
