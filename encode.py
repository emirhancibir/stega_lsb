#!/usr/bin/env python3

import cv2
import numpy as np


def insert_msg(img_path, msg):

    # LIST DEF
    bin_msgs = []
    ori_bin_datas = []
    msg_splitted_bits = []

    # READING IMAGE
    img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)

    # GETTING SHAPE AND CALCULATE MAX BYTES
    shape = np.shape(img)
    max_bytes = shape[0]*shape[1]

    # THROW EXCEPT FOR CAPACITY
    if len(msg) > max_bytes:
        print("Message greater than capacity:{}".format(max_bytes))
    
    data = np.reshape(img, -1) # flatten data # [b g r b g r .......]
    print("ORIGINAL DATA")
    print(data)
    print("-"*30)

    # CONVERT NUMPY TO LIST
    data = data.tolist()

    # CONVERT TO BINARY MESSAGE
    for i in msg:
        # CONVERT TO BINARY MESSAGE (0bxxxxxxxx)
        bin_msg = format(ord(i),'08b')
        bin_msgs.append(bin_msg)

    # SPLIT MSG
    for i in bin_msgs:
        
        for j in range(0, len(i), 2):
            msg_splitted_bits.append(i[j:j+2])
        
    
    print("MESSAGE")
    print((msg_splitted_bits))
    print("-"*30)
    
    
    # CONVERT AGAIN DECIMAL 2 BIT SPLITTED MSG 
    msg_splitted_bits = [int(bit, 2) for bit in msg_splitted_bits]
    print(msg_splitted_bits)
    print("-"*30)
    for i, bit in enumerate(msg_splitted_bits):
        # CLEAN LAST TWO BITS
        data[i] &= 0b11111100

    for i, bit in enumerate(msg_splitted_bits):
        
        print("ori : ", data[i])
        data[i] |= bit
        print("changed : ",data[i])        

    data = np.array(data)
    data = np.reshape(data, (shape[0], shape[1], 3))
    cv2.imwrite("imgs/encoded_img.png", data)
    
        
if __name__ == '__main__':

    img_path = "imgs/man.jpeg"
    insert_msg(img_path, "zart")

# TODO: MUST BE ADD MESSAGE FINISH FLAG BECAUSE ITS NOT RECEIVING MESSAGE LENGTH
# TODO: SAVED FILE NAMES WILL BE DYNAMIC E.G. IMWRITE ....