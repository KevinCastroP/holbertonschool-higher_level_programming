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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None:
            return "[]"
        ans = json.dumps(list_dictionaries)
        return ans

    @classmethod
    def save_to_file(cls, list_objs):
        """parse to json an write the value on a file"""
        string = "[]"
        if list_objs is not None:
            dics = [di.to_dictionary() for di in list_objs]
            string = cls.to_json_string(dics)
        with open(cls.__name__ + ".json", "w") as file:
            file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """return objects list from json string"""
        lis = []
        if json_string is not None:
            lis = json.loads(json_string)
        return lis

    @classmethod
    def create(cls, **dictionary):
        """create function"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        try:
            f = open(str(cls.__name__) + ".json")
            f.close()
        except:
            return []

        l = []
        with open(str(cls.__name__) + ".json", "r") as f:
            l = cls.from_json_string(f.read())

        num_ins = len(l)
        inst = []
        for y in range(num_ins):
            inst.append(cls.create(**l[y]))

        return inst
