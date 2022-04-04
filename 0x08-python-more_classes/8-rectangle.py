#!/usr/bin/python3
"""return the biggest rectangle based on the area"""


class Rectangle:
    """defines a rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize the dimensions of a rectangle

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieving width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width of a rectangle

        Args:
            value (int): width of new rectangle
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise TypeError('width must be >= 0')

    @property
    def height(self):
        """retrieving height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height of a rectangle

        Args:
            value (int): height of new rectangle
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise TypeError('height must be >= 0')

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """prints a rectangle using 'print_symbol'"""
        height = self.__height
        width = self.__width
        n_s = str(self.print_symbol)
        if width == 0 or height == 0:
            return ""
        return '\n'.join(self.print_symbol * width for _ in range(height))

    def __repr__(self):
        """return a Rectangle object to be used in eval"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints goodbye rectangle when an instance is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle object): rectangle one
            rect_2 (Rectangle object): rectangle two
        """
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif area_1 == area_2  or area_1 > area_2:
            return rect_1
        else:
            return rect_2
