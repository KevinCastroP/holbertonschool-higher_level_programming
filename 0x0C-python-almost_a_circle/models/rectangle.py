#!/usr/bin/python3
"""
first class Rectangle
"""
from models.base import Base
import json


class Rectangle(Base):
    """first rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
