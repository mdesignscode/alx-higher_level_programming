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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
