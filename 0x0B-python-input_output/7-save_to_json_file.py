#!/usr/bin/python3
"""
Save Object to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """write an obj using json"""
    with open(filename, "w") as k:
        return k.write(json.dumps(my_obj))
