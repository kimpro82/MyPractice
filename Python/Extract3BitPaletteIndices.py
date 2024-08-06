"""
Extract 3-Bit Palette Indices
2024.08.04

This module provides functions for extracting 3-bit palette indices from byte data
and converting those values to a list of bits.

Functions:
- extract_3_bit_palette_indices(data): Extracts 3-bit palette indices from the given byte data.
"""

IS_TEST = True

def extract_3_bit_palette_indices(data):
    """
    Extracts 3-bit palette indices from the given byte data.

    Args:
        data (list of int): The byte data to extract 3-bit palette indices from.

    Returns:
        list of int: The extracted 3-bit palette indices.
    """
    bit_list = []
    for index, byte in enumerate(data):
        for bit_position in range(8):
            bit = (byte >> (7 - bit_position)) & 1
            bit_list.append(bit)  # Extract individual bits
        if IS_TEST:
            print(f"data[{index}] : {byte:3d} {bin(byte):10s} {bit_list[-8:]}")

    # Extract 3-bit palette indices
    palette_indices = []
    for index in range(0, len(bit_list), 3):
        if index + 2 < len(bit_list):
            palette_index = (bit_list[index] << 2) | (bit_list[index + 1] << 1) | bit_list[index + 2]
            if IS_TEST:
                print(f"palette_index[{int(index/3)}] : {bit_list[index:index+3]} {bin(palette_index):5s} {palette_index}")
            palette_indices.append(palette_index)
    return palette_indices

if __name__ == "__main__":
    # Test data
    test_data = [224, 84, 64]

    # Extract 3-bit palette indices
    extracted_palette_indices = extract_3_bit_palette_indices(test_data)
    print("Extracted 3-bit palette indices:", extracted_palette_indices)
