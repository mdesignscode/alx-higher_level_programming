#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str, optional): name of file to append to. Defaults to "".
        text (str, optional): string to append. Defaults to "".
    """
    with open(filename, "a") as file:
        written = file.write(text)
    return written
