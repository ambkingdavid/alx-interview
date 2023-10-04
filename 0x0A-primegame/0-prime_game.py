#!/usr/bin/python3
"""
prime game module
"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = False

        for i in range(2, n + 1):
            dp[i] = not all(dp[i - p] for p in primes if p <= i)

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
