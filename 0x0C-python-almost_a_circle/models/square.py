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

    def update(self, *args, **kwargs):
        """assigns attributes to square class"""
        if len(args) > 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    super(Square, type(self)).width.fset(self, arg)
                    super(Square, type(self)).height.fset(self, arg)
                elif num == 2:
                    super(Square, type(self)).x.fset(self, arg)
                elif num == 3:
                    super(Square, type(self)).y.fset(self, arg)
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                super(Square, type(self)).width.fset(self, kwargs["size"])
                super(Square, type(self)).height.fset(self, kwargs["size"])
            if "x" in kwargs:
                super(Square, type(self)).x.fset(self, kwargs["x"])
            if "y" in kwargs:
                super(Square, type(self)).y.fset(self, kwargs["y"])

    def to_dictionary(self):
        """ar adding dictionary to the square class"""
        dic = self.__dict__
        attributes = ["id", "size", "x", "y"]
        rot = {x: getattr(self, x) for x in attributes }
        return rot
