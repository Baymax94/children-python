import pygame
from random import randint
from pygame.locals import *
width,height=480,360
xy=width//2,height//2
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("整体透明度图像的mask测试程序.py")
# baymax=pygame.image.load('baymax.png').convert()
baymax=pygame.image.load('F://GitHub//children-python//风火轮编程//Python创意编程//baymax.png').convert()

rect=baymax.get_rect(center=xy)
baymax.set_alpha(40)
baymax.set_colorkey((255,255,255))
mask=pygame.mask.from_surface(baymax)
w,h=rect.size

screen.blit(baymax,rect)
pygame.display.update()

while True:
    x=randint(0,w-1)
    y=randint(0,h-1)
    print(mask.get_at((x,y)),end=' ')

