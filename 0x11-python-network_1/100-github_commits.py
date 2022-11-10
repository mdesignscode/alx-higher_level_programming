#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”"""

from requests import get
from sys import argv


if __name__ == '__main__':
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    params = {"sort": "date"}
    response =  get(url, )

    for index, commit in enumerate(response.json()):
        sha, author = commit['sha'], commit['commit']['author']['name']
        print(f'{sha}: {author}')
        if index == 9:
            break
