#!/usr/bin/python3

def validUTF8(data):
    # Helper function to check if a number has its most significant bit set
    def is_most_significant_bit_set(num):
        return num & 0b10000000 != 0

    # Helper function to check if a number has the pattern 10xxxxxx
    def is_continuation_byte(num):
        return num & 0b11000000 == 0b10000000

    # Variable to keep track of the number of continuation bytes expected
    expected_continuation_bytes = 0

    for byte in data:
        # If we are expecting continuation bytes
        if expected_continuation_bytes > 0:
            # Check if the current byte is a continuation byte
            if is_continuation_byte(byte):
                expected_continuation_bytes -= 1
            else:
                return False
        else:
            # Check the number of bytes for the current character
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
