#!/usr/bin/python3
""" Rotate 2D matrix by 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """ Rotate 2D matrix by 90 degrees clockwise"""

    copy = matrix[:]
    m_len = range(len(matrix))

    for i in m_len:
        col = [row[i] for row in copy]
        matrix[i] = col[::-1]
