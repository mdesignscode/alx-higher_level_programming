#!/usr/bin/python3
"""Create an Object from a “JSON file”"""
json = __import__('json')


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
        filename (str): name of the file to create Object from
    """
    with open(filename) as file:
        file_read = file.read()
        json_object = json.loads(file_read)
    return json_object
