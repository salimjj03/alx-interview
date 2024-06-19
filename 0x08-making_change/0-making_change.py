#!/usr/bin/python3
"""
determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    count = 0
    value = total
    coins.sort(reverse=True)
    star_index = 0

    while 1:
        for i in coins:
            if value - i > 0:
                count += 1
                value -= i
                break
            elif value - i == 0:
                return count + 1
            elif count == len(coins) and coins[-1] == i and value - i < 0:
                return -1
            star_index += 1
