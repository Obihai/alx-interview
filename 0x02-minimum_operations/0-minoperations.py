#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    Finds the minimum number of operations required to
    transform a positive integer `n` into 1.

    Parameters:
    - n (int): The positive integer to be transformed.

    Returns:
    - int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    return operations
