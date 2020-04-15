#!/usr/bin/python3
"""
Fetching intranet
"""


if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    body = r.text
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
