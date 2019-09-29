#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# include<opencv\highgui.hpp>
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
# opencv版本不同注意指令
fourcc = cv2.CAP_OPENCV_MJPEG

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
