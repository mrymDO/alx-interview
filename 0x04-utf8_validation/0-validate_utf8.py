#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """determines if a data set is a valid UTF-8 encoding"""
    num_consecutive_ones = 0

    for byte in data:
        if num_consecutive_ones == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                num_consecutive_ones = 1
            elif byte >> 4 == 0b1110:
                num_consecutive_ones = 2
            elif byte >> 3 == 0b11110:
                num_consecutive_ones = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_consecutive_ones -= 1
            if num_consecutive_ones < 0:
                return False

    return num_consecutive_ones == 0
