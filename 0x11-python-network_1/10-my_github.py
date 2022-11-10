#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""

from requests import get
from sys import argv


USER = argv[1]
TOKEN = argv[2]
headers = {'Authorization': 'USER:TOKEN'}

if __name__ == '__main__':
    user = get(f'https://api.github.com/users/{USER}', headers=headers)
    print(user.json()['id'])
