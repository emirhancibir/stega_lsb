#!/usr/bin/env python3

import cv2
import numpy as np

def decode(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)
    shape = np.shape(img)
    
    data = np.reshape(img, -1)
    data = data.tolist()

        






if __name__ == "__main__":
    decode("/home/emir/Stegonagraphy/steganography/encoded_img.png")