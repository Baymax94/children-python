#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle
# 画布背景颜色
# turtle.bgcolor("black")
t = turtle.Pen()
colors = ["red", "blue", "green", "yellow"]
t.speed(0)
# 边数
sides = 6
for x in range(100):
    t.pencolor(colors[x % 4])
    t.forward(x)
    # t.left(360/sides + 1)
    t.left(360/sides)
    # 画笔宽度
    t.width(x*sides/100)

# SquareSpiral1
