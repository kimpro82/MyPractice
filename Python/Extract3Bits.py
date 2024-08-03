"""
Extract 3-Bits Values
2024.08.04

This module provides functions for extracting 3-bit values from byte data,
converting those values to a list of bits, and then converting the bits back to bytes.

Functions:
- Extract3Bits(data)             : Extracts 3-bit values from the given byte data.
- Convert3BitValuesToBits(pixels): Converts 3-bit values to a list of bits.
- BitsToBytes(bits)              : Converts a list of bits to a list of bytes.
"""

def Extract3Bits(data):
    """
    Extracts 3-bit values from the given byte data.

    Args   :
        data (list of int): The byte data to extract 3-bit values from.

    Returns:
        list of int       : The extracted 3-bit values.
    """
    bits = []
    for byte in data:
        for i in range(8):
            bits.append((byte >> (7 - i)) & 1)  # Extract individual bits

    # Extract 3-bit values
    pixels = []
    for i in range(0, len(bits), 3):
        if i + 2 < len(bits):
            pixel_value = (bits[i] << 2) | (bits[i+1] << 1) | bits[i+2]
            pixels.append(pixel_value)
    return pixels

def Convert3BitValuesToBits(pixels):
    """
    Converts 3-bit values to a list of bits.

    Args   :
        pixels (list of int): The list of 3-bit values to convert.

    Returns:
        list of int         : The converted list of bits.
    """
    bits = []
    for pixel in pixels:
        bits.extend([(pixel >> 2) & 1, (pixel >> 1) & 1, pixel & 1])
    return bits

def BitsToBytes(bits):
    """
    Converts a list of bits to a list of bytes.

    Args   :
        bits (list of int): The list of bits to convert.

    Returns:
        list of int       : The converted list of bytes.
    """
    byte_list = []
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(bits):
                byte = (byte << 1) | bits[i + j]
        byte_list.append(byte)
    return byte_list

if __name__ == "__main__":
    # Test data
    data = [224, 84, 64]  # Example data

    # Extract 3-bit values
    pixels = Extract3Bits(data)
    print("Extracted 3-bit values:", pixels)

    # Convert 3-bit values to bit list
    bits = Convert3BitValuesToBits(pixels)

    # Convert bits to bytes
    byte_data = BitsToBytes(bits)
    print("Converted byte data   :", byte_data)
