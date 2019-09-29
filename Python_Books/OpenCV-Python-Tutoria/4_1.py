#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2

# load an color image in grayscale
# 不能出现中文路径，并且使用“/”
img = cv2.imread(
    "E:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/Baymax.jpg", 0)
# img = cv2.imread('Baymax.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 读入图像
# cv2.imread()
# 显示图像
# cv2.imshow()
