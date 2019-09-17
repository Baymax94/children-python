# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle
t = turtle.Pen()
t.pensize(5)        # 画笔宽度为5
t.left(90)          # 左转90度
t.begin_poly()      # 开始记录顶点
t.fd(200)           # 前进200
t.right(90)         # 右转90
t.circle(20)        # 画圆
t.end_poly()        # 结束记录顶点
p = t.get_poly()    # 获取顶点元组

screen = turtle.getscreen()
screen.addshape("db", p)
screen.mode("logo")
screen.delay(2)
t.shape("db")
t.clear()
t.seth(90)
t.color("blue")
angle = 0

while True:
    t.right(angle)
    if t.heading() > 180:
        angle = angle - 0.1
    else:
        angle = angle + 0.1

# 单摆模拟.py
# 本程序使用海龟画图来模拟一个单摆
