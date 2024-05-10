#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file.
"""


def min_operations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file.
    """
    if n <= 1:
        return 0

    ops = 0
    div = 2

    while n > 1:
        if n % div == 0:
            n //= div
            ops += div
        else:
            div += 1

    return ops
