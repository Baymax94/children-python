'''
程序：画太极图，不填充
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *
pensize(2)
circle(100, steps=96)
circle(50, 180)
circle(-50, 180)
right(90)
up()
fd(50)
seth(0)
fd(25)
seth(90)
down()
circle(20, steps=48)
up()
home()
seth(90)
fd(50)
left(90)
fd(25)
left(90)
down()
circle(20, steps=48)
ht()
