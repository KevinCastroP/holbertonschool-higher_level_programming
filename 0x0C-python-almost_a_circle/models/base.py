#!/usr/bin/python3
"""
creating the first class Base
"""
import json


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
