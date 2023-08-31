#!/usr/bin/python3
"""
A module
"""

import sys


def nqueens(n):
    solutions = []
    def nqueens_helper(queens, row):
        if row == n:
            solutions.append(queens)
            return
        
        for col in range(n):
            if is_valid(queens, row, col):
                nqueens_helper(queens + [[row, col]], row + 1)

    def is_valid(queens, row, col):
        for queen in queens:
            if queen[1] == col:
                return False
            
            if abs(queen[0] - row) == abs(queen[1] - col):
                return False
        return True

    nqueens_helper([], 0)
    return solutions


def main():
    """
    Entry point
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(N)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
