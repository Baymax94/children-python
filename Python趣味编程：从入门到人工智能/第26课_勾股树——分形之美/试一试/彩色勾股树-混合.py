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
    
def draw2(b):
    '''画勾股树'''
    square(b)
    
    fd(b)
    left(30)
    square(b * cos(radians(30)))
    
    right(90)
    fd(b * cos(radians(30)))
    square(b * cos(radians(60)))

    right(90)
    fd(b * cos(radians(60)))
    right(30)
    fd(b)
    right(90)
    fd(b)
    right(90)


def tree(b):
    if b >= 5:
        i = randint(1, 5)
        print(i)
        if i == 1:
            draw_10(b)
        elif i == 2:
            draw_30(b)
        elif i == 3:
            draw_45(b)
        elif i == 4:
            draw_60(b)
        elif i == 5:
            draw_80(b)
            
        
def draw_60(b):
    '''画勾股树'''
    square(b)

    fd(b)
    left(60)
    tree(b * cos(radians(60)))
    square(b * cos(radians(60)))

    right(90)
    fd(b * cos(radians(60)))
    tree(b * cos(radians(30)))
    square(b * cos(radians(30)))

    right(90)
    fd(b * cos(radians(30)))
    right(60)
    fd(b)
    right(90)
    fd(b)
    right(90)

def draw_30(b):
    '''画勾股树'''
    square(b)

    fd(b)
    left(30)
    tree(b * cos(radians(30)))
    square(b * cos(radians(30)))

    right(90)
    fd(b * cos(radians(30)))
    tree(b * cos(radians(60)))
    square(b * cos(radians(60)))

    right(90)
    fd(b * cos(radians(60)))
    right(30)
    fd(b)
    right(90)
    fd(b)
    right(90)
    
def draw_10(b):
    '''画勾股树'''
    square(b)

    fd(b)
    left(10)
    tree(b * cos(radians(10)))
    square(b * cos(radians(10)))

    right(90)
    fd(b * cos(radians(10)))
    tree(b * cos(radians(80)))
    square(b * cos(radians(80)))

    right(90)
    fd(b * cos(radians(80)))
    right(10)
    fd(b)
    right(90)
    fd(b)
    right(90)

def draw_80(b):
    '''画勾股树'''
    square(b)

    fd(b)
    left(80)
    tree(b * cos(radians(80)))
    square(b * cos(radians(80)))

    right(90)
    fd(b * cos(radians(80)))
    tree(b * cos(radians(10)))
    square(b * cos(radians(10)))

    right(90)
    fd(b * cos(radians(10)))
    right(80)
    fd(b)
    right(90)
    fd(b)
    right(90)
        
def draw_45(b):
    '''画勾股树'''
    square(b)

    fd(b)
    left(45)
    tree(b * cos(radians(45)))
    square(b * cos(radians(45)))

    right(90)
    fd(b * cos(radians(45)))
    tree(b * cos(radians(45)))
    square(b * cos(radians(45)))

    right(90)
    fd(b * cos(radians(45)))
    right(45)
    fd(b)
    right(90)
    fd(b)
    right(90)
        
if __name__ == '__main__':
    colors = []
    gencolors(10000)
    hideturtle()
    speed(0)
    seth(90)
    up()
    goto(-100, -250)
    down()
    tree(60)
