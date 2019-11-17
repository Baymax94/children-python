# import cv2 as cv    # opencv读取的格式是BGR
from cv2 import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np
'''
%matplotlib inline
'''
# notebook魔法指令，plt.show
img=cv.imread('OpenCV计算机视觉实战(Python版)/Picture/car.png')
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
