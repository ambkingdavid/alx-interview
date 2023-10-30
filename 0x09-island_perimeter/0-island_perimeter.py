#!/usr/bin/python3

"""
Island Perimeter
"""


def island_perimeter(grid: list) -> int:
    """
    Island Perimeter
    Args:
        grid: List of ints
    Returns:
        The perimeter
    """
    perimeter = 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    for row in range(num_rows):
        for col in range(num_cols):
            # Check if the current cell is land
            if grid[row][col] == 1:
                # Check the top neighbor
                if row - 1 < 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check the bottom neighbor
                if row + 1 >= num_rows or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check the left neighbor
                if col - 1 < 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check the right neighbor
                if col + 1 >= num_cols or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
