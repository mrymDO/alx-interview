#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """rotate 2D matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - layer - 1

        for i in range(first, last):
            offset = i - first

            top = matrix[first][i]

            matrix[first][i] = matrix[last - offset][first]

            matrix[last - offset][first] = matrix[last][last - offset]

            matrix[last][last - offset] = matrix[i][last]

            matrix[i][last] = top
