#!/usr/bin/python3
"""
converting From JSON string to Object
"""


def from_json_string(my_str):
    """convert string to object with json"""

    new_obj = json.loads(my_str)
    return new_obj
