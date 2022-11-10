#!/usr/bin/python3
"""sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""

from requests import get
from sys import argv


if __name__ == '__main__':
    response = get(argv[1])
    print(response.headers["X-Request-Id"])
