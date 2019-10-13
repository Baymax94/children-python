#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(
    "F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/opencv01.jpg")

rows, cols, ch = img.shape

'''
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
plt.subplot(121, plt.imshow(img), plt.title('Input'))
plt.subplot(121, plt.imshow(img), plt.title('Output'))
plt.show()
'''

cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]
# src 3 -> dst 3 (左上角, 左下角,右上角)
matSrc = np.float32([[0, 0], [0, height-1], [width-1, 0]]
                    )  # 需要注意的是 行列 和 坐标 是不一致的
matDst = np.float32([[50, 50], [100, height-50], [width-200, 100]])

matAffine = cv2.getAffineTransform(matSrc, matDst)  # mat 1 src 2 dst 形成组合矩阵
dst = cv2.warpAffine(img, matAffine, (height, width))
cv2.imshow('image', dst)
cv2.waitKey(0)

# 仿射变换
