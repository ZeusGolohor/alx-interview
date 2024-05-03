#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    a method that determines if all the boxes can be opened.
    """
    opened = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        opened.add(current_box)
        for key in boxes[current_box]:
            if key not in opened:
                queue.append(key)

    return len(opened) == len(boxes)
