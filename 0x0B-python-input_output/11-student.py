#!/usr/bin/python3
"""Defines a student by:
    first_name
    last_name
    age
"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """initialization of student

        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Args:
            attrs (any, optional): attributes to retrieve. Defaults to None.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except KeyError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
            json (json_obj): json object to replace Student instance attributes
        """
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
