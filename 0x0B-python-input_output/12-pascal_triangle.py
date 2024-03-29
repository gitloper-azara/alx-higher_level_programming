#!/usr/bin/python3
"""PASCAL_TRIANGLE MODULE
"""


def pascal_triangle(n):
    """generate pascal's triangle up to the specified level n

    Args:
        n (int): the level of Pascal's triangle
    Returns:"
        a list of lists representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
