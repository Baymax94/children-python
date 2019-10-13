#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread(
    "F:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/opencv01.jpg")


'''
cap = cv2.VideoCapture(0)
while(1):
    # 获取每一帧
    ret, frame = cap.read()
    # 转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 设定蓝色的阈值
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 对原图像和掩模进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # 显示图像
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
# 关闭窗口
cv2.destroyAllWindows()
'''
'''
# 镜像
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]

dst = np.zeros([height*2, width, deep], np.uint8)

for i in range(height):
    for j in range(width):
        dst[i, j] = img[i, j]
        dst[height*2-i-1, j] = img[i, j]

for i in range(width):
    dst[height, i] = (0, 0, 255)
cv2.imshow('image', dst)
cv2.waitKey(0)
'''

# 平移
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

dst = np.zeros(imgInfo, np.uint8)

for i in range(height):
    for j in range(width - 100):
        dst[i, j + 100] = img[i, j]

cv2.imshow('image', dst)
cv2.waitKey(0)
