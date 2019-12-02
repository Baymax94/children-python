'''
程序：绘制勾股树
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *
from math import cos, radians

def square(b):
    '''画正方形'''
    for i in range(4):
        fd(b)
        right(90)

def draw(b):
    '''画勾股树'''
    if b < 50: return
    
    square(b)
        
    fd(b)
    left(30)
    draw(b * cos(radians(30)))
    square(b * cos(radians(30)))

    right(90)
    fd(b * cos(radians(30)))
    draw(b * cos(radians(60)))
    square(b * cos(radians(60)))
    
    right(90)
    fd(b * cos(radians(60)))
    right(30)
    fd(b)
    right(90)
    fd(b)
    right(90)
        
if __name__ == '__main__':
    speed(0)
    up()
    goto(50, -250)
    down()
    seth(90)
    draw(100)
