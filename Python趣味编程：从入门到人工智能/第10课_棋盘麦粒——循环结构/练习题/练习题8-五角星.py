'''
程序：画循环五角星
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *
pensize(2)
seth(108)
for i in range(5):
    left(144)
    fd(100)
    right(72)
    fd(100)
