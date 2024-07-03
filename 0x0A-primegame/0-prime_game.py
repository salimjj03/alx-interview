#!/usr/bin/python3
"""
prime game
"""


def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    prime game
    """

    Maria = 0
    Ben = 0

    for round in range(x):
        ls = [i for i in range(1, nums[round] + 1) if is_prime(i)]
        count = len(ls)
        if count == 0 or count % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria == Ben:
        return (None)
    return("Maria" if Maria > Ben else "Ben")
