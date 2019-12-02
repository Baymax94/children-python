'''
程序：绘制玫瑰曲线
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *
from math import *

def draw(a, n, end):
    '''绘制玫瑰曲线'''
    t = 0
    while t <= end:
        x = a * sin(n * t) * cos(t)
        y = a * sin(n * t) * sin(t)
        goto(x, y)
        t = t + 0.01

if __name__ == '__main__':
    '''三叶玫瑰'''
    draw(100, 3, 3.14)
    '''五叶玫瑰'''
    #draw(100, 1.5, 12.56)
