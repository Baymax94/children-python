'''
单摆模拟pygame版.py
'''
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import pygame
from pygame.locals import *

class Pendulum_ball:
    def __init__(self,rotate_center,rotate_radius,ball_radius):
        """参数依次为旋转中心，旋转半径，球的半径"""
        self.rc=rotate_center
        self.ra=rotate_radius
        self.r=ball_radius
        self.image=pygame.Surface((self.r*2,self.r*2))
        self.image.set_colorkey((0,0,0))
        p=self.r,self.r
        pygame.draw.circle(self.image,(255,0,0),p,self.r)
        p=self.rc[0]+self.ra,self.rc[1]
        self.rect=self.image.get_rect(center=p)
        self.angle=0    # 和x轴的角度
        self.da=0       # 每次增加的角度，角速度
        self.line=pygame.Surface((self.ra,2))    # 线条属性

    def update(self):
        self.angle=self.angle+self.da
        if self.angle > -90:
            self.da = self.da - 0.5  # 0.5是角加速度
        elif self.angle < -90:
            self.da = self.da + 0.5
        x = self.rc[0] + self.ra * math.cos(math.radians(self.angle))
        y = self.rc[1] - self.ra * math.sin(math.radians(self.angle))
        self.rect.center = x, y

    def draw(self,screen):
        """首先画线，然后画球"""
        start=self.rc
        end=self.rect.center
        pygame.draw.line(screen,(125,0,0),start,end,2)
        screen.blit(self.image,self.rect)

width,height=480,360
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("单摆模拟pygame版")
ball = Pendulum_ball((width//2,100),200,10)

clock=pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type==QUIT:running=False
    ball.update()
    screen.fill((0,0,0))
    ball.draw(screen)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
