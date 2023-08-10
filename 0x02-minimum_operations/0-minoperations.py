#!/usr/bin/env python3
"""A module that contains the minOperations function"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
