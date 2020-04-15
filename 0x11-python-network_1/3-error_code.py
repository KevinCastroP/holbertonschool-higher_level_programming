#!/usr/bin/python3
"""
Display the body of the response
"""


if __name__ == "__main__":
    from urllib import request, error
    import sys

    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
