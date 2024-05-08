#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number
of operations needed to result in exactly n H
characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All
=> Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """
    In a text file, there is a single character H.Your text
    editor can execute only two operationsin this file:
    Copy All and Paste. Given a number n,write a method
    that calculates the fewest number
    of operations needed to result in exactly n H
    characters in the file.

        Prototype: def minOperations(n)
        Returns an integer
        If n is impossible to achieve, return 0

    Example:

    n = 9

    H => Copy All => Paste => HH => Paste =>HHH => Copy All
    => Paste => HHHHHH => Paste => HHHHHHHHH

    Number of operations: 6
    """

    file = 1
    operation = 0
    buf = 1

    while file < n:
        if n % file == 0:
            buf = file
            operation += 1
        file += buf
        operation += 1

    return operation if file == n else 0
