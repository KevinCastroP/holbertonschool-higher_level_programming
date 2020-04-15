#!/usr/bin/python3
"""
Fetching intranet
"""


if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("    - type: {}".format(type(r.text)))
    print("    - content: {}".format(r.text))
