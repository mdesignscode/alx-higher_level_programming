#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)"""

from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    data = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], data=data)
    with request.urlopen(req) as resp:
        print(resp.read().decode("UTF-8"))
