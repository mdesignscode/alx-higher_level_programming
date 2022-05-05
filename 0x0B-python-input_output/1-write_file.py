#!/usr/bin/python3
"""writes a string to a text file (UTF8) and
returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str, optional): name of file to be read. Defaults to "".
        text (str, optional): the text to write/overwrite to file. Defaults to "".
    """
    with open(filename, "w", encoding="utf-8") as file:
        written = file.write(text)
    return written
