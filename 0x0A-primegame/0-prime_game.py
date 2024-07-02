#!/usr/bin/python3
"""
prime game
"""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    prime game
    """

    Maria = 0
    Ben = 0
    count = 0

    for round in range(x):
        ls = [i for i in range(1, nums[round] + 1)]
        for num in ls:
            if is_prime(num):
                count += 1
        if count == 0 or count % 2 == 0:
            Ben += 1
        else:
            Maria += 1
        count = 0
    if Maria == Ben:
        return (None)
    return("Maria" if Maria > Ben else "Ben")
