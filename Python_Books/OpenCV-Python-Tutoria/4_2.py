#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img = cv2.imread(
    "E:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/baymax.png", 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite(
    'E:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/messigrary.png', img)
cv2.destroyAllWindows()

# 保存图像
