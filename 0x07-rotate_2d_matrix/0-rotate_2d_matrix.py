#!/usr/bin/python3
"""
A script to solve 2d matrix.
"""


def rotate_2d_matrix(matrix):
    """
    A script to solve 2d matrix.
    """
    num = len(matrix)
    for y in range(num):
        for x in range(y):
            t = matrix[y][x]
            matrix[y][x] = matrix[x][y]
            matrix[x][y] = t
    for y in range(num):
        for x in range(int(num / 2)):
            t = matrix[y][x]
            matrix[y][x] = matrix[y][num-1-x]
            matrix[y][num-1-x] = t
