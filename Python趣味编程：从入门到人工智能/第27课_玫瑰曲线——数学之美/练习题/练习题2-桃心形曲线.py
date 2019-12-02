'''
程序：绘制桃心形曲线
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *
from math import *
pensize(3)
fillcolor('Purple')
up()
a, t = 10, 0
begin_fill()
while t <= 2 * pi:
    x = a * 15 * sin(t) ** 3
    y = a * (15 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))
    goto(x, y)
    down()
    t = t + 0.01
end_fill()
ht()
