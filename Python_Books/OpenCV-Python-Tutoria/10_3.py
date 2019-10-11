#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img1 = cv2.imread(
    'E:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/Baymax.jpg')
img2 = cv2.imread(
    'E:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/opencv03.jpg')

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
# 取roi中与mask中不为零的值对应的像素的值，其他值为0
# 注意这里必须有mask=mask或者mask=mask_inv, 其中的mask= 不能忽略
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)

# 取roi中与mask_inv中不为零的值对应的像素的值，其他值为0。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 按位运算
