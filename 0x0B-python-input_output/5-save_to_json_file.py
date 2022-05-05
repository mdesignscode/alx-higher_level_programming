#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
json = __import__('json')


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (object): python object to convert to json object
        filename (str): name of file to write to
    """
    with open(filename, "w") as file:
        json_obj = json.dumps(my_obj)
        file.write(json_obj)
