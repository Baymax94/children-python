#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread(
    "F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/Baymax.jpg")
# ball = img[280:340, 330:390]
ball = img[500:560, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 图像ROI
