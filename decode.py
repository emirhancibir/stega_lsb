#!/usr/bin/env python3

import cv2
import numpy as np

def decode(img_path):

    # DEFINING LIST
    bin_data = []
    last_two_bits = []
    merged_data = []
    ascii_chars = []
    temp_bits = ''


    img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)
    shape = np.shape(img)
    
    data = np.reshape(img, -1)
    
    data = data.tolist()

    for num in data:
        data = format(num, '08b')
        bin_data.append(data)
    
    print("BINARY IMAGE DATA")
    print(np.array(bin_data))
    print("-"*30)
    
    # GETTING LAST TWO BITS FOR IMAGE BINARY
    for i in bin_data:
        last_two_bits.append(i[-2:])
    
    print("LAST TWO BITS")
    print(np.array(last_two_bits))
    print("-"*30)

    for bits in last_two_bits:
        temp_bits += bits
        if len(temp_bits) == 8 and temp_bits != '00000000':
            merged_data.append(temp_bits)
            temp_bits = ''
    
    print("MERGED DATA")
    print(np.array(merged_data))

    # GETTING ASCII VALUE
    for i in merged_data:
        dec_char = int(i, 2)
        ascii_chars.append(chr(dec_char))

    msg = ''.join(ascii_chars)
    print("-"*30)
    print("SECRET MESSAGE IS : {}".format(msg))
    

        

if __name__ == "__main__":
    decode("imgs/encoded.png")