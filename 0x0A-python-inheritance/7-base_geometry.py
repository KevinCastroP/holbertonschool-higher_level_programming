#!/usr/bin/python3
"""
Integer validator
a cass with public instances area
and integer validator
"""


class BaseGeometry:
    """base geo class"""
    def area(self):
        """area function raises area not implemeted"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validate value"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
