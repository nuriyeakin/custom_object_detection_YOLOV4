# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import os
from glob import glob

png = glob("E:\YOLO\custom_yolo_model\spot_data\spot_images\*.jpeg")

for j in png:
    print(j)
    img = cv2.imread(j)
    cv2.imwrite(j[:-4]+"jpg",img)
    os.remove(j)