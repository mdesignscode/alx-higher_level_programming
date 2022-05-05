#!/usr/bin/python3
"""Read a text file encoded in UTF8 and print it to stdout"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): name of the file to be read. Defaults to "".
    """
    with open(filename) as file:
        contents = file.read()
        print(contents, end='')
