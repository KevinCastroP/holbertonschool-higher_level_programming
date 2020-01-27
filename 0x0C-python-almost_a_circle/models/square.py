#!/usr/bin/python3
"""
creating a class square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """And now, the Square!"""
    def __init__(self, size, x=0, y=0, id=None):
        """creator"""
        super().__init__(size, size, x, y, id)
