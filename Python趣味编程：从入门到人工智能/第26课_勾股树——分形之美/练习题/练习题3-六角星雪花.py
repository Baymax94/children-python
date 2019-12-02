'''
程序：绘制六角星雪花分形图
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *

def draw_snowflake(b):
    if b < 4: return
    down()
    for i in range(6):
        draw_snowflake(b/3)
        fd(b)
        left(60)
        fd(b)
        right(120)
    up()

if __name__ == '__main__':
    speed(0)
    pensize(2)
    draw_snowflake(100)
    ht()
