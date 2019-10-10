#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread(
    "F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/Baymax.jpg")
b, g, r = cv2.split(img)
img = cv2.merge(b, g, r)

img[:, :, 2] = 0

# 拆分及合并图像通道
