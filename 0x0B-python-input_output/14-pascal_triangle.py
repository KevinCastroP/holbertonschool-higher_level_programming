#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """pascal triangle function"""
    if n <= 0:
        return []
    triangle = [[1]]
    last = triangle[0]
    for row in range(n - 1):
        new = [1]
        for col in range(row + 1):
            if col >= row:
                new.append(1)
            else:
                val = last[col] + last[col + 1]
                new.append(val)
        triangle.append(new)
        last = new
    return triangle
