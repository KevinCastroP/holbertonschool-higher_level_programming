#!/usr/bin/python3
"""
Take my github credentials and display my Id
"""


if __name__ == "__main__":

    from requests import get, auth
    from sys import argv

    r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
