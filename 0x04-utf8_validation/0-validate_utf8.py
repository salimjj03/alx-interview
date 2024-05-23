#!/usr/bin/python3
"""
method that determines if a given data set represents a valid
UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer

"""


def validUTF8(data):
    """
    method that determines if a given data set represents a valid
    UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer

    """
    bytes_num = 0

    first_mask = 1 << 7
    second_mask = 1 << 6

    for i in data:
        byte = 1 << 7

        if bytes_num == 0:
            while byte & i:
                bytes_num += 1
                byte = byte >> 1

            if bytes_num == 0:
                continue

            if bytes_num == 1 or bytes_num >= 5:
                return False
        else:
            if not (i & first_mask and not (i & second_mask)):
                return False
        bytes_num -= 1

    if bytes_num == 0:
        return True

    return False
