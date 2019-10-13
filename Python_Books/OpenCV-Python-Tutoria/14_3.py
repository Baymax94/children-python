#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread(
    "F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/opencv01.jpg")

# rows, cols = img.shape
imgInfo = img.shape
rows = imgInfo[0]
cols = imgInfo[1]
deep = imgInfo[2]

# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)
# 第三个参数是􄥂出图像的尺寸中心
dst = cv2.warpAffine(img, M, (2*cols, 2*rows))
while(1):
    cv2.imshow('img', dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
