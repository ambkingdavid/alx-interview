#!/usr/bin/python3
"""
A module
"""


def validUTF8(data):
    """
    UTF8 validator method
    """
    # Initialize a variable to keep track of the number
    # of bytes left in the current character
    bytes_left = 0

    # Iterate through the list of integers
    for num in data:
        # Check if this is the start of a new character
        if bytes_left == 0:
            # Count the number of leading 1s in the binary representation
            mask = 1 << 7
            while num & mask:
                bytes_left += 1
                mask >>= 1

            # Check if it's a valid start byte (1 to 4 bytes allowed)
            if bytes_left == 0:
                continue  # This is a single-byte character

            # If it's an invalid start byte or too long, return False
            if bytes_left == 1 or bytes_left > 4:
                return False
        else:
            # Check if this byte is a continuation byte (starts with '10')
            if (num >> 6) != 0b10:
                return False

        # Reduce the count of bytes left in the current character
        bytes_left -= 1

    # After processing all bytes, if there are no
    # incomplete characters, it's valid
    return bytes_left == 0
