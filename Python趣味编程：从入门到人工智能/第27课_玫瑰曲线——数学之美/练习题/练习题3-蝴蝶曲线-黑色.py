'''
程序：绘制蝴蝶曲线(黑色)
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *
from math import *
pensize(2)
up()
a, t = 60, 0
while t <= 24 * pi:
    p = e ** cos(t) - 2 * cos(4*t) + sin(t/12) ** 5
    x = a * sin(t) * p
    y = a * cos(t) * p
    goto(x, y)
    down()
    t = t + 0.01
ht()
