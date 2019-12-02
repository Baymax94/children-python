from turtle import *
from math import cos, radians
import random
def draw(a):
    '''画勾股树'''
    if a > 5:
        down()
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        color(r,g,b)
        begin_fill()
        for i in range(5):
            fd(a)
            right(90)
        end_fill()
        up()
        left(120)
        draw(a * cos(radians(30)))
        right(90)
        fd(a * cos(radians(30)))
        draw(a * cos(radians(60)))
        right(90)
        fd(a * cos(radians(60)))
        right(30)
        fd(a)
        right(90)
        fd(a)
        right(90)

if __name__ == '__main__':
    mode('logo')
    speed(0)
    colormode(255)
    seth(0)
    up()
    goto(50, -200)
    draw(100)
