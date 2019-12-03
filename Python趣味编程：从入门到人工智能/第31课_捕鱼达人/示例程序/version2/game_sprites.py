'''
程序：捕鱼达人的各个精灵v2
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
        self.set_animation(item)                #创建鱼的动画图像
        super().__init__(img = self.alive_img)  #调用父类的初始化方法
        self.name = name                        #鱼的名字
        self.life = item['life']                #生命值
        self.score = item['score']              #得分
        self.is_turn = item['turn']             #是否允许游动时转向
        self.is_capture = False                 #是否被捕获
        self.visible = True                     #是否可见
        self.death_time = 0                     #鱼挣扎死亡的时间
        self.change_time = time()               #鱼上次改变路线的时间
        self.angle = 0                          #旋转角度
        self.speed = item['speed']              #游动速度
        self.acc = 0                            #加速度
        self.set_start()                        #设置鱼游动的起点

    def set_animation(self, item = {}):
        '''设置动画'''
        image = pyglet.resource.image(item['file'])
        img_seq = pyglet.image.ImageGrid(image, item['rows'], 1)
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
        #每隔3秒改变游动路线
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
                
