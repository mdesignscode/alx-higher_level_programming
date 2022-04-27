#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :
Text must be a string
There will be no space at the beginning and end of each printed line
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:
    ., ? and :

    Args:
        text (str): text to be printed
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    flag = 0
    for letter in text:
        if letter in ['.', '?', ':']:
            if flag == 0:
                print(letter, end='')
                print('\n')
                flag = 1
        if flag == 1:
            if letter == ' ':
                flag = 0
                continue
        else:
            print(letter, end='')
                
