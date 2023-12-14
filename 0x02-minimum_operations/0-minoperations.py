#!/usr/bin/python3
"""number of oprations to copy H n times"""


def minOperations(n):
    """min operation"""
    if n <= 1:
        return 0

    operations = 0
    current_chars = 1
    copied_chars = 0

    while current_chars < n:
        if n % current_chars == 0:
            copied_chars = current_chars
            operations += 2
            current_chars *= 2
        else:
            current_chars += copied_chars
            operations += 1

    return operations
