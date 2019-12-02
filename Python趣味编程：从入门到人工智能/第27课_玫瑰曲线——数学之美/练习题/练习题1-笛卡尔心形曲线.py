'''
程序：绘制笛卡尔心形曲线
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *
from math import *
pensize(3)
fillcolor('red')
up()
a, t = 100, 0
begin_fill()
while t <= 2 * pi:
    x = a * (1 - sin(t)) * cos(t)
    y = a * (1 - sin(t)) * sin(t)
    goto(x, y)
    down()
    t = t + 0.01
end_fill()
ht()
