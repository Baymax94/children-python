#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 画矩形
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# 画圆_圆心+半径
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
# 画椭圆_中心+长轴+短轴+旋转角度(0~360)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# 画多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))
# 写字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

winname = 'example'
cv2.namedWindow(winname)

cv2.imshow(winname, img)
k = cv2.waitKey(0)
if k == 27:   # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):   # wait for 's' key to save and exit
    cv2.imwrite(
        "E:/GitHub/children-python/Python_Books/OpenCV-Python-Tutoria/messigray.png", img)
    cv2.destroyAllWindows()
# OpenCV中的绘图函数
# https://segmentfault.com/a/1190000015585635
