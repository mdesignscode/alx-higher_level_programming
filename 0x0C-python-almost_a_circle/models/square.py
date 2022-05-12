#!/usr/bin/python3
"""Definition of Square Object"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a Square object

    Args:
        Rectangle (class): Sub Class to inherit from
    """

    def __init__(self, size, x=0, y=0, id=None):
        """square constructor

        Args:
            size (int, optional): size of square
            x (int, optional): x offset of square. Defaults to 0.
            y (int, optional): y offset of square. Defaults to 0.
            id (int, optional): identifier . Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns an informal representation of a square object"""
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter and Setter methods for size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if not args and not kwargs:
            return

        if args:
            attrs = ['id', 'size', 'x', 'y']
            for index, value in enumerate(args):
                setattr(self, attrs[index], value)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
