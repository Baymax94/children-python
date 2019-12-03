'''
程序：下落物体类v4
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from random import randint
from math import sqrt
from game_res import *

class FallingObject(pyglet.sprite.Sprite):
    '''下落物体类'''
    def __init__(self):
        '''初始化'''
        super().__init__(snowflake_img)
        #类型：1-雪花，2-礼物，3-剪刀
        self.type = 1
        self.change()

    def change(self):
        #随机切换掉落物体的造型
        n = randint(1, 10)
        if 1 <= n <= 5:
            self.type = 1
            self.image = snowflake_img
        elif 6 <= n <= 8:
            self.type = 2
            self.image = gift_img
        else:
            self.type = 3
            self.image = clipper_img
        #将物体定位到窗口上方随机位置
        self.x, self.y = randint(100, 700), 900    

    def touching(self, pos=(0, 0), distance=0):
        '''碰撞检测'''
        d = sqrt((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2)
        return d < distance
