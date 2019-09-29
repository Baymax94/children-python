#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
img = cv2.imread(
    "E:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/baymax.png", 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:   # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):   # wait for 's' key to save and exit
    cv2.imwrite(
        "E:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/messigray.png", img)
    cv2.destroyAllWindows()
