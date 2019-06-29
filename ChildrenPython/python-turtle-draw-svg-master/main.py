# -*- coding: utf-8 -*-
# Author: tfx2001
# License: GNU GPLv3
# Time: 2018-08-09 18:27

import turtle as te
from bs4 import BeautifulSoup
import argparse
import sys
import numpy as np
import cv2
import os
from win32.win32api import GetSystemMetrics

WriteStep = 15  # 贝塞尔函数的取样次数
Speed = 1000
Width = 600  # 界面宽度
Height = 600  # 界面高度
Xh = 0  # 记录前一个贝塞尔函数的手柄
Yh = 0
scale = (1, 1)
first = True
K = 32


def Bezier(p1, p2, t):  # 一阶贝塞尔函数
    return p1 * (1 - t) + p2 * t


def Bezier_2(x1, y1, x2, y2, x3, y3):  # 二阶贝塞尔函数
    te.goto(x1, y1)
    te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        te.goto(x, y)
    te.penup()


def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4):  # 三阶贝塞尔函数
    x1 = -Width / 2 + x1
    y1 = Height / 2 - y1
    x2 = -Width / 2 + x2
    y2 = Height / 2 - y2
    x3 = -Width / 2 + x3
    y3 = Height / 2 - y3
    x4 = -Width / 2 + x4
    y4 = Height / 2 - y4  # 坐标变换
    te.goto(x1, y1)
    te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        te.goto(x, y)
    te.penup()


def Moveto(x, y):  # 移动到svg坐标下（x，y）
    te.penup()
    te.goto(-Width / 2 + x, Height / 2 - y)
    te.pendown()


def Moveto_r(dx, dy):
    te.penup()
    te.goto(te.xcor() + dx, te.ycor() - dy)
    te.pendown()


def line(x1, y1, x2, y2):  # 连接svg坐标下两点
    te.penup()
    te.goto(-Width / 2 + x1, Height / 2 - y1)
    te.pendown()
    te.goto(-Width / 2 + x2, Height / 2 - y2)
    te.penup()


def Lineto_r(dx, dy):  # 连接当前点和相对坐标（dx，dy）的点
    te.pendown()
    te.goto(te.xcor() + dx, te.ycor() - dy)
    te.penup()


def Lineto(x, y):  # 连接当前点和svg坐标下（x，y）
    te.pendown()
    te.goto(-Width / 2 + x, Height / 2 - y)
    te.penup()


def Curveto(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到（x，y）
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, x1, y1, x2, y2, x, y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def Curveto_r(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到相对坐标（x，y）
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, X_now + x1, Y_now + y1,
             X_now + x2, Y_now + y2, X_now + x, Y_now + y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def transform(w_attr):
    funcs = w_attr.split(' ')
    for func in funcs:
        func_name = func[0: func.find('(')]
        if func_name == 'scale':
            global scale
            scale = (float(func[func.find('(') + 1: -1].split(',')[0]),
                     -float(func[func.find('(') + 1: -1].split(',')[1]))


def readPathAttrD(w_attr):
    ulist = w_attr.split(' ')
    for i in ulist:
        # print("now cmd:", i)
        if i.isdigit() or i.isalpha():
            yield float(i)
        elif i[0].isalpha():
            yield i[0]
            yield float(i[1:])
        elif i[-1].isalpha():
            yield float(i[0: -1])
        elif i[0] == '-':
            yield float(i)


def drawSVG(filename, w_color):
    global first
    SVGFile = open(filename, 'r')
    SVG = BeautifulSoup(SVGFile.read(), 'lxml')
    Height = float(SVG.svg.attrs['height'][0: -2])
    Width = float(SVG.svg.attrs['width'][0: -2])
    transform(SVG.g.attrs['transform'])
    if first:
        te.setup(height=Height, width=Width)
        te.setworldcoordinates(-Width / 2, 300, Width -
                               Width / 2, -Height + 300)
        first = False
    te.tracer(100)
    te.pensize(1)
    te.speed(Speed)
    te.penup()
    te.color(w_color)

    for i in SVG.find_all('path'):
        attr = i.attrs['d'].replace('\n', ' ')
        f = readPathAttrD(attr)
        lastI = ''
        for i in f:
            if i == 'M':
                te.end_fill()
                Moveto(next(f) * scale[0], next(f) * scale[1])
                te.begin_fill()
            elif i == 'm':
                te.end_fill()
                Moveto_r(next(f) * scale[0], next(f) * scale[1])
                te.begin_fill()
            elif i == 'C':
                Curveto(next(f) * scale[0], next(f) * scale[1],
                        next(f) * scale[0], next(f) * scale[1],
                        next(f) * scale[0], next(f) * scale[1])
                lastI = i
            elif i == 'c':
                Curveto_r(next(f) * scale[0], next(f) * scale[1],
                          next(f) * scale[0], next(f) * scale[1],
                          next(f) * scale[0], next(f) * scale[1])
                lastI = i
            elif i == 'L':
                Lineto(next(f) * scale[0], next(f) * scale[1])
            elif i == 'l':
                Lineto_r(next(f) * scale[0], next(f) * scale[1])
                lastI = i
            elif lastI == 'C':
                Curveto(i * scale[0], next(f) * scale[1],
                        next(f) * scale[0], next(f) * scale[1],
                        next(f) * scale[0], next(f) * scale[1])
            elif lastI == 'c':
                Curveto_r(i * scale[0], next(f) * scale[1],
                          next(f) * scale[0], next(f) * scale[1],
                          next(f) * scale[0], next(f) * scale[1])
            elif lastI == 'L':
                Lineto(i * scale[0], next(f) * scale[1])
            elif lastI == 'l':
                Lineto_r(i * scale[0], next(f) * scale[1])
    te.penup()
    te.hideturtle()
    te.update()
    SVGFile.close()


def drawBitmap(w_image):
    print('Reducing the colors...')
    Z = w_image.reshape((-1, 3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS, 10, 1.0)
    global K
    ret, label, center = cv2.kmeans(
        Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res = res.reshape(w_image.shape)
    no = 1
    for i in center:
        sys.stdout.write('\rDrawing: %.2f%% [' % (
            no / K * 100) + '#' * no + ' ' * (K - no) + ']')
        no += 1
        res2 = cv2.inRange(res, i, i)
        res2 = cv2.bitwise_not(res2)
        cv2.imwrite('.tmp.bmp', res2)
        os.system('potrace.exe .tmp.bmp -s --flat')
        # print(i)
        drawSVG('.tmp.svg', '#%02x%02x%02x' % (i[2], i[1], i[0]))
    os.remove('.tmp.bmp')
    os.remove('.tmp.svg')
    print('\n\rFinished, close the window to exit.')
    te.done()


if __name__ == '__main__':
    paser = argparse.ArgumentParser(
        description="Convert an bitmap to SVG and use turtle libray to draw it.")
    paser.add_argument('filename', type=str,
                       help='The file(*.jpg, *.png, *.bmp) name of the file you want to convert.')
    paser.add_argument(
        "-c", "--color", help="How many colors you want to draw.(If the number is too large that the program may be very slow.)", type=int, default=32)
    args = paser.parse_args()
    K = args.color
    try:
        bitmapFile = open(args.filename, mode='r')
    except FileNotFoundError:
        print(__file__ + ': error: The file is not exists.')
        quit()
    if os.path.splitext(args.filename)[1].lower() not in ['.jpg', '.bmp', '.png']:
        print(__file__ + ': error: The file is not a bitmap file.')
        quit()
    bitmap = cv2.imread(args.filename)
    if bitmap.shape[0] > GetSystemMetrics(1):
        bitmap = cv2.resize(bitmap, (int(bitmap.shape[1] * (
            (GetSystemMetrics(1) - 50) / bitmap.shape[0])), GetSystemMetrics(1) - 50))
    drawBitmap(bitmap)
