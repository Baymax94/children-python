#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread(
    "E:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/baymax.png", 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
# 利用Matplotib
# https://matplotlib.org/api/pyplot_api.html
