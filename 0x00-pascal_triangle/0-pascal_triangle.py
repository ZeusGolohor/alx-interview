#!/usr/bin/python3
"""
A script to print a pascal triangle.
"""


def pascal_triangle(n):
    """
    Method to print pascal trangle.
    """
    if n <= 0:
        return []

    triangle = []
    for row_n in range(n):
        row = [1] * (row_n + 1)
        if row_n >= 2:
            for i in range(1, row_n):
                row[i] = triangle[row_n - 1][i - 1] + triangle[row_n - 1][i]
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(entry) for entry in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
