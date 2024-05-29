#!/usr/bin/env python3

import cv2
import numpy as np

def read_image(img_path, debug=False):
    """
    Reads an image from the specified file path and returns the image data and the maximum number of bytes the image can occupy.

    Args:
        img_path (str): The file path of the image to be read.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.

    Returns:
        numpy.ndarray: The image data.
        int: The maximum number of bytes the image can occupy.
    """
    img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)
    shape = np.shape(img)
    
    if debug:
        print("shape[0] : {} shape[1] : {}".format(shape[0], shape[1]))
        print("-"*30)
    
    max_bytes = shape[0]*shape[1]
    
    return img, max_bytes

def convert_msg_to_binary(msg, debug=False):
    """
    Converts a given message string into a list of binary representations for each character.
    
    Args:
        msg (str): The message to be converted to binary.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.
    
    Returns:
        list[str]: A list of binary strings, where each string represents the binary
        value of a single character from the input message.
    """
    bin_msgs = []
    for char in msg:
        bin_msg = format(ord(char), '08b')
        bin_msgs.append(bin_msg)
    if debug:
        print("BIN MSG")
        print(bin_msgs)
        print("-"*30)
    return bin_msgs

def split_binary_msg(bin_msgs, debug=False):
    """
    Splits a list of binary messages into a list of 2-bit binary strings.
    
    Args:
        bin_msgs (list of str): A list of binary messages, where each message is a string of binary digits.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.
    
    Returns:
        list of int: A list of integers, where each integer represents a 2-bit binary string from the input messages.
    """
    msg_splitted_bits = []
    for bin_msg in bin_msgs:
        for i in range(0, len(bin_msg), 2):
            msg_splitted_bits.append(bin_msg[i:i+2])
    if debug:
        print("BIN MESSAGE SPLITTED")
        print(msg_splitted_bits)
        print("-"*30)
    msg_splitted_bits = [int(bit, 2) for bit in msg_splitted_bits]
    if debug:
        print("SPLITTED MSG DEC")
        print(msg_splitted_bits)
        print("-"*30)
    return msg_splitted_bits

def encode_message(img, msg_splitted_bits, debug=False):
    """
    Encodes a message into an image by modifying the least significant bits of the image data.
    
    Args:
        img (numpy.ndarray): The image data to be encoded.
        msg_splitted_bits (list): A list of binary bits representing the message to be encoded.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.
    
    Returns:
        None
    """
    data = np.reshape(img, -1)

    if debug:
        print("ORIGINAL DATA")
        print(data)
        print("-"*30)

    data = data.tolist()

    for i in range(len(data)):
        data[i] &= 0b11111100

    if debug:
        print(np.array(data))
    
    for i, bit in enumerate(msg_splitted_bits):
        data[i] |= bit
    
    data = np.array(data)
    
    if debug:
        print(data)
    
    data = np.reshape(data, (img.shape[0], img.shape[1], 3))
    cv2.imwrite("imgs/encoded.png", data)

def insert_msg(img_path, msg, debug=False):
    """
    Inserts a message into an image by encoding the message into the image's pixel data.
    
    Args:
        img_path (str): The file path to the image to be encoded.
        msg (str): The message to be encoded into the image.
        debug (bool, optional): If True, print intermediate steps. Defaults to False.
    
    Raises:
        None
    
    Returns:
        None
    """
    img, max_bytes = read_image(img_path, debug)
    if len(msg) > max_bytes:
        print("Message greater than capacity:{}".format(max_bytes))
        return
    bin_msgs = convert_msg_to_binary(msg, debug)
    msg_splitted_bits = split_binary_msg(bin_msgs, debug)
    encode_message(img, msg_splitted_bits, debug)
    print("INSERTION COMPLETED")


if __name__ == '__main__':
    img_path = "imgs/panda.png"
    msg = "313131 lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    debug = False  # Set to True to enable debug prints
    insert_msg(img_path, msg, debug)
