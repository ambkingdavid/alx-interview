#!/usr/bin/python3

"""Making change"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """

    Args:
        coins: list of coins
        total: Amount to be met
    Returns:
        Fewest Number
    """
    if total <= 0:
        return 0
    """Sort the coins in descending order"""
    sorted_coins = sorted(coins, reverse=True)
    total_coins_used = 0
    """Loop through the sorted coins"""
    for coin in sorted_coins:
        """while the total is greater or equals to the current coin"""
        while total >= coin:
            """Subtract the current coin from the total"""
            total -= coin
            """Increment the total coins used by 1"""
            total_coins_used += 1
    """if the total == 0 that means the subtraction was successful"""
    if total == 0:
        """return the total coins used"""
        return total_coins_used
    return -1
