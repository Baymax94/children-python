from turtle import *
from math import cos, radians
from random import randint

def gencolors(n):
    colormode(255)
    for i in range(n):
        r = randint(1,255)
        g = randint(1,255)
        b = randint(1,255)
        colors.append((r, g, b))
        
def square(b, isfill=1):
    if isfill:
        color(colors[randint(0, len(colors)-1)])
        begin_fill()
        for i in range(4):
            fd(b)
            right(90)
        end_fill()
    else:
        for i in range(4):
            fd(b)
            right(90)

def draw(b):
    '''画勾股树'''
    if b >= 5:
        square(b)
        
        fd(b)
        left(70)
        draw(b * cos(radians(70)))
        square(b * cos(radians(70)))
        
        right(90)
        fd(b * cos(radians(70)))
        draw(b * cos(radians(20)))
        square(b * cos(radians(20)))
        
        right(90)
        fd(b * cos(radians(20)))
        right(70)
        fd(b)
        right(90)
        fd(b)
        right(90)
    
if __name__ == '__main__':
    colors = []
    gencolors(10000)
    speed(0)
    seth(90)
    up()
    goto(-250, -150)
    down()
    draw(100)
