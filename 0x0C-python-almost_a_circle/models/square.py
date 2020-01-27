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

    def __str__(self):
        """string representation of square"""
        my_id = self.id
        x = super().x
        y = super().y
        w = super().width
        return "[Square] ({}) {}/{} - {}".format(my_id, x, y, w)

    @property
    def size(self):
        """size getter"""
        return super().width

    @size.setter
    def size(self, size):
        """size setter"""
        super(Square, type(self)).width.fset(self, size)
        super(Square, type(self)).height.fset(self, size)
