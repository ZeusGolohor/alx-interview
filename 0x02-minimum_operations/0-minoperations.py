#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file.
"""


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file.
    """
    if not isinstance(n, int):
        return 0
    ops = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops += 2
        elif clipboard > 0:
            done += clipboard
            ops += 1
    return ops
