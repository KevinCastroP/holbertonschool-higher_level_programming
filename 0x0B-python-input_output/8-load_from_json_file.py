#!/usr/bin/python3
"""
Create object from a JSON file
"""


import json


def load_from_json_file(filename):
    """creating object from json file"""
    with open(filename, "r") as k:
        return json.loads(k.read())
