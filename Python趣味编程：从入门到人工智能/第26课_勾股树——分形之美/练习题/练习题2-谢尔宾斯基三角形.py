'''
程序：谢尔宾斯基三角形
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *
def draw_triangle(b):
    if b < 10: return
    for i in range(3):
        draw_triangle(b/2)
        left(120)
        fd(b)       

if __name__ == '__main__':
    speed(0)
    pensize(1)
    draw_triangle(300)
    ht()
