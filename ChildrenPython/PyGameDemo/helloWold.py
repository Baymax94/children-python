import pygame
import os
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import exit
#向sys模块借一个exit函数用来退出程序
 
pygame.init()
#初始化pygame,为使用硬件做准备
 
screen = pygame.display.set_mode((640, 480), 0, 32)
#创建了一个窗口
pygame.display.set_caption("Hello, World!")
#设置窗口标题
#os.path.realpath找到路径，然后r\,否则/
background = pygame.image.load(os.path.realpath('PyGameDemo/sushiplate.jpg')).convert()
#background = pygame.image.load(os.path.realpath(r'PyGameDemo\sushiplate.jpg')).convert()
mouse_cursor=pygame.image.load(os.path.realpath(r'PyGameDemo\fugu.png')).convert_alpha()
#加载并转换图像
 
while True:
#游戏主循环
 
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
 
    screen.blit(background, (0,0))
    #将背景图画上去
 
    x, y = pygame.mouse.get_pos()
    #获得鼠标位置(设置当中)
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去
 
    pygame.display.update()