#!/usr/bin/python3
"""Base class for all other classes in this module"""
import json


class Base:
    """Base Class

    Args:
        __nb_objects (int): number of instances of class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int, optional): argument value to initialize. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries ([{}]): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        json_file = open(cls.__name__ + ".json", "w")
        if list_objs is None:
            json.dump([], json_file)

        else:
            new_dict = [item.to_dictionary() for item in list_objs]
            json_file.write(cls.to_json_string(new_dict))

        json_file.close()

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string (str): a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0 \
                or not isinstance(json_string, str):
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 20)
            dummy.update(**dictionary)
            return dummy
        else:
            dummy = cls(10)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as file:
                contents = cls.from_json_string(file.read())
                for item in contents:
                    list_instances = []
                    list_instances.append(cls.create(**item))
                    return list_instances

        except FileNotFoundError:
            return []
