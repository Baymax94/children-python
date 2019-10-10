#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img1 = cv2.imread(
    'F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/Baymax.jpg')
img2 = cv2.imread(
    'F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/opencv01.jpg')
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindow()

# 图像混合（权重）
# 还有问题，大小不一致，待修改
