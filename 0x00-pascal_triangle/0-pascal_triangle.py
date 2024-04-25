#!/usr/bin/python3
""" This module returns a list of lists of integers
representing the Pascal’s triangle of n. """


def pascal_triangle(n):
    """ This module returns a list of lists of integers
    representing the Pascal’s triangle of n. """

    if n <= 0:
        return []
    ls = []
    for i in range(1, n + 1):
        ln = len(ls)
        new = []
        for j in range(ln + 1):
            if ln == 0:
                new.append(1)
            else:
                if j == 0:
                    new.append(1)
                elif j > 0 and j < ln:
                    new.append(ls[ln - 1][j - 1] + ls[ln - 1][j])
                elif j == ln:
                    new.append(1)
        ls.append(new)

    return (ls)
