#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread(
    "F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/Baymax.jpg")
print(img.shape)    # 图像的形状：行数，列数，通道数
print(img.size)     # 图像的像素数
print(img.dtype)    # 图像的数据类型

# 获取图像属性：行，列，通道，图像数据类型，像素数数目等
