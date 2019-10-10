#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread(
    "F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/Baymax.jpg")

px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)

'''修改像素值'''
img[100, 100] = [255, 255, 255]
print(img[100, 100])

'''获取像素值及修改'''
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))
