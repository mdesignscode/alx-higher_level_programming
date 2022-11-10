#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

from requests import post
from sys import argv


letter = "" if len(argv) == 1 else argv[1]


if __name__ == '__main__':
    response = post("http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        json = response.json()

        if not len(json):
            print('No result')
        else:
            print(f'[{json["id"]}] {json["name"]}')

    except Exception:
        print('Not a valid JSON')
