#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divide a matrix"""
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error1 = "Each row of the matrix must have the same size"
    if not (isinstance(matrix, list)):
        raise TypeError(error1)
    len_list = len(matrix[0])
    for count1 in matrix:
        if len(count1) != len_list:
            raise TypeError(error2)
        for count2 in count1:
            if not (isinstance(count2, int) or isinstance(count2, float)):
                raise TypeError(error1)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    new_list = []
    for count1 in matrix:
        for count2 in count1:
            res = count2 / div
            new_list.append(round(res, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
