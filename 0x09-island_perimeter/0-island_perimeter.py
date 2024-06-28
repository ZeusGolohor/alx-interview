#!/usr/bin/env python3
"""
A script that returns the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    A method to that returns the perimeter of the island described in grid.
    """
    land_grid = grid
    num_rows, num_cols = len(land_grid), len(land_grid[0])
    total_perimeter = 0

    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if land_grid[row_index][col_index] == 1:
                total_perimeter += 4
                if row_index > 0 and land_grid[row_index - 1][col_index] == 1:
                    total_perimeter -= 2
                if col_index > 0 and land_grid[row_index][col_index - 1] == 1:
                    total_perimeter -= 2
    return total_perimeter
