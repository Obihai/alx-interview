#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    expected_continuation_bytes = 0

    for byte in data:
        # Check if the current byte is a continuation byte
        if byte & 0b11000000 == 0b10000000:
            expected_continuation_bytes -= 1
            if expected_continuation_bytes < 0:
                return False
        else:
            if byte & 0b10000000 == 0:  # One-byte character
                expected_continuation_bytes = 0
            elif byte & 0b11100000 == 0b11000000:  # Two-byte character
                expected_continuation_bytes = 1
            elif byte & 0b11110000 == 0b11100000:  # Three-byte character
                expected_continuation_bytes = 2
            elif byte & 0b11111000 == 0b11110000:  # Four-byte character
                expected_continuation_bytes = 3
            else:
                return False

    return expected_continuation_bytes == 0
