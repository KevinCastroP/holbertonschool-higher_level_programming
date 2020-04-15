#!/usr/bin/python3
"""
Takes in a letter and send a post request
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    r = requests.post(
        'http://0.0.0.0:5000/search_user', data=data)

    try:
        data_dict = r.json()
        if data_dict:
            print("[{}] {}".format(data_dict.get('id'), data_dict.get('name')))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
