#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread(
    "F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/opencv01.jpg",0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
