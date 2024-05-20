#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics.
"""
import sys


def parse_log():
    """
    Write a script that reads stdin line by line and computes metrics.
    """
    li = 0
    lines = {}
    file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    try:
        for line in sys.stdin:
            li += 1
            lines[li] = line.split(" ")
            file_size += int(lines[li][-1])
            status_codes[int(lines[li][-2])] += 1
            if li == 10:
                li = 0
                print("File size: {}".format(file_size))
                for key, value in status_codes.items():
                    print("{}: {}".format(key, value))
    except KeyboardInterrupt as e:
        print("File size: {}".format(file_size))
        for key, value in status_codes.items():
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    parse_log()
