#!/usr/bin/python3
""" Island perimeter
"""


def island_perimeter(grid):
    """ Island perimeter
    """
    perimeter = 0

    if not grid or not grid[0]:
        return perimeter

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
