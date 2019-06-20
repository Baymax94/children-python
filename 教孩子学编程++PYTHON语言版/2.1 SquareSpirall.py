# SquareSpirall.py - Draws a square spiral
import turtle
# Turtle最早来自于LOGO语言，是专门用于小孩子学习编程的，通过编程模拟一只turtle（海龟）在画板上爬行绘制图案，后来很多高级语言都移植了海龟绘图，python从2.6之后也将turtle库加入了其内部库中。
# 由于是内部库，使用import turtle语句就能引入turtle库，绘图主要有以下几个步骤：设置画板、设置画笔、控制海龟移动绘制图形、色彩填充，下图的代码就是个简单的示例。
t = turtle.Pen()
for x in range(100):
    t.forward(x*2)
    #修改括号内尺寸
    t.left(60)
    #修改括号内角度