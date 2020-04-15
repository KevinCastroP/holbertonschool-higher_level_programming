#!/usr/bin/python3
"""
Displaying the body of response
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])

    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
