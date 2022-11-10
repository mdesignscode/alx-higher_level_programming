#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

from urllib import request

if __name__ == '__main__':
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        print('Body response:')
        for key, value in response.getheaders():
            print(f'\t- {key}: {value}')
