#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""

from requests import get
from sys import argv


USER = argv[1]
TOKEN = argv[2]

if __name__ == '__main__':
    user = get('https://api.github.com/user', auth=(USER, TOKEN))
    try:
        print(user.json()['id'])
    except KeyError:
        print(None)
