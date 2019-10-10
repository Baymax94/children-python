#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread(
    "F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/Baymax.jpg")
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))
print(x+y)

# 图像加法
'''
可以使用函数cv2.add()将两幅图像进行加法运算，当然也可以直接使用numpy，res=img1+img。两幅图像的大小，类型必须一致，或者第二个图像可以使一个简单的标量值
'''
