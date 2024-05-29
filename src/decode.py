#!/usr/bin/env python3


import cv2
import numpy as np

def read_image(img_path, debug=False):
    """
    Reads an image from the given path and returns the image data.

    Args:
        img_path (str): The path to the image file.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.

    Returns:
        numpy.ndarray: The image data as a NumPy array.
    """
    img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)
    return img

def get_binary_data(img, debug=False):
    """
    Converts the image data to a list of binary strings.

    Args:
        img (numpy.ndarray): The image data as a NumPy array.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.

    Returns:
        list: A list of binary strings representing the image data.
    """
    bin_data = []
    data = np.reshape(img, -1).tolist()

    for num in data:
        data = format(num, '08b')
        bin_data.append(data)

    if debug:
        print("Binary data:")
        print(np.array(bin_data))
        print("-" * 30)

    return bin_data

def get_last_two_bits(bin_data, debug=False):
    """
    Extracts the last two bits from each binary string in the input list.

    Args:
        bin_data (list): A list of binary strings.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.

    Returns:
        list: A list of the last two bits from each binary string.
    """
    
    last_two_bits = [i[-2:] for i in bin_data]

    if debug:
        print("Last two bits:")
        print(np.array(last_two_bits))
        print("-" * 30)

    return last_two_bits

def merge_bits(last_two_bits, debug=False):
    """
    Merges the last two bits from each binary string into 8-bit chunks.

    Args:
        last_two_bits (list): A list of the last two bits from each binary string.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.

    Returns:
        list: A list of 8-bit binary strings representing the merged data.
    """
    merged_data = []
    temp_bits = ''

    for bits in last_two_bits:
        temp_bits += bits
        if len(temp_bits) == 8 and temp_bits != '00000000':
            merged_data.append(temp_bits)
            temp_bits = ''

    if debug:
        print("Merged data:")
        print(np.array(merged_data))
        print("-" * 30)

    return merged_data

def decode_message(merged_data, debug=False):
    """
    Decodes the merged data into ASCII characters and returns the secret message.

    Args:
        merged_data (list): A list of 8-bit binary strings representing the merged data.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.

    Returns:
        str: The secret message decoded from the merged data.
    """
    ascii_chars = []

    for i in merged_data:
        dec_char = int(i, 2)
        ascii_chars.append(chr(dec_char))

    msg = ''.join(ascii_chars)

    if debug:
        print("Secret message:")
        print(msg)
        print("-" * 30)

    return msg

def decode(img_path, debug=False):
    """
    Decodes the secret message from the given image file.

    Args:
        img_path (str): The path to the image file.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.

    Returns:
        str: The secret message decoded from the image.
    """
    img = read_image(img_path)
    bin_data = get_binary_data(img, debug)
    last_two_bits = get_last_two_bits(bin_data, debug)
    merged_data = merge_bits(last_two_bits, debug)
    msg = decode_message(merged_data, debug)
    return msg

if __name__ == "__main__":
    debug = False  # Set to True to enable debug prints
    secret_message = decode("../imgs/encoded.png", debug)
    print("-" * 30)
    print("SECRET MESSAGE IS : {}".format(secret_message))
