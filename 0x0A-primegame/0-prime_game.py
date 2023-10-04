#!/usr/bin/python3
"""
prime game module
"""


def isWinner(x, nums):
    """
    a function that determines the winner of a prime game
    """
    def is_prime(num):
        """
        checks if a number is prime
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def primeNumbers(n):
        """
        gets the prime numbers in a list of consecutive numbers

        returns the length of the list
        """
        primeList = []

        for num in n:
            if is_prime(num):
                primeList.append(num)
        return len(primeList)

    def is_even(n):
        """
        checks if a number is odd
        """
        if n % 2 == 0:
            return True
        return False

    maria = 0
    ben = 0

    if not len(nums):
        return None

    for round in range(x):
        roundList = [num for num in range(1, nums[round] + 1)]
        if nums[round] == 1:
            ben += 1
        elif is_even(primeNumbers(roundList)):
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    return None
