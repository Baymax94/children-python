'''
程序：捕鱼达人的各个精灵
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from pyglet.image import Animation
from random import randint
from time import time
from sprite_plus import SpritePlus
from game_res import *

class FishSprite(SpritePlus):
    '''鱼精灵'''
    def __init__(self, name = '', item = {}):
        self.set_animation(item)
        super().__init__(img = self.alive_img)
        self.name = name
        self.life = item['life']
        self.score = item['score']
        self.is_turn = item['turn']
        self.is_capture = False
        self.visible = True
        self.death_time = 0
        self.change_time = time()
        self.angle = 0
        self.speed = item['speed']
        self.acc = 0
        #让鱼开始游动
        self.set_start()

    def set_animation(self, item = {}):
        '''设置动画'''
        image = pyglet.resource.image(item['file'])
        img_seq = pyglet.image.ImageGrid(image, item['rows'], 1)
        for img in img_seq: self.set_image_center(img)
        self.alive_img = Animation.from_image_sequence(img_seq[:3:-1], 0.2)
        self.dead_img = Animation.from_image_sequence(img_seq[3::-1], 0.2)
        
    def twist(self):
        '''切换到鱼扭动的造型'''
        self.image = self.dead_img

    def set_start(self):
        '''鱼的起点'''
        if randint(1, 10) > 5:
            self.x = 0 - randint(512, 1024)
        else:
            self.x = randint(1536, 2048)
        self.y = randint(0, 768)
        self.point(512, 384)
        
    def swim(self, dt):
        '''鱼儿游动'''
        if time() - self.change_time > 3:
            self.change_time = time()
            if -512 < self.x < 1536 and -384 < self.y < 1152:
                if self.is_turn:
                    self.angle = randint(-10, 10)
                    self.acc = randint(-10, self.speed // 2)
        #随机转向、加减速移动
        self.left(self.angle * dt)
        self.move((self.speed + self.acc) * dt)
        #超出范围时让鱼消失
        if not (-1024 < self.x < 2048 and -768 < self.y < 1536):
            self.visible = False

    def check_dead(self, dt):
        '''鱼儿是否死亡'''
        if self.visible:
            self.death_time += 1 * dt
            if self.death_time > 1:
                self.visible = False
                

class BulletSprite(SpritePlus):
    '''炮弹精灵'''
    def __init__(self, x=0, y=0):
        super().__init__(img=bullet_img, x=x, y=y)
        self.set_sprite_center()
        self.speed = 300
        self.visible = True

    def fire_move(self, dt):
        if self.visible:
            self.move(self.speed * dt)
            if self.x < 0 or self.x > 1024 or self.y > 768:
                self.visible = False


class NetSprite(SpritePlus):
    '''渔网精灵'''
    def __init__(self, x=0, y=0):
        super().__init__(img=fishing_net_img, x=x, y=y)
        self.set_sprite_center()
        self.size = 0
        self.visible = True
        
    def open(self, dt):
        if self.scale <= 1:
            self.size += 300 * dt
            self.scale = self.size / 100
        else:
            self.visible = False


class CoinSprite(SpritePlus):
    '''硬币精灵'''
    def __init__(self, x=0, y=0, score=0):
        self.set_animation(score)
        super().__init__(img=self.coin_img, x=x, y=y)
        self.score = score
        self.speed = 400
        self.visible = True
        #面向窗口底部的硬币箱
        self.point(150, 0)

    def set_animation(self, score):
        '''设置动画'''
        image = silver_coin_img if score <= 20 else gold_coin_img
        coin_seq = pyglet.image.ImageGrid(image, 10, 1)
        self.coin_img = Animation.from_image_sequence(coin_seq, 0.02)
        self.set_image_center(self.coin_img)
        
    def move_down(self, dt):
        '''移动硬币'''
        if self.y > 0:
            self.move(self.speed * dt)
        else:
            self.visible = False
