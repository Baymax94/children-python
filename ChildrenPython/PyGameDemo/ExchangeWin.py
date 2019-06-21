import pygame
from pygame.locals import *
from sys import exit
import os
 
SCREEN_SIZE = (640, 480)
 
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
 
background = pygame.image.load(os.path.realpath('PyGameDemo/sushiplate.jpg')).convert()
 
while True:
 
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to "+str(event.size))
 
    screen_width, screen_height = SCREEN_SIZE
    # 这里需要重新填满窗口
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
    #第一张图为（0，0）即左上角位置。根据步数说明，拉长的图。（x,0）,往下拉(0,y)。
    #for x in range(0, screen_width, background.get_width()):
        #screen.blit(background, (x, 0))
   
 
    pygame.display.update()