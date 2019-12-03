'''
程序：Sprite增强类，实现类似Scratch角色运动控制
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from math import sqrt, sin, cos, atan, radians, degrees
from random import randint

class SpritePlus(pyglet.sprite.Sprite):
    '''Sprite增强类'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
    def point(self, x, y):
        '''让角色面向指定的坐标'''
        #界限角，在坐标轴的角度
        if x == self.x:
            a = 0 if y > self.y else 180
        elif y == self.y:
            a = 90 if x > self.x else 270
        else:
            #象限角
            R = degrees(atan(abs(x - self.x) / abs(y - self.y)))
            #测量学上的方位角
            if x > self.x and y > self.y:
                a = R
            elif x > self.x and y < self.y:
                a = 180 - R
            elif x < self.x and y < self.y:
                a = 180 + R
            elif x < self.x and y > self.y:
                a = 360 - R
        
        #数学上的方位角
        self.rotation = a - 90

    def left(self, angle):
        '''左转一个角度'''
        self.rotation -= angle

    def right(self, angle):
        '''右转一个角度'''
        self.rotation += angle

    def move(self, distance):
        '''移动一个距离'''
        #将数学上的方位角换算为测量学上的方位角，即+90
        self.x += distance * sin(radians(self.rotation + 90))
        self.y += distance * cos(radians(self.rotation + 90))
        
    def touching(self, pos=(0, 0), distance=0):
        '''碰撞检测'''
        d = sqrt((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2)
        return d < distance
    
    def set_image_center(self, image):
        '''设置精灵的中心锚点'''
        if isinstance(image, pyglet.image.Animation):
            for frame in image.frames:
                frame.image.anchor_x = frame.image.width // 2
                frame.image.anchor_y = frame.image.height // 2
        elif isinstance(image, pyglet.image.AbstractImage):
            image.anchor_x = image.width / 2
            image.anchor_y = image.height / 2
            
    def set_sprite_center(self):
        '''设置精灵的中心锚点'''
        self.set_image_center(self.image)
        self.set_position(self.x, self.y)
