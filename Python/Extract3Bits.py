"""
Extract 3-Bit Values
2024.08.04

This module provides functions for extracting 3-bit values from byte data,
converting those values to a list of bits, and then converting the bits back to bytes.

Functions:
- extract_3_bit_values(data)          : Extracts 3-bit values from the given byte data.
- convert_3_bit_values_to_bits(pixels): Converts 3-bit values to a list of bits.
- bits_to_bytes(bits)                 : Converts a list of bits to a list of bytes.
"""

def extract_3_bit_values(data):
    """
    Extracts 3-bit values from the given byte data.

    Args:
        data (list of int): The byte data to extract 3-bit values from.

    Returns:
        list of int: The extracted 3-bit values.
    """
    bit_list = []
    for byte in data:
        for bit_position in range(8):
            bit_list.append((byte >> (7 - bit_position)) & 1)  # Extract individual bits

    # Extract 3-bit values
    pixel_list = []
    for index in range(0, len(bit_list), 3):
        if index + 2 < len(bit_list):
            pixel_value = (bit_list[index] << 2) | (bit_list[index + 1] << 1) | bit_list[index + 2]
            pixel_list.append(pixel_value)
    return pixel_list

def convert_3_bit_values_to_bits(pixels):
    """
    Converts 3-bit values to a list of bits.

    Args:
        pixels (list of int): The list of 3-bit values to convert.

    Returns:
        list of int: The converted list of bits.
    """
    bit_list = []
    for pixel in pixels:
        bit_list.extend([(pixel >> 2) & 1, (pixel >> 1) & 1, pixel & 1])
    return bit_list

def bits_to_bytes(bits):
    """
    Converts a list of bits to a list of bytes.

    Args:
        bits (list of int): The list of bits to convert.

    Returns:
        list of int: The converted list of bytes.
    """
    byte_list = []
    for index in range(0, len(bits), 8):
        byte = 0
        for bit_position in range(8):
            if index + bit_position < len(bits):
                byte = (byte << 1) | bits[index + bit_position]
        byte_list.append(byte)
    return byte_list

if __name__ == "__main__":
    # Test data
    test_data = [224, 84, 64]  # Example data

    # Extract 3-bit values
    extracted_pixels = extract_3_bit_values(test_data)
    print("Extracted 3-bit values:", extracted_pixels)

    # Convert 3-bit values to bit list
    extracted_bits = convert_3_bit_values_to_bits(extracted_pixels)

    # Convert bits to bytes
    converted_byte_data = bits_to_bytes(extracted_bits)
    print("Converted byte data:", converted_byte_data)
