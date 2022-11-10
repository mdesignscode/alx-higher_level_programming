#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the response"""

from requests import get
from sys import argv


if __name__ == '__main__':
    response = get(argv[1])
    if response.status_code > 399:
        print(f'Error code: {response.status_code}')
    else:
        print(response.text)
