#!/usr/bin/python3
"""Definition of Rectangle"""


from models.base import Base


class Rectangle(Base):
    """define a rectangle object

    Args:
        Base (class): Base Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle constructor

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): x offset of rectangle. Defaults to 0.
            y (int, optional): y offset of rectangle. Defaults to 0.
            id (int, optional): identifier. Defaults to None.
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 1:
            raise ValueError('width must be > 0')
        self.width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 1:
            raise ValueError('height must be > 0')
        self.height = height

        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.x = x


        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.y = y


        @property
        def width(self):
            """Getter and Setter methods for width"""
            return self.width

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError('width must be an integer')
            if value < 1:
                raise ValueError('width must be > 0')
            self.width = value

        @property
        def height(self):
            """Getter and Setter methods for height"""
            return self.height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError('height must be an integer')
            if value < 1:
                raise ValueError('height must be > 0')
            self.height = value

        @property
        def x(self):
            """Getter and Setter methods for x"""
            return self.x

        @x.setter
        def x(self, value):
            if type(value) is not int:
                raise TypeError('x must be an integer')
            if value < 0:
                raise ValueError('x must be >= 0')
            self.x = value

        @property
        def y(self):
            """Getter and Setter methods for y"""
            return self.y

        @y.setter
        def y(self, value):
            if type(value) is not int:
                raise TypeError('y must be an integer')
            if value < 0:
                raise ValueError('y must be >= 0')
            self.y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print(('\n' * self.y) + '\n'
              .join(' ' * self.x + '#' * self.width
                    for _ in range(self.height)))

    def __str__(self):
        """Returns an informal string representation a Rectangle object"""
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.x, self.y,
                    self.width, self.height)

    def update(self, *args, **kwargs):
        """update the instance attributes"""
        if len(kwargs):
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return self.__dict__
