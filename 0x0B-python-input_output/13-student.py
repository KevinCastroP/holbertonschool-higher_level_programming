#!/usr/bin/python3
"""
Student to disk and reload
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json as attributes"""
        dic = self.__dict__
        if attrs is not None:
            if all(type(x) == str for x in attrs):
                return {x: dic[x] for x in dic if x in attrs}
        return dic

    def reload_from_json(self, json):
        """reload all attributes from json dict"""
        for att in json.keys():
            self.__dict__[att] = json[att]
