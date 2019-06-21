import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
 
font = pygame.font.SysFont("arial", 16);
font_height = font.get_linesize()
event_text = []
 
while True:
 
    event = pygame.event.wait()
    event_text.append(str(event))
    #数组，代表屏幕显示多少条。所以与屏幕高度和字高度有关。负数索引说明只取最后一条开始的一屏幕的字。
    event_text = event_text[int(-SCREEN_SIZE[1]/font_height):]
    #一屏幕的字
 
    if event.type == QUIT:
        exit()
 
    screen.fill((255, 255, 255))
 
    y = SCREEN_SIZE[1]-font_height#找到屏幕最下方。
    #其实就是说从最后一行开始写，然后为了不重复倒退到前一行。替换所有（值）
    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y) )
        y-=font_height
        #否则叠在一起了，y列减去字符高度，
 
    pygame.display.update()