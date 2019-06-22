import pygame
pygame.init()  # 启动pygame
screen = pygame.display.set_mode([800,600])  # 创建一个宽800像素，高600像素的显示窗口
keep_going = True
GREEN = (0,255,0)        # RGB color triplet for GREEN
radius = 50
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.draw.circle(screen,GREEN,(100,100),radius)
    pygame.display.update()
pygame.quit()