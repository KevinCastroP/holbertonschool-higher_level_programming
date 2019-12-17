#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for k in range(len(matrix)):
        for c in range(len(matrix[k])):
            print("{:d}".format(matrix[k][c]), end='')
            if c < len(matrix[k]) - 1:
                print("{}".format(' '), end='')
        print()
