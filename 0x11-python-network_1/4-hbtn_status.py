#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

from requests import get

if __name__ == '__main__':
    response = get("https://alx-intranet.hbtn.io/status")
    print('Body response:')
    for key, value in response.headers.items():
        print(f'\t- {key}: {value}')
